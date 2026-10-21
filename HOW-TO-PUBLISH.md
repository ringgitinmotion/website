# Ringgit in Motion website: how it's published

The site is hosted free on **GitHub Pages** from the repository `ringgitinmotion/website`.

Live address: **https://ringgitinmotion.github.io/website/**

| Page | Comment keyword | Link |
| --- | --- | --- |
| Home (all calculators) | — | https://ringgitinmotion.github.io/website/ |
| Kopi calculator | KOPI | https://ringgitinmotion.github.io/website/kopi.html |
| 50/30/20 budget | JOM | https://ringgitinmotion.github.io/website/budget.html |
| Compound calculator | GROW | https://ringgitinmotion.github.io/website/compound.html |
| Real return (inflation) | MONEY | https://ringgitinmotion.github.io/website/real-return.html |
| Debt payoff | LOAN | https://ringgitinmotion.github.io/website/debt.html |
| Emergency fund | COVER | https://ringgitinmotion.github.io/website/emergency.html |

## One-time setup (already done once Pages is switched on)

Repository → **Settings → Pages** → Source: **Deploy from a branch** → Branch: **main**, folder **/ (root)** → Save.

## Updating the site

1. Change text or numbers in `_build.py` (or `style.css` / `calc.js`).
2. Run `python _build.py` in this folder to regenerate the pages.
3. Commit and push:
   ```
   git add -A
   git commit -m "Describe the change"
   git push
   ```
4. GitHub Pages republishes within a minute or two.
