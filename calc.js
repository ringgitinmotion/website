/* Ringgit in Motion — shared calculator helpers (no libraries, no tracking). */
(function () {
  const RIM = {};
  RIM.$ = (id) => document.getElementById(id);
  RIM.rm = (v) => "RM" + Math.round(v).toLocaleString("en-MY");
  RIM.rmShort = (v) => {
    if (Math.abs(v) >= 1e6) return "RM" + (v / 1e6).toFixed(Math.abs(v) >= 1e7 ? 0 : 1).replace(/\.0$/, "") + "M";
    if (Math.abs(v) >= 1e3) return "RM" + Math.round(v / 1e3) + "K";
    return "RM" + Math.round(v);
  };
  /* value after n months of paying m at the end of each month, monthly compounding */
  RIM.fv = (m, annualPct, months) => {
    const r = annualPct / 100 / 12;
    return r === 0 ? m * months : (m * (Math.pow(1 + r, months) - 1)) / r;
  };
  /* a lump sum after n months, monthly compounding */
  RIM.grow = (p, annualPct, months) => p * Math.pow(1 + annualPct / 100 / 12, months);

  /*
   * Wire number boxes + sliders to a state object, remember it per visitor, call render on change.
   * fields: {key: [min, max]}; ids are <key> (number box) and <key>R (slider).
   */
  RIM.form = (storeKey, defaults, fields, render) => {
    const keys = Object.keys(defaults);
    let state = { ...defaults };
    try {
      const saved = JSON.parse(localStorage.getItem(storeKey) || "null");
      if (saved) keys.forEach((k) => { if (typeof saved[k] === "number" && isFinite(saved[k])) state[k] = saved[k]; });
    } catch (e) {}
    const clamp = (k, v) => Math.min(fields[k][1], Math.max(fields[k][0], v));
    const sync = () => keys.forEach((k) => {
      RIM.$(k).value = state[k];
      const r = RIM.$(k + "R");
      if (r) r.value = Math.min(Number(r.max), Math.max(Number(r.min), state[k]));
    });
    const go = () => {
      render(state);
      try { localStorage.setItem(storeKey, JSON.stringify(state)); } catch (e) {}
    };
    keys.forEach((k) => {
      RIM.$(k).addEventListener("input", () => {
        const v = parseFloat(RIM.$(k).value);
        if (!isFinite(v)) return;
        state[k] = clamp(k, v);
        const r = RIM.$(k + "R");
        if (r) r.value = Math.min(Number(r.max), state[k]);
        go();
      });
      RIM.$(k).addEventListener("change", sync);
      const r = RIM.$(k + "R");
      if (r) r.addEventListener("input", () => { state[k] = clamp(k, parseFloat(r.value)); RIM.$(k).value = state[k]; go(); });
    });
    document.querySelectorAll("form").forEach((f) => f.addEventListener("submit", (e) => e.preventDefault()));
    const reset = RIM.$("reset");
    if (reset) reset.addEventListener("click", () => { state = { ...defaults }; sync(); go(); RIM.toast("Back to the example numbers."); });
    sync();
    go();
    return () => state;
  };

  RIM.toast = (msg) => { const t = RIM.$("toast"); if (t) t.textContent = msg; };
  /* copy a line of text; if the browser refuses, show it selected so it can be copied by hand */
  RIM.copy = (text) => {
    const done = () => RIM.toast("Copied. Paste it anywhere.");
    const fallback = () => {
      const t = RIM.$("toast");
      t.textContent = text;
      const range = document.createRange();
      range.selectNodeContents(t);
      const sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
    };
    try { navigator.clipboard.writeText(text).then(done, fallback); } catch (e) { fallback(); }
  };

  /*
   * Chart over years. series: [{kind: "area-v"|"area-p"|"line-v"|"line-n", values: [...per year]}]
   * The last series' end value gets a dot and a label.
   */
  RIM.chart = (svg, years, series, endKey) => {
    const W = 640, H = 280, L = 62, Rr = 96, T = 16, B = 30;
    const all = series.flatMap((s) => s.values);
    const maxV = Math.max(1, ...all);
    const mag = Math.pow(10, Math.floor(Math.log10(maxV)));
    const step = [1, 2, 2.5, 5, 10].map((s) => (s * mag) / 10).find((s) => maxV / s <= 5) || mag;
    const yMax = Math.ceil(maxV / step) * step;
    const X = (y) => L + (y / Math.max(1, years)) * (W - L - Rr);
    const Y = (v) => T + (1 - v / yMax) * (H - T - B);
    let s = "";
    for (let v = 0; v <= yMax + 1e-6; v += step) {
      s += `<line class="gridline" x1="${L}" x2="${W - Rr}" y1="${Y(v).toFixed(1)}" y2="${Y(v).toFixed(1)}"/>`;
      s += `<text class="tick" x="${L - 8}" y="${(Y(v) + 4).toFixed(1)}" text-anchor="end">${RIM.rmShort(v)}</text>`;
    }
    const xStep = years <= 10 ? 2 : years <= 25 ? 5 : 10;
    for (let y = 0; y <= years; y += xStep) s += `<text class="tick" x="${X(y).toFixed(1)}" y="${H - 10}" text-anchor="middle">${y === 0 ? "YR 0" : y}</text>`;
    series.forEach((ser) => {
      const pts = ser.values.map((v, y) => `${X(y).toFixed(1)} ${Y(v).toFixed(1)}`);
      if (ser.kind.startsWith("area")) s += `<path class="${ser.kind}" d="M ${X(0)} ${Y(0)} L ${pts.join(" L ")} L ${X(years)} ${Y(0)} Z"/>`;
      else s += `<path class="${ser.kind}" d="M ${pts.join(" L ")}"/>`;
    });
    const end = series.find((x) => x.key === endKey) || series[series.length - 1];
    const ev = end.values[end.values.length - 1];
    s += `<circle class="dot" cx="${X(years)}" cy="${Y(ev).toFixed(1)}" r="6"/>`;
    s += `<text class="endlbl" x="${X(years) + 12}" y="${(Y(ev) + 5).toFixed(1)}">${RIM.rmShort(ev)}</text>`;
    svg.innerHTML = s;
  };

  window.RIM = RIM;
})();
