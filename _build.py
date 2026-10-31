"""Builds the Ringgit in Motion site: shared head/nav/footer + each page's body. Run: python _build.py"""
from pathlib import Path

HERE = Path(__file__).resolve().parent

PAGES = [
    # file, nav label, keyword
    ("kopi.html", "Kopi", "KOPI"),
    ("budget.html", "50/30/20", "JOM"),
    ("compound.html", "Compound", "GROW"),
    ("real-return.html", "Real return", "MONEY"),
    ("debt.html", "Debt", "LOAN"),
    ("emergency.html", "Emergency", "COVER"),
    ("raise.html", "Raise", "MORE"),
    ("epf.html", "EPF", "BONUS"),
    ("park.html", "Park cash", "POCKET"),
    ("bnpl.html", "BNPL", "TOTAL"),
]


def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="logo.png">
<link rel="icon" href="logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anybody:wdth,wght@50..150,500..900&family=Fraunces:ital,opsz,wght@1,9..144,420&family=JetBrains+Mono:wght@500;700&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
"""


def nav(current):
    links = "".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == current else ""}>{label}</a>' for f, label, _ in PAGES
    )
    return f"""<header class="nav">
  <a class="brand" href="index.html"><img src="logo.png" alt=""><span>Ringgit <em>in motion</em></span></a>
  <nav class="links" aria-label="Calculators">{links}</nav>
</header>
"""


FOOTER = """<footer>
  <p class="fine">Ringgit in Motion makes money basics simple, with short animated posts on Instagram (@ringgitinmotion).</p>
  <p class="fine">These calculators are illustrations for learning, not financial advice. They assume steady returns; real returns, fees, taxes and inflation vary. Nothing you type leaves your device.</p>
</footer>
<script src="calc.js"></script>
"""


def page(file, title, desc, body, script):
    html = head(title, desc) + nav(file) + "<main>\n" + body + "\n</main>\n" + FOOTER + "<script>\n" + script + "\n</script>\n</body>\n</html>\n"
    (HERE / file).write_text(html, encoding="utf-8")
    print("wrote", file)


def field(id_, label, value, rmin, rmax, step, nmin, nmax, hint=""):
    h = f'\n      <span class="hint">{hint}</span>' if hint else ""
    return f"""    <div class="field">
      <div class="row"><label for="{id_}">{label}</label><input class="num" id="{id_}" type="number" min="{nmin}" max="{nmax}" step="{step}" value="{value}" inputmode="decimal"></div>
      <input id="{id_}R" type="range" min="{rmin}" max="{rmax}" step="{step}" value="{value}" aria-label="{label} slider">{h}
    </div>"""


def card(lead, big, lines, legend=""):
    rows = "\n".join(
        f'      <div{" class=\"gold\"" if gold else ""}><dt>{dt}</dt><dd id="{id_}">-</dd></div>' for dt, id_, gold in lines
    )
    return f"""  <div class="card" aria-live="polite">
    <p class="lead" id="lead">{lead}</p>
    <p class="big" id="big">{big}</p>
    <div class="split" aria-hidden="true"><i id="splitA"></i><i id="splitB"></i><i id="splitC"></i></div>
    <div class="legend">{legend}</div>
    <dl class="lines">
{rows}
    </dl>
    <div class="actions">
      <button type="button" id="copy">Copy my result</button>
      <button type="button" class="ghost" id="reset">Reset example</button>
      <span class="toast" id="toast" role="status"></span>
    </div>
  </div>"""


def mast(eyebrow, q, h1):
    return f"""<section class="mast">
  <div class="eyebrow">{eyebrow}</div>
  <p class="q">{q}</p>
  <h1>{h1}</h1>
</section>"""


# ---------------------------------------------------------------- home
tiles = [
    ("kopi.html", "KOPI", "Kopi calculator", "What your daily coffee would grow to if you invested it instead."),
    ("budget.html", "JOM", "50/30/20 budget", "Split your take-home pay into needs, wants and savings."),
    ("compound.html", "GROW", "Compound calculator", "Watch a monthly amount grow over the years, and see what waiting costs."),
    ("real-return.html", "MONEY", "Real return", "What your savings can really buy after inflation."),
    ("debt.html", "LOAN", "Debt payoff", "How long your debt takes to clear, what it costs, and how much paying a bit more saves."),
    ("emergency.html", "COVER", "Emergency fund", "Your 3 to 6 month safety net: how much you need and when you’ll get there."),
    ("raise.html", "MORE", "Raise calculator", "Got a raise? See what saving part of it grows into, before lifestyle creep eats it."),
    ("epf.html", "BONUS", "EPF calculator", "What you and your boss put into KWSP each month, the 3 accounts, and what it grows to."),
    ("park.html", "POCKET", "Park your cash", "Savings account, fixed deposit or ASB: what the same money earns in each, and the catches."),
    ("bnpl.html", "TOTAL", "BNPL calculator", "Add up every buy now, pay later plan, see the share of your pay, and what a monthly fee really costs."),
]
home_body = """<section class="hero">
  <img src="logo.png" alt="Ringgit in Motion logo: a gold RM coin in motion">
  <div>
    <div class="eyebrow">Ringgit in Motion</div>
    <h1>Make your money <span>move.</span></h1>
    <p class="tagline">Free money calculators for Malaysians. No sign-up, nothing to install.</p>
  </div>
</section>
<section class="mid" aria-label="Calculators">
  <h2>Pick a calculator</h2>
  <p>Came from a post? The keyword you commented is on its tile.</p>
  <div class="grid4">
""" + "\n".join(
    f'    <a class="tile" href="{f}"><span class="kw">{kw}</span><h3>{t}</h3><p>{d}</p></a>' for f, kw, t, d in tiles
) + """
  </div>
</section>"""
page("index.html", "Ringgit in Motion", "Free money calculators for Malaysians: coffee, 50/30/20 budget, compound growth and real return after inflation.", home_body, "")

# ---------------------------------------------------------------- kopi
kopi_body = mast("Kopi calculator · comment KOPI", "what does your daily coffee really cost?", "Kopi <span>Calculator</span>") + """
<section class="tool" aria-label="Kopi calculator">
  <form class="controls" autocomplete="off">
""" + "\n".join([
    field("price", "Price per cup (RM)", 15, 1, 40, 0.5, 0, 100),
    field("cups", "Cups a month", 22, 1, 60, 1, 0, 120, "22 is one cup every workday."),
    '    <div class="divider"></div>',
    field("rate", "Yearly return (%)", 6, 0, 12, 0.1, 0, 20, "An assumption. Real returns go up and down."),
    field("years", "Years", 20, 1, 40, 1, 1, 50),
]) + """
  </form>
  <div class="stack">
