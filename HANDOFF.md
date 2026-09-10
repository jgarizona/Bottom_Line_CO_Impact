# Bottom-Line Impact Calculator — Handoff

## What this is
A one-page interactive sales calculator for JLT Mobile Computers. It demonstrates that JLT Rugged computers protect a customer's bottom line better than Consumer Grade, Semi-Rugged, and (competitor) Rugged platforms, using JLT's lower failure rate and faster contracted repair SLA versus industry estimates.

## Where things stand right now
- **Live preview (private artifact):** https://claude.ai/code/artifact/f4601223-ab03-4629-a84f-e49e40d2e555 — currently Version 19.
- **GitHub repo (target):** https://github.com/jgarizona/Bottom_Line_CO_Impact — created by Jeff, empty as of this handoff. A separate claude.ai/code session (bound to this repo, launched by Jeff directly) is in progress pushing the initial `index.html`.
- **Source file used to build every version in this conversation:** `downtime-meter.html` — a single self-contained HTML/CSS/JS file (no external deps except Google Fonts).

## Design source of truth
Built from Jeff's own authoritative spec, `JLT_Bottom_Line_Calculator_Project.md` (uploaded earlier in this conversation, never modified by Claude). It defines: 5 simple customer inputs only, a specific formula chain, hiding granular cost assumptions behind an expandable "Model assumptions" section, avoiding a spreadsheet/chart-heavy look, and closing with: *"Don't compare what the computer costs to buy. Compare what the wrong computer costs your business."*

## Page structure (top to bottom)
1. Topbar — JLT wordmark + "Bottom-Line Impact" tag
2. Hero — headline + lede ("The core business of your warehouse is moving product out and to your bottom line...") + a 2-3% workload-redistribution callout
3. Inputs panel — annual output, working days, fleet size, impact % (slider + chips)
4. Impact hero — daily output / daily bottom-line impact, plus a conditional "two systems down" block
5. Live ticker — play/pause/reset/fast-forward, with a "show the cost if two systems are down" checkbox
6. Platform comparison tiles — Consumer Grade, Semi-Rugged, Rugged, JLT Rugged, each with a spec caption distinguishing JLT's validated SLA data from competitors' estimates
7. Verdict banner
8. Three collapsible `<details>` foldouts, in this order:
   - **"Free Computers… Almost"** — pick a platform, see how long (in months/years) its downtime losses take to equal the price of *one* JLT Rugged computer (~$4,000, fixed constant, not user-editable). JLT's own tile is special-cased to a fixed "2+ years" message about its 7+ year service life paying dividends through uptime, rather than a breakeven number.
   - **"The Hidden Cost of Hot and Cold"** — static table of normal/hot/cold service-life estimates per platform, with "ESTIMATE" tags on competitor rows and "JLT SLA" on JLT's own validated figures.
   - **"Model assumptions (for internal review)"** — the original full inputs/spec table.
9. Footer

## Key formulas (see inline JS comments in the file for exact code)
- `dailyOutput = annualOutput / workingDays`
- `dailyImpact = dailyOutput * (impactPct/100)`
- `failuresPerYear = fleetSize * (failureRate/100)`
- `annualImpact = failuresPerYear * repairDays * dailyImpact`
- `fiveYear = annualImpact * 5`
- Breakeven (non-JLT tiers): `JLT_UNIT_PRICE (4000) / tier.annualImpact`, formatted as months if < 1 year, else years.

## Theming note (don't reintroduce this bug)
CSS uses custom properties for light/dark support. The ticker panel and verdict banner are "always dark" and use fixed `--banner-bg` / `--banner-fg` / `--banner-border` tokens declared ONLY in the base `:root` — never redefine those specific tokens inside the dark-mode blocks, or they'll invert. This bug was introduced and fixed twice already.

## GitHub / push access — what we learned
- The Claude GitHub App was OAuth-**authorized** on Jeff's GitHub account (jgarizona) but never actually **installed** — that mismatch was the root cause of every push getting a 403 from this Cowork session.
- Fixed by going to claude.ai/code → clicking "Install on GitHub" → the app now has access including `jgarizona/Bottom_Line_CO_Impact`.
- Important limitation: a Cowork/Claude Code session's repo push authorization is fixed at **session start**, based on whatever repo(s) were selected in the repository picker. It cannot be granted to an already-running session. Any future session that needs to push to this repo must have it selected up front.
- GitHub does not offer a generic MCP "connector" for GitHub (checked both installed connectors and the full marketplace, even after Jeff enabled connector search) — repo access is handled entirely through the dedicated GitHub App + git proxy described above, not the general connector system.

## Open items
See `TODO.md`.
