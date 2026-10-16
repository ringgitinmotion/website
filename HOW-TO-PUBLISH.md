# Put the Ringgit in Motion calculators online (free)

This folder is a complete website. Anyone can use it: no Claude account, no login, nothing to install.

| Page | Keyword it answers | File |
| --- | --- | --- |
| Home (all calculators) | — | `index.html` |
| Kopi calculator | KOPI | `kopi.html` |
| 50/30/20 budget | JOM | `budget.html` |
| Compound calculator | GROW | `compound.html` |
| Real return (inflation) | MONEY | `real-return.html` |

## Easiest: Netlify Drop (about 2 minutes)

1. Go to **app.netlify.com/drop** and sign up for a free account (Google sign-in works).
2. Drag this whole `website` folder onto the page.
3. Netlify gives you an address like `random-name-123.netlify.app`. Open it to check.
4. Rename it: **Site configuration → Change site name** → `ringgitinmotion`.
   Your site is now **https://ringgitinmotion.netlify.app** (if the name is free).

Links to send for each keyword (Netlify also serves them without `.html`):

- KOPI → `https://ringgitinmotion.netlify.app/kopi`
- JOM → `https://ringgitinmotion.netlify.app/budget`
- GROW → `https://ringgitinmotion.netlify.app/compound`
- MONEY → `https://ringgitinmotion.netlify.app/real-return`

Put the home page link in your Instagram bio, so every post points to one place.

## To update later

Change the numbers or text in `_build.py`, run `python _build.py` in this folder, then on Netlify go to
**Deploys** and drag the folder in again. The address stays the same.

## Other free hosts

- **Cloudflare Pages** (pages.cloudflare.com): "Upload assets", drag the folder.
- **GitHub Pages**: create a repository, upload the files, turn on Pages in Settings.

`_build.py` and this guide are harmless if uploaded, but they don't need to be.