""" + card("RM330 a month, invested for 20 years at 6%, grows to", "RM152,473", [
    ("Spent on coffee a month", "monthly", False), ("A year", "yearly", False),
    ("You put in", "paid", False), ("Growth on top", "growth", True)],
    '<span><b style="background: var(--brand-ink)"></b>You put in</span><span><b style="background: var(--gold-fill)"></b>Growth</span>') + """
    <figure><svg class="chart" id="chart" viewBox="0 0 640 280" role="img" aria-label="Growth chart"></svg>
      <figcaption>The lilac area is what you put in. The gold above it is growth from compounding.</figcaption></figure>
  </div>
</section>
<section class="mid" aria-label="Middle ground">
  <h2>Don’t want to quit? Skip a few.</h2>
  <div class="field" style="max-width: 520px;">
    <div class="row"><label for="skip">Cups you skip a week</label><input class="num" id="skip" type="number" min="0" max="21" step="1" value="3" inputmode="numeric"></div>
    <input id="skipR" type="range" min="0" max="14" step="1" value="3" aria-label="Cups skipped a week slider">
  </div>
  <p class="out" id="skipOut"></p>
</section>"""
kopi_js = r"""
const { $, rm, fv } = RIM;
RIM.form("rim-kopi", { price: 15, cups: 22, rate: 6, years: 20, skip: 3 },
  { price: [0, 100], cups: [0, 120], rate: [0, 20], years: [1, 50], skip: [0, 21] }, (s) => {
  const m = s.price * s.cups, n = s.years * 12, total = fv(m, s.rate, n), paid = m * n;
  $("lead").textContent = `${rm(m)} a month, invested for ${s.years} year${s.years === 1 ? "" : "s"} at ${s.rate}%, grows to`;
  $("big").textContent = rm(total);
  $("monthly").textContent = rm(m); $("yearly").textContent = rm(m * 12);
  $("paid").textContent = rm(paid); $("growth").textContent = rm(Math.max(0, total - paid));
  const pp = total > 0 ? (paid / total) * 100 : 100;
  $("splitA").style.cssText = `width:${pp}%;background:var(--brand-ink)`; $("splitB").style.cssText = `width:${100 - pp}%;background:var(--gold-fill)`; $("splitC").style.width = "0";
  const yrs = [...Array(s.years + 1)].map((_, y) => y);
  RIM.chart($("chart"), s.years, [{ kind: "area-v", key: "v", values: yrs.map((y) => fv(m, s.rate, 12 * y)) }, { kind: "area-p", values: yrs.map((y) => m * 12 * y) }, { kind: "line-v", key: "v", values: yrs.map((y) => fv(m, s.rate, 12 * y)) }], "v");
  const sm = (s.price * s.skip * 52) / 12;
  $("skipOut").innerHTML = s.skip === 0 ? "Set how many cups you would skip each week to see what that alone could grow to."
    : `Skipping ${s.skip} cup${s.skip === 1 ? "" : "s"} a week frees up <strong>${rm(sm)}</strong> a month, which grows to <strong>${rm(fv(sm, s.rate, n))}</strong> in ${s.years} years.`;
  window.__copy = `My RM${s.price} coffee, ${s.cups} cups a month = ${rm(m)}/month. Invested at ${s.rate}% for ${s.years} years, that's about ${rm(total)}. (Ringgit in Motion Kopi Calculator, illustration only)`;
});
$("copy").addEventListener("click", () => RIM.copy(window.__copy));
"""
page("kopi.html", "Kopi Calculator · Ringgit in Motion", "What your daily coffee would grow to if you invested the money instead.", kopi_body, kopi_js)

# ---------------------------------------------------------------- 50/30/20
budget_body = mast("50/30/20 budget · comment JOM", "where should your paycheck go?", "50/30/20 <span>Budget</span>") + """
<section class="tool" aria-label="50/30/20 budget calculator">
  <form class="controls" autocomplete="off">
""" + "\n".join([
    field("pay", "Take-home pay a month (RM)", 4000, 1000, 20000, 50, 0, 1000000, "After EPF, SOCSO and tax: what lands in your bank."),
    '    <div class="divider"></div>',
    field("needs", "Needs (%)", 50, 20, 80, 1, 0, 100, "Rent, food, transport, bills. If yours cost more than 50%, set your real number."),
    field("save", "Savings (%)", 20, 0, 50, 1, 0, 100, "Emergency fund first, then investing and extra debt payments."),
]) + """
  </form>
  <div class="stack">
""" + card("Your RM4,000 a month splits into", "50/30/20", [
    ("Needs a month", "needsA", False), ("Wants a month", "wantsA", False),
    ("Savings a month", "saveA", True), ("Savings in a year", "saveY", True)],
    '<span><b style="background: var(--brand-ink)"></b>Needs</span><span><b style="background: rgba(255,243,224,.55)"></b>Wants</span><span><b style="background: var(--gold-fill)"></b>Savings</span>') + """
  </div>
</section>
<section class="mid" aria-label="What the savings become">
  <h2>What your savings could become</h2>
  <p class="out" id="growOut"></p>
  <p class="fine">Assumes the savings are invested at 6% a year, compounded monthly. Real returns go up and down.</p>
</section>"""
budget_js = r"""
const { $, rm, fv } = RIM;
RIM.form("rim-budget", { pay: 4000, needs: 50, save: 20 }, { pay: [0, 1000000], needs: [0, 100], save: [0, 100] }, (s) => {
  let needs = s.needs, save = Math.min(s.save, 100 - needs), wants = Math.max(0, 100 - needs - save);
  const a = (p) => (s.pay * p) / 100;
  $("lead").textContent = `Your ${rm(s.pay)} a month splits into`;
  $("big").textContent = `${Math.round(needs)}/${Math.round(wants)}/${Math.round(save)}`;
  $("needsA").textContent = rm(a(needs)); $("wantsA").textContent = rm(a(wants));
  $("saveA").textContent = rm(a(save)); $("saveY").textContent = rm(a(save) * 12);
  $("splitA").style.cssText = `width:${needs}%;background:var(--brand-ink)`;
  $("splitB").style.cssText = `width:${wants}%;background:rgba(255,243,224,.55)`;
  $("splitC").style.cssText = `width:${save}%;background:var(--gold-fill)`;
  const m = a(save);
  $("growOut").innerHTML = m <= 0 ? "Set a savings percentage to see what it could grow to."
    : `Saving <strong>${rm(m)}</strong> a month could grow to <strong>${rm(fv(m, 6, 120))}</strong> in 10 years and <strong>${rm(fv(m, 6, 240))}</strong> in 20.`;
  window.__copy = `My 50/30/20 on ${rm(s.pay)}: needs ${rm(a(needs))}, wants ${rm(a(wants))}, savings ${rm(a(save))} a month. (Ringgit in Motion budget calculator)`;
});
$("copy").addEventListener("click", () => RIM.copy(window.__copy));
"""
page("budget.html", "50/30/20 Budget · Ringgit in Motion", "Split your take-home pay into needs, wants and savings with the 50/30/20 rule.", budget_body, budget_js)

# ---------------------------------------------------------------- compound
comp_body = mast("Compound calculator · comment GROW", "how much could a little each month become?", "Compound <span>Calculator</span>") + """
<section class="tool" aria-label="Compound calculator">
  <form class="controls" autocomplete="off">
""" + "\n".join([
    field("monthly", "Each month (RM)", 100, 10, 3000, 10, 0, 1000000),
    field("start", "Starting amount (RM)", 0, 0, 50000, 100, 0, 100000000, "Money you already have to put in on day one."),
    '    <div class="divider"></div>',
    field("rate", "Yearly return (%)", 6, 0, 12, 0.1, 0, 20, "An assumption. Real returns go up and down."),
    field("years", "Years", 30, 1, 45, 1, 1, 60),
]) + """
  </form>
  <div class="stack">
""" + card("RM100 a month for 30 years at 6% grows to", "RM100,452", [
    ("You put in", "paid", False), ("Growth on top", "growth", True), ("Growth share of the total", "share", True)],
    '<span><b style="background: var(--brand-ink)"></b>You put in</span><span><b style="background: var(--gold-fill)"></b>Growth</span>') + """
    <figure><svg class="chart" id="chart" viewBox="0 0 640 280" role="img" aria-label="Growth chart"></svg>
      <figcaption>The lilac area is what you put in. The gold above it is growth, and it speeds up over time.</figcaption></figure>
  </div>
</section>
<section class="mid" aria-label="Cost of waiting">
  <h2>What does waiting cost?</h2>
  <div class="field" style="max-width: 520px;">
    <div class="row"><label for="delay">Start this many years later</label><input class="num" id="delay" type="number" min="0" max="40" step="1" value="10" inputmode="numeric"></div>
    <input id="delayR" type="range" min="0" max="20" step="1" value="10" aria-label="Years later slider">
  </div>
  <p class="out" id="waitOut"></p>
</section>"""
comp_js = r"""
const { $, rm, fv, grow } = RIM;
const total = (s, months) => fv(s.monthly, s.rate, months) + grow(s.start, s.rate, months);
RIM.form("rim-compound", { monthly: 100, start: 0, rate: 6, years: 30, delay: 10 },
  { monthly: [0, 1000000], start: [0, 100000000], rate: [0, 20], years: [1, 60], delay: [0, 40] }, (s) => {
  const n = s.years * 12, t = total(s, n), paid = s.start + s.monthly * n, g = Math.max(0, t - paid);
  $("lead").textContent = `${rm(s.monthly)} a month${s.start ? ` plus ${rm(s.start)} up front` : ""} for ${s.years} years at ${s.rate}% grows to`;
  $("big").textContent = rm(t);
  $("paid").textContent = rm(paid); $("growth").textContent = rm(g);
  $("share").textContent = t > 0 ? Math.round((g / t) * 100) + "%" : "0%";
  const pp = t > 0 ? (paid / t) * 100 : 100;
  $("splitA").style.cssText = `width:${pp}%;background:var(--brand-ink)`; $("splitB").style.cssText = `width:${100 - pp}%;background:var(--gold-fill)`; $("splitC").style.width = "0";
  const yrs = [...Array(s.years + 1)].map((_, y) => y);
  const v = yrs.map((y) => total(s, 12 * y)), p = yrs.map((y) => s.start + s.monthly * 12 * y);
  RIM.chart($("chart"), s.years, [{ kind: "area-v", key: "v", values: v }, { kind: "area-p", values: p }, { kind: "line-v", key: "v", values: v }], "v");
  const left = Math.max(0, s.years - s.delay), late = total(s, left * 12);
  $("waitOut").innerHTML = s.delay === 0 ? "Starting today gives you the full result above."
    : s.delay >= s.years ? `Waiting ${s.delay} years leaves no time to grow inside a ${s.years}-year plan.`
    : `Start ${s.delay} year${s.delay === 1 ? "" : "s"} later and you end with <strong>${rm(late)}</strong>. Waiting costs about <strong>${rm(t - late)}</strong>.`;
  window.__copy = `${rm(s.monthly)} a month for ${s.years} years at ${s.rate}% grows to about ${rm(t)}. I only put in ${rm(paid)}. (Ringgit in Motion compound calculator, illustration only)`;
});
$("copy").addEventListener("click", () => RIM.copy(window.__copy));
"""
page("compound.html", "Compound Calculator · Ringgit in Motion", "See how a monthly amount grows with compound interest, and what waiting costs.", comp_body, comp_js)

# ---------------------------------------------------------------- real return
real_body = mast("Real return · comment MONEY", "is your savings account keeping up with prices?", "Real <span>Return</span>") + """
<section class="tool" aria-label="Real return calculator">
  <form class="controls" autocomplete="off">
""" + "\n".join([
    field("bal", "Savings balance (RM)", 10000, 500, 200000, 500, 0, 100000000),
    field("rate", "Interest rate (% a year)", 0.25, 0, 6, 0.05, 0, 20, "Basic savings at the big banks pay about 0.25%. Check your own account."),
    field("infl", "Inflation (% a year)", 1.9, 0, 6, 0.1, 0, 20, "Malaysia: 1.9% in August 2026 (DOSM)."),
    field("years", "Years", 10, 1, 40, 1, 1, 60),
]) + """
  </form>
  <div class="stack">
""" + card("After 10 years your RM10,000 can really buy", "RM8,494", [
    ("Balance your app shows", "nominal", False), ("Buying power lost vs today", "lost", False),
    ("Your real return a year", "real", True), ("Rate needed to break even", "even", True)],
    '<span><b style="background: var(--brand-ink)"></b>What it buys</span><span><b style="background: var(--gold-fill)"></b>Lost to prices</span>') + """
    <figure><svg class="chart" id="chart" viewBox="0 0 640 280" role="img" aria-label="Balance versus buying power chart"></svg>
      <figcaption>The dashed line is the balance your app shows. The gold area is what that money can actually buy, in today’s ringgit.</figcaption></figure>
  </div>
</section>"""
real_js = r"""
const { $, rm } = RIM;
RIM.form("rim-real", { bal: 10000, rate: 0.25, infl: 1.9, years: 10 }, { bal: [0, 100000000], rate: [0, 20], infl: [0, 20], years: [1, 60] }, (s) => {
  const nomAt = (y) => s.bal * Math.pow(1 + s.rate / 100, y);
  const realAt = (y) => nomAt(y) / Math.pow(1 + s.infl / 100, y);
  const nom = nomAt(s.years), real = realAt(s.years), lost = Math.max(0, s.bal - real);
  const rr = ((1 + s.rate / 100) / (1 + s.infl / 100) - 1) * 100;
  $("lead").textContent = `After ${s.years} year${s.years === 1 ? "" : "s"} your ${rm(s.bal)} can really buy`;
  $("big").textContent = rm(real);
  $("nominal").textContent = rm(nom);
  $("lost").textContent = rm(lost);
  $("real").textContent = (rr >= 0 ? "+" : "") + rr.toFixed(2) + "%";
  $("even").textContent = "above " + s.infl + "%";
  const pr = nom > 0 ? (real / nom) * 100 : 100;
  $("splitA").style.cssText = `width:${Math.min(100, pr)}%;background:var(--brand-ink)`; $("splitB").style.cssText = `width:${Math.max(0, 100 - pr)}%;background:var(--gold-fill)`; $("splitC").style.width = "0";
  const yrs = [...Array(s.years + 1)].map((_, y) => y);
  RIM.chart($("chart"), s.years, [{ kind: "area-v", key: "r", values: yrs.map(realAt) }, { kind: "line-n", values: yrs.map(nomAt) }], "r");
  window.__copy = `My ${rm(s.bal)} at ${s.rate}% with ${s.infl}% inflation: in ${s.years} years it shows ${rm(nom)} but buys only ${rm(real)} in today's money. (Ringgit in Motion real-return calculator)`;
});
$("copy").addEventListener("click", () => RIM.copy(window.__copy));
"""
page("real-return.html", "Real Return Calculator · Ringgit in Motion", "What your savings can really buy after inflation, in Malaysian ringgit.", real_body, real_js)

# ---------------------------------------------------------------- debt payoff
debt_body = mast("Debt payoff · comment LOAN", "how long until you’re debt-free?", "Debt <span>Payoff</span>") + """
<section class="tool" aria-label="Debt payoff calculator">
  <form class="controls" autocomplete="off">
""" + "\n".join([
    field("bal", "Amount you owe (RM)", 5000, 500, 50000, 100, 0, 10000000),
    field("rate", "Interest rate (% a year)", 18, 0, 30, 0.1, 0, 60, "Malaysian credit cards charge 15–18% a year, depending on your repayment record."),
    field("pay", "You pay each month (RM)", 250, 50, 3000, 10, 0, 10000000, "Paying only the minimum keeps you in debt far longer."),
]) + """
  </form>
  <div class="stack">
""" + card("RM5,000 at 18%, paying RM250 a month, is cleared in", "24 months", [
    ("Total interest", "interest", True), ("Total you pay back", "total", False),
    ("Interest share of what you pay", "share", False)],
    '<span><b style="background: var(--brand-ink)"></b>What you borrowed</span><span><b style="background: var(--gold-fill)"></b>Interest</span>') + """
    <figure><svg class="chart" id="chart" viewBox="0 0 640 280" role="img" aria-label="Balance over time"></svg>
      <figcaption>Your balance month by month until it reaches zero.</figcaption></figure>
  </div>
</section>
<section class="mid" aria-label="Pay a bit more">
  <h2>What if you pay a bit more?</h2>
  <div class="field" style="max-width: 520px;">
    <div class="row"><label for="extra">Extra each month (RM)</label><input class="num" id="extra" type="number" min="0" max="1000000" step="10" value="100" inputmode="decimal"></div>
    <input id="extraR" type="range" min="0" max="1000" step="10" value="100" aria-label="Extra payment slider">
  </div>
  <p class="out" id="extraOut"></p>
</section>"""
debt_js = r"""
const { $, rm } = RIM;
// month-by-month payoff: interest is added, then the payment comes off
const payoff = (bal, apr, pay) => {
  const r = apr / 1200;
  if (pay <= bal * r + 0.005) return null; // payment doesn't even cover the interest
  let b = bal, months = 0, interest = 0;
  const path = [b];
  while (b > 0.005 && months < 1200) {
    const i = b * r;
    interest += i;
    b = Math.max(0, b + i - pay);
    months++;
    path.push(b);
  }
  return { months, interest, total: bal + interest, path };
};
const span = (m) => {
  const y = Math.floor(m / 12), mo = m % 12;
  return [y ? `${y} year${y === 1 ? "" : "s"}` : "", mo ? `${mo} month${mo === 1 ? "" : "s"}` : ""].filter(Boolean).join(" ") || "0 months";
};
RIM.form("rim-debt", { bal: 5000, rate: 18, pay: 250, extra: 100 }, { bal: [0, 10000000], rate: [0, 60], pay: [0, 10000000], extra: [0, 1000000] }, (s) => {
  const p = payoff(s.bal, s.rate, s.pay);
  $("lead").textContent = `${rm(s.bal)} at ${s.rate}%, paying ${rm(s.pay)} a month, is cleared in`;
  if (!p) {
    const need = (s.bal * s.rate) / 1200;
    $("big").textContent = "Never";
    $("interest").textContent = `${rm(need)}+ a month`;
    $("total").textContent = "keeps growing";
    $("share").textContent = "-";
    $("splitA").style.cssText = "width:0"; $("splitB").style.cssText = "width:100%;background:var(--gold-fill)"; $("splitC").style.width = "0";
    $("chart").innerHTML = "";
    $("extraOut").innerHTML = `Your payment doesn’t cover the monthly interest of about <strong>${rm(need)}</strong>, so the debt never shrinks. Pay more than that, or ask your bank about a lower-rate option.`;
    window.__copy = `My ${rm(s.bal)} debt at ${s.rate}% never shrinks if I pay ${rm(s.pay)} a month. (Ringgit in Motion debt calculator)`;
    return;
  }
  $("big").textContent = span(p.months);
  $("interest").textContent = rm(p.interest);
  $("total").textContent = rm(p.total);
  $("share").textContent = Math.round((p.interest / p.total) * 100) + "%";
  const pp = (s.bal / p.total) * 100;
  $("splitA").style.cssText = `width:${pp}%;background:var(--brand-ink)`; $("splitB").style.cssText = `width:${100 - pp}%;background:var(--gold-fill)`; $("splitC").style.width = "0";
  RIM.chart($("chart"), p.months, [{ kind: "area-v", key: "b", values: p.path }], "b", "MO");
  const q = payoff(s.bal, s.rate, s.pay + s.extra);
  $("extraOut").innerHTML = s.extra <= 0 || !q ? "Add an extra amount to see how much sooner you’d be debt-free."
    : `Paying <strong>${rm(s.pay + s.extra)}</strong> a month clears it in ${span(q.months)}: <strong>${span(p.months - q.months)}</strong> sooner, and <strong>${rm(p.interest - q.interest)}</strong> less interest.`;
  window.__copy = `My ${rm(s.bal)} debt at ${s.rate}%, paying ${rm(s.pay)} a month: debt-free in ${span(p.months)}, ${rm(p.interest)} in interest. (Ringgit in Motion debt calculator)`;
});
$("copy").addEventListener("click", () => RIM.copy(window.__copy));
"""
page("debt.html", "Debt Payoff Calculator · Ringgit in Motion", "How long your debt takes to clear, what it costs in interest, and how much paying a bit more saves.", debt_body, debt_js)

# ---------------------------------------------------------------- emergency fund
ef_body = mast("Emergency fund · comment COVER", "how big should your safety net be?", "Emergency <span>Fund</span>") + """
<section class="tool" aria-label="Emergency fund calculator">
  <form class="controls" autocomplete="off">
    <p class="hint">Your must-pays each month. Leave out shopping, eating out and holidays.</p>
""" + "\n".join([
    field("rent", "Rent or home loan (RM)", 1200, 0, 5000, 50, 0, 1000000),
    field("food", "Groceries and meals (RM)", 800, 0, 3000, 50, 0, 1000000),
    field("trans", "Transport (RM)", 400, 0, 2000, 50, 0, 1000000, "Petrol, toll, parking, LRT, car loan."),
    field("bills", "Bills and insurance (RM)", 600, 0, 3000, 50, 0, 1000000, "Utilities, phone, internet, insurance, other loan repayments."),
    field("other", "Anything else you must pay (RM)", 0, 0, 3000, 50, 0, 1000000, "For example, support for parents or childcare."),
    '    <div class="divider"></div>',
    field("months", "Months to cover", 6, 3, 12, 1, 1, 24, "3 is the minimum. 6 is safer, especially if your income is irregular."),
    field("saved", "Already saved (RM)", 2000, 0, 50000, 100, 0, 100000000),
    field("monthly", "You can save each month (RM)", 500, 0, 3000, 50, 0, 1000000),
]) + """
  </form>
  <div class="stack">
""" + card("Your RM3,000 of essentials × 6 months =", "RM18,000", [
    ("You have now", "have", False), ("Still to save", "left", False),
    ("3-month mark", "at3", True), ("Full goal reached", "atGoal", True)],
    '<span><b style="background: var(--gold-fill)"></b>Saved</span><span><b style="background: rgba(255,243,224,.25)"></b>Still to save</span>') + """
    <figure><svg class="chart" id="chart" viewBox="0 0 640 280" role="img" aria-label="Savings path to the goal"></svg>
      <figcaption>Your fund month by month until it reaches the goal, if you keep saving the same amount.</figcaption></figure>
  </div>
</section>
<section class="mid" aria-label="Where to keep it">
  <h2>Where to keep it</h2>
  <p class="out">Somewhere <strong>separate</strong> from your spending account, that you can reach <strong>within a day</strong>, and that’s protected (check for <strong>PIDM</strong> cover). Not in shares or crypto: the point is that it’s there when you need it.</p>
  <p class="fine">Use it for real emergencies only: job loss, medical bills, urgent repairs. Then top it back up.</p>
</section>"""
ef_js = r"""
const { $, rm } = RIM;
const span = (m) => {
  const y = Math.floor(m / 12), mo = m % 12;
  return [y ? `${y} year${y === 1 ? "" : "s"}` : "", mo ? `${mo} month${mo === 1 ? "" : "s"}` : ""].filter(Boolean).join(" ") || "now";
};
const when = (have, need, monthly) => (have >= need ? "done ✓" : monthly <= 0 ? "set a monthly amount" : "in " + span(Math.ceil((need - have) / monthly)));
RIM.form("rim-emergency", { rent: 1200, food: 800, trans: 400, bills: 600, other: 0, months: 6, saved: 2000, monthly: 500 },
  { rent: [0, 1000000], food: [0, 1000000], trans: [0, 1000000], bills: [0, 1000000], other: [0, 1000000], months: [1, 24], saved: [0, 100000000], monthly: [0, 1000000] }, (s) => {
  const ess = s.rent + s.food + s.trans + s.bills + s.other;
  const goal = ess * s.months, three = ess * 3;
  $("lead").textContent = `Your ${rm(ess)} of essentials × ${s.months} month${s.months === 1 ? "" : "s"} =`;
  $("big").textContent = rm(goal);
  const pct = goal > 0 ? Math.min(100, (s.saved / goal) * 100) : 100;
  $("have").textContent = `${rm(s.saved)} (${Math.round(pct)}%)`;
  $("left").textContent = rm(Math.max(0, goal - s.saved));
  $("at3").textContent = `${rm(three)}: ${when(s.saved, three, s.monthly)}`;
  $("atGoal").textContent = when(s.saved, goal, s.monthly);
  $("splitA").style.cssText = `width:${pct}%;background:var(--gold-fill)`; $("splitB").style.cssText = `width:${100 - pct}%;background:rgba(255,243,224,.25)`; $("splitC").style.width = "0";
  if (goal > 0 && s.monthly > 0 && s.saved < goal) {
    const n = Math.ceil((goal - s.saved) / s.monthly);
    const vals = [...Array(n + 1)].map((_, m) => Math.min(goal, s.saved + s.monthly * m));
    RIM.chart($("chart"), n, [{ kind: "area-v", key: "f", values: vals }], "f", "MO");
  } else {
    $("chart").innerHTML = "";
  }
  window.__copy = `My emergency fund goal: ${rm(goal)} (${s.months} months of ${rm(ess)}). Saving ${rm(s.monthly)} a month, I get there ${when(s.saved, goal, s.monthly)}. (Ringgit in Motion emergency fund calculator)`;
});
$("copy").addEventListener("click", () => RIM.copy(window.__copy));
"""
page("emergency.html", "Emergency Fund Calculator · Ringgit in Motion", "How big your emergency fund should be (3 to 6 months of essentials) and when you will reach it.", ef_body, ef_js)

# ---------------------------------------------------------------- raise
raise_body = mast("Raise calculator · comment MORE", "got a raise? don’t let it disappear.", "Raise <span>Calculator</span>") + """
<section class="tool" aria-label="Raise calculator">
  <form class="controls" autocomplete="off">
""" + "\n".join([
    field("pay", "Take-home pay before the raise (RM)", 4000, 1000, 20000, 50, 0, 10000000),
    field("raise", "Raise a month, take-home (RM)", 1000, 50, 5000, 50, 0, 10000000, "The extra that actually lands in your account."),
    field("pct", "Share of the raise you save (%)", 50, 0, 100, 5, 0, 100, "Half is a good rule: you still enjoy the other half."),
    '    <div class="divider"></div>',
    field("rate", "Yearly return (%)", 6, 0, 12, 0.1, 0, 20, "An assumption. Real returns go up and down."),
    field("years", "Years", 10, 1, 40, 1, 1, 60),
]) + """
  </form>
  <div class="stack">
""" + card("Save RM500 a month of your raise for 10 years at 6%, and it grows to", "RM81,940", [
    ("New take-home pay", "newpay", False), ("Extra to enjoy each month", "enjoy", False),
    ("Extra to save each month", "keep", True), ("You put in", "paid", False), ("Growth on top", "growth", True)],
    '<span><b style="background: var(--brand-ink)"></b>You put in</span><span><b style="background: var(--gold-fill)"></b>Growth</span>') + """
    <figure><svg class="chart" id="chart" viewBox="0 0 640 280" role="img" aria-label="Growth of the saved part of the raise"></svg>
      <figcaption>The lilac area is the part of your raise you saved. The gold above it is growth.</figcaption></figure>
  </div>
</section>
<section class="mid" aria-label="Compare">
  <h2>Three ways to use the same raise</h2>
  <p class="out" id="cmpOut"></p>
</section>"""
raise_js = r"""
const { $, rm, fv } = RIM;
RIM.form("rim-raise", { pay: 4000, raise: 1000, pct: 50, rate: 6, years: 10 },
  { pay: [0, 10000000], raise: [0, 10000000], pct: [0, 100], rate: [0, 20], years: [1, 60] }, (s) => {
  const keep = (s.raise * s.pct) / 100, enjoy = s.raise - keep, n = s.years * 12;
  const total = fv(keep, s.rate, n), paid = keep * n;
  $("lead").textContent = `Save ${rm(keep)} a month of your raise for ${s.years} year${s.years === 1 ? "" : "s"} at ${s.rate}%, and it grows to`;
  $("big").textContent = rm(total);
  $("newpay").textContent = rm(s.pay + s.raise);
  $("enjoy").textContent = rm(enjoy);
  $("keep").textContent = rm(keep);
  $("paid").textContent = rm(paid);
  $("growth").textContent = rm(Math.max(0, total - paid));
  const pp = total > 0 ? (paid / total) * 100 : 100;
  $("splitA").style.cssText = `width:${pp}%;background:var(--brand-ink)`; $("splitB").style.cssText = `width:${100 - pp}%;background:var(--gold-fill)`; $("splitC").style.width = "0";
  const yrs = [...Array(s.years + 1)].map((_, y) => y);
  const v = yrs.map((y) => fv(keep, s.rate, 12 * y)), p = yrs.map((y) => keep * 12 * y);
  RIM.chart($("chart"), s.years, [{ kind: "area-v", key: "v", values: v }, { kind: "area-p", values: p }, { kind: "line-v", key: "v", values: v }], "v");
  $("cmpOut").innerHTML =
    `Spend all of it (lifestyle creep): <strong>RM0</strong> extra saved. ` +
    `Save half: <strong>${rm(fv(s.raise / 2, s.rate, n))}</strong>. ` +
    `Save all of it: <strong>${rm(fv(s.raise, s.rate, n))}</strong>, in ${s.years} years.`;
  window.__copy = `Saving ${rm(keep)} a month of my ${rm(s.raise)} raise grows to about ${rm(total)} in ${s.years} years at ${s.rate}%. (Ringgit in Motion raise calculator, illustration only)`;
});
$("copy").addEventListener("click", () => RIM.copy(window.__copy));
"""
page("raise.html", "Raise Calculator · Ringgit in Motion", "Got a raise? See what saving part of it grows into, before lifestyle creep spends it.", raise_body, raise_js)

# ---------------------------------------------------------------- epf
epf_body = mast("EPF calculator · comment BONUS", "that EPF cut on your payslip? it’s a pay rise.", "EPF <span>Calculator</span>") + """
<section class="tool" aria-label="EPF calculator">
  <form class="controls" autocomplete="off">
""" + "\n".join([
    field("pay", "Monthly salary (RM)", 3000, 1500, 20000, 50, 0, 10000000),
    field("you", "Your share (%)", 11, 0, 20, 0.5, 0, 50, "Most employees under 60 pay 11%."),
    field("boss", "Employer’s share (%)", 13, 0, 20, 0.5, 0, 50, "13% if your pay is RM5,000 or less, 12% above that."),
    field("bal", "EPF balance today (RM)", 0, 0, 500000, 1000, 0, 100000000),
    '    <div class="divider"></div>',
    field("rate", "Yearly dividend (%)", 5.5, 0, 10, 0.05, 0, 20, "An assumption. EPF paid 5.2% to 6.9% a year over the last 10 years (6.15% for 2025)."),
    field("years", "Years", 30, 1, 45, 1, 1, 60),
]) + """
  </form>
  <div class="stack">
""" + card("RM720 a month into EPF for 30 years at 5.5% grows to", "RM641,466", [
    ("You put in a month", "youM", False), ("Your employer adds", "bossM", True),
    ("Akaun Persaraan (75%, locked till 55)", "a1", False), ("Akaun Sejahtera (15%)", "a2", False), ("Akaun Fleksibel (10%)", "a3", False),
    ("You put in, in total", "youT", False), ("Employer put in, in total", "bossT", True), ("Dividends on top", "div", True)],
    '<span><b style="background: var(--brand-ink)"></b>You</span><span><b style="background: rgba(255,243,224,.55)"></b>Employer</span><span><b style="background: var(--gold-fill)"></b>Dividends</span>') + """
    <figure><svg class="chart" id="chart" viewBox="0 0 640 280" role="img" aria-label="EPF balance over the years"></svg>
      <figcaption>The lilac area is what you and your employer paid in (plus today’s balance). The gold above it is dividends.</figcaption></figure>
  </div>
</section>
<section class="mid" aria-label="Akaun Fleksibel">
  <h2>Leave Akaun Fleksibel alone?</h2>
  <p class="out" id="cmpOut"></p>
  <p class="fine">Since May 2024, new contributions split 75% / 15% / 10% into Akaun Persaraan, Sejahtera and Fleksibel, and all three earn the same dividend. Dividends are compounded here as a steady yearly rate; real EPF dividends change every year. Education only, not financial advice.</p>
</section>"""
epf_js = r"""
const { $, rm } = RIM;
// EPF credits a yearly dividend, so use the monthly rate that compounds to exactly that yearly rate
const fvEff = (m, b0, pct, n) => {
  const r = Math.pow(1 + pct / 100, 1 / 12) - 1;
  const g = Math.pow(1 + r, n);
  return b0 * g + (r === 0 ? m * n : (m * (g - 1)) / r);
};
RIM.form("rim-epf", { pay: 3000, you: 11, boss: 13, bal: 0, rate: 5.5, years: 30 },
  { pay: [0, 10000000], you: [0, 50], boss: [0, 50], bal: [0, 100000000], rate: [0, 20], years: [1, 60] }, (s) => {
  const youM = (s.pay * s.you) / 100, bossM = (s.pay * s.boss) / 100, m = youM + bossM, n = s.years * 12;
  const total = fvEff(m, s.bal, s.rate, n);
  const youT = youM * n, bossT = bossM * n, div = Math.max(0, total - youT - bossT - s.bal);
  $("lead").textContent = `${rm(m)} a month into EPF for ${s.years} year${s.years === 1 ? "" : "s"} at ${s.rate}% grows to`;
  $("big").textContent = rm(total);
  $("youM").textContent = rm(youM); $("bossM").textContent = rm(bossM);
  $("a1").textContent = rm(m * 0.75) + " a month"; $("a2").textContent = rm(m * 0.15) + " a month"; $("a3").textContent = rm(m * 0.1) + " a month";
  $("youT").textContent = rm(youT); $("bossT").textContent = rm(bossT); $("div").textContent = rm(div);
  const pct = (v) => (total > 0 ? (v / total) * 100 : 0);
  $("splitA").style.cssText = `width:${pct(youT + s.bal)}%;background:var(--brand-ink)`;
  $("splitB").style.cssText = `width:${pct(bossT)}%;background:rgba(255,243,224,.55)`;
  $("splitC").style.cssText = `width:${pct(div)}%;background:var(--gold-fill)`;
  const yrs = [...Array(s.years + 1)].map((_, y) => y);
  const v = yrs.map((y) => fvEff(m, s.bal, s.rate, 12 * y)), p = yrs.map((y) => s.bal + m * 12 * y);
  RIM.chart($("chart"), s.years, [{ kind: "area-v", key: "v", values: v }, { kind: "area-p", values: p }, { kind: "line-v", key: "v", values: v }], "v");
  $("cmpOut").innerHTML =
    `Your Akaun Fleksibel gets <strong>${rm(m * 0.1)}</strong> a month. Leave it for ${s.years} years and it grows to ` +
    `<strong>${rm(fvEff(m * 0.1, 0, s.rate, n))}</strong>. Withdraw it every month and that part of your retirement is <strong>RM0</strong>.`;
  window.__copy = `${rm(m)} a month into my EPF (${rm(bossM)} of it from my employer) could grow to about ${rm(total)} in ${s.years} years at ${s.rate}%. (Ringgit in Motion EPF calculator, illustration only)`;
});
$("copy").addEventListener("click", () => RIM.copy(window.__copy));
"""
page("epf.html", "EPF Calculator · Ringgit in Motion", "What you and your employer put into EPF (KWSP) each month, how it splits into 3 accounts, and what it could grow to.", epf_body, epf_js)

# ---------------------------------------------------------------- park your cash
park_body = mast("Park your cash · comment POCKET", "savings, FD or ASB: does it matter where cash sits?", "Park your <span>Cash</span>") + """
<section class="tool" aria-label="Park your cash calculator">
  <form class="controls" autocomplete="off">
""" + "\n".join([
    field("amt", "Amount (RM)", 20000, 1000, 300000, 500, 0, 100000000),
    field("months", "Months you leave it", 12, 1, 12, 1, 1, 12, "Fixed deposit here is a 12-month one. Take it out before 12 months and many banks pay no interest."),
    '    <div class="divider"></div>',
    field("sav", "Savings account (% a year)", 0.25, 0, 4, 0.05, 0, 20, "Basic savings at the big banks pay about 0.15% to 0.25%."),
    field("fd", "12-month fixed deposit (% a year)", 1.9, 0, 5, 0.05, 0, 20, "Board rate at Maybank, CIMB and RHB: 1.90% (ABM, 15 Aug 2026). Promotions pay more, with a minimum and an end date."),
    field("asb", "ASB or ASM payout (% a year)", 5.75, 0, 8, 0.05, 0, 20, "ASB paid 5.75 sen per RM1 unit for 2025. ASM paid 5.00 sen, ASM 3 4.75 sen. Not fixed, not guaranteed."),
]) + """
  </form>
  <div class="stack">
""" + card("RM20,000 for 12 months earns, at best,", "RM1,150", [
    ("Savings account", "eS", False), ("12-month fixed deposit", "eF", False), ("ASB / ASM (if the payout holds)", "eA", True),
    ("Extra vs the savings account", "gap", True), ("Protected by PIDM?", "pidm", False)],
    '<span><b style="background: rgba(255,243,224,.55)"></b>Savings</span><span><b style="background: var(--brand-ink)"></b>Fixed deposit</span><span><b style="background: var(--gold-fill)"></b>ASB / ASM</span>') + """
  </div>
</section>
<section class="mid" aria-label="ASB lowest balance">
  <h2>The ASB lowest-balance catch</h2>
  <p>ASB and ASM pay on your <em>lowest</em> balance in each month. Take money out for even one day and that month only counts what was left.</p>
  <form class="controls" autocomplete="off">
""" + field("dip", "Taken out for a day (RM)", 5000, 0, 50000, 500, 0, 100000000) + """
  </form>
  <p class="out" id="dipOut"></p>
  <p class="fine">Illustration only. Savings and fixed deposit interest is shown as simple yearly interest; ASB/ASM is shown as the yearly payout rate on money kept in for whole months. Bank deposits are protected by PIDM up to RM250,000 per depositor per member bank (Islamic and conventional separately). ASB and ASM are unit trusts: not PIDM-protected and not guaranteed. ASB is mainly for Bumiputera; ASM funds are open to all Malaysians when units are available. Rates change. Education only, not financial advice.</p>
</section>"""
park_js = r"""
const { $, rm } = RIM;
let rate = 5.75;
RIM.form("rim-park", { amt: 20000, months: 12, sav: 0.25, fd: 1.9, asb: 5.75 },
  { amt: [0, 100000000], months: [1, 12], sav: [0, 20], fd: [0, 20], asb: [0, 20] }, (s) => {
  const part = s.months / 12;
  const eS = s.amt * (s.sav / 100) * part;
  const eF = s.months >= 12 ? s.amt * (s.fd / 100) : 0;
  const eA = s.amt * (s.asb / 100) * part;
  const best = Math.max(eS, eF, eA);
  rate = s.asb;
  $("lead").textContent = `${rm(s.amt)} for ${s.months} month${s.months === 1 ? "" : "s"} earns, at best,`;
  $("big").textContent = rm(best);
  $("eS").textContent = rm(eS);
  $("eF").textContent = s.months >= 12 ? rm(eF) : "RM0 (broken early)";
  $("eA").textContent = rm(eA);
  $("gap").textContent = "+" + rm(Math.max(0, best - eS));
  $("pidm").textContent = s.amt > 250000 ? "Bank deposits: up to RM250,000 per bank. ASB: no" : "Savings and FD: yes. ASB: no";
  const tot = eS + eF + eA;
  const pct = (v) => (tot > 0 ? (v / tot) * 100 : 0);
  $("splitA").style.cssText = `width:${pct(eS)}%;background:rgba(255,243,224,.55)`;
  $("splitB").style.cssText = `width:${pct(eF)}%;background:var(--brand-ink)`;
  $("splitC").style.cssText = `width:${pct(eA)}%;background:var(--gold-fill)`;
  window.__copy = `${rm(s.amt)} for ${s.months} months: savings ${rm(eS)}, fixed deposit ${s.months >= 12 ? rm(eF) : "RM0 (broken early)"}, ASB/ASM about ${rm(eA)} if the payout holds. (Ringgit in Motion park-your-cash calculator, illustration only)`;
  dipRender();
});
function dipRender() {
  const d = parseFloat($("dip").value) || 0;
  $("dipOut").innerHTML = `Take out <strong>${rm(d)}</strong> for one day and that month earns on ${rm(d)} less: about <strong>${rm((d * rate) / 100 / 12)}</strong> gone at ${rate}% a year. Money you put in mid-month only starts counting the month after.`;
}
const syncDip = (src, dst) => $(src).addEventListener("input", () => { $(dst).value = $(src).value; dipRender(); });
syncDip("dip", "dipR"); syncDip("dipR", "dip");
dipRender();
$("copy").addEventListener("click", () => RIM.copy(window.__copy));
"""
page("park.html", "Park Your Cash Calculator · Ringgit in Motion", "Savings account vs fixed deposit vs ASB in Malaysia: what the same money earns in each, PIDM cover, and the catches.", park_body, park_js)

# ---------------------------------------------------------------- buy now, pay later
bnpl_body = mast("BNPL calculator · comment TOTAL", "split in 3, every buy feels small. then they stack.", "BNPL <span>Total</span>") + """
<section class="tool" aria-label="Buy now pay later calculator">
  <form class="controls" autocomplete="off">
""" + "\n".join([
    field("pay", "Take-home pay a month (RM)", 3500, 1000, 20000, 50, 0, 10000000),
    '    <div class="divider"></div>',
    field("p1", "Plan 1: monthly instalment (RM)", 120, 0, 1000, 10, 0, 1000000, "Example: RM360 sneakers in 3."),
    field("p2", "Plan 2: monthly instalment (RM)", 150, 0, 1000, 10, 0, 1000000, "Example: RM450 earbuds in 3."),
    field("p3", "Plan 3: monthly instalment (RM)", 150, 0, 1000, 10, 0, 1000000, "Example: RM900 flight in 6."),
    field("p4", "Plan 4: monthly instalment (RM)", 80, 0, 1000, 10, 0, 1000000, "Example: RM240 groceries in 3."),
]) + """
  </form>
  <div class="stack">
""" + card("Your BNPL plans take, every month,", "RM500", [
    ("Share of your take-home pay", "share", True), ("10% guide (our rule of thumb)", "guide", False),
    ("Over or under the guide", "gap", True), ("Pay left after the plans", "left", False)],
    '<span><b style="background: var(--gold-fill)"></b>BNPL plans</span><span><b style="background: rgba(255,243,224,.55)"></b>Rest of your pay</span>') + """
  </div>
</section>
<section class="mid" aria-label="Fee check">
  <h2>Is your plan really 0%?</h2>
  <p>Some plans add a monthly fee on the full price. See what it adds up to, and what it means as a yearly loan rate.</p>
  <form class="controls" autocomplete="off">
""" + "\n".join([
    field("price", "Price (RM)", 1200, 50, 10000, 50, 0, 100000000),
    field("months", "Months", 6, 1, 24, 1, 1, 60),
    field("fee", "Fee (% a month, on the full price)", 1.5, 0, 5, 0.05, 0, 20, "Check the fee table shown at checkout. 0 for a true 0% plan."),
]) + """
  </form>
  <p class="out" id="feeOut"></p>
  <p class="fine">Illustration only: the plans and fee are examples, not any provider's actual rates. The yearly rate is the loan rate (APR) that gives the same payments. Late charges are not included. Since 1 March 2026, BNPL providers in Malaysia fall under the Consumer Credit Act 2025 and the Consumer Credit Commission. Education only, not financial advice.</p>
</section>"""
bnpl_js = r"""
const { $, rm } = RIM;
RIM.form("rim-bnpl", { pay: 3500, p1: 120, p2: 150, p3: 150, p4: 80 },
  { pay: [0, 10000000], p1: [0, 1000000], p2: [0, 1000000], p3: [0, 1000000], p4: [0, 1000000] }, (s) => {
  const tot = s.p1 + s.p2 + s.p3 + s.p4;
  const share = s.pay > 0 ? (tot / s.pay) * 100 : 0;
  const guide = s.pay * 0.1;
  $("big").textContent = rm(tot);
  $("share").textContent = share.toFixed(1) + "%";
  $("guide").textContent = rm(guide) + " a month";
  $("gap").textContent = tot > guide ? rm(tot - guide) + " over" : rm(guide - tot) + " under";
  $("left").textContent = rm(Math.max(0, s.pay - tot));
  const pa = Math.min(100, share);
  $("splitA").style.cssText = `width:${pa}%;background:var(--gold-fill)`;
  $("splitB").style.cssText = `width:${100 - pa}%;background:rgba(255,243,224,.55)`;
  $("splitC").style.cssText = "width:0";
  window.__copy = `My BNPL plans take ${rm(tot)} a month: ${share.toFixed(1)}% of my take-home pay. (Ringgit in Motion BNPL calculator)`;
});
// monthly rate r where the payments are worth exactly the price today (bisection)
function apr(price, pay, n) {
  if (pay * n <= price + 1e-9) return 0;
  let lo = 0, hi = 1;
  for (let i = 0; i < 100; i++) {
    const r = (lo + hi) / 2;
    const pv = (pay * (1 - Math.pow(1 + r, -n))) / r;
    if (pv > price) lo = r; else hi = r;
  }
  return ((lo + hi) / 2) * 12 * 100;
}
function feeRender() {
  const price = parseFloat($("price").value) || 0, n = Math.max(1, Math.round(parseFloat($("months").value) || 1)), f = parseFloat($("fee").value) || 0;
  const pay = price / n + (price * f) / 100;
  const total = pay * n, extra = total - price, y = apr(price, pay, n);
  $("feeOut").innerHTML = `${n} payments of <strong>${rm(pay)}</strong> = <strong>${rm(total)}</strong> in total: <strong>${rm(extra)}</strong> more than paying in full. ` +
    (extra > 0 ? `As a loan, that is about <strong>${y.toFixed(0)}% a year</strong>.` : `A true 0% plan, as long as every payment is on time.`);
}
["price", "months", "fee"].forEach((id) => {
  const sync = (src, dst) => $(src).addEventListener("input", () => { $(dst).value = $(src).value; feeRender(); });
  sync(id, id + "R"); sync(id + "R", id);
});
feeRender();
$("copy").addEventListener("click", () => RIM.copy(window.__copy));
"""
page("bnpl.html", "BNPL Calculator · Ringgit in Motion", "Buy now, pay later in Malaysia: add up your plans, see the share of your pay, and what a monthly fee costs as a yearly rate.", bnpl_body, bnpl_js)
