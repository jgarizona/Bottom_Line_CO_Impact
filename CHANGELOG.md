# Changelog — Bottom-Line Impact Calculator

## Earlier work (prior session, versions ~1–12)
- Initial build modeled on a Zerto-style downtime-cost calculator, including repair cost, non-linear workload redistribution (10 forklifts / 1 down ≠ 10% output loss), IT removal/reimaging cost, spare-unit logic, and JLT's 7-day contract / 10-day-with-shipping repair window.
- Rebuilt from scratch against Jeff's authoritative spec (`JLT_Bottom_Line_Calculator_Project.md`): reduced to 5 simple inputs, adopted the exact formula chain, hid granular assumptions behind a "Model assumptions" foldout, added the closing line about comparing what the wrong computer costs.
- Removed the spare-computer Yes/No toggle and simplified downtime handling to always use full contracted/estimated repair time.
- Added SLA vs. estimate distinctions on tile captions (JLT's validated SLA vs. competitors' assumptions).
- Fixed a squished/invisible-text bug in the assumptions table (flexbox shrink issue).
- Set new default input values per Jeff's screenshots.
- Discussed (no code change) whether multiple simultaneous failures should be modeled — concluded the linear/additive model is valid in expectation, exposure is low at typical fleet sizes.
- Added a "show the cost if two systems are down" checkbox with a 2x-impact heuristic for the second unit; moved/restyled the checkbox into the ticker panel per feedback.
- Slowed the fast-forward ticker rate from 3600x to 360x after it "went crazy."
- Replaced the boxy "JLT SLA" badge with a native-tooltip hover style (`.sla-hint`), removed the box from under the failure-rate stat.
- Fixed a table-row misalignment bug (`vertical-align:top` on assumption table cells).

## This session

- **v13** — Added two new collapsible foldouts between the verdict banner and "Model assumptions": **"Free Computers… Almost"** (interactive breakeven-years reveal, editable JLT unit price, 4 clickable platform pills) and **"The Hidden Cost of Hot and Cold"** (static service-life/temperature table). Verified via Playwright screenshots.
- **v14** — Reworded the hero lede from "Your core business is moving product — not repairing computers..." to "The core business of your warehouse is moving product out and to your bottom line..."
- **v15** — Updated the lede's IT sentence to "IT and Maintenance gets pulled off its normal work."
- **v16** — Removed the editable "Estimated JLT unit price" field entirely (now a fixed internal constant, $4,000). Reworded the "Free Computers… Almost" blurb to "Pick a platform to see how long it would take to buy a JLT system," with "JLT system" as a hover tooltip showing the $4,000 assumption.
- **v17** — Special-cased the JLT Rugged pill in "Free Computers… Almost": instead of a breakeven-vs-itself number, it now shows a fixed "2+ years" callout about JLT's 7+ year service life continuing to pay dividends through uptime.
- **v18** — Changed the breakeven math basis: instead of years to buy the *entire JLT fleet* (which pushed the Rugged tier's number to 7.1 years — beyond a typical 5-year ROI window), it now shows how long it takes the platform's downtime losses to equal the price of *one* JLT computer. Values dropped to a much more compelling range (Consumer Grade 1.5 months, Semi-Rugged ~3.8 months, Rugged 8.6 months) and auto-format as months when under a year.
- **v19** — Reworded the awkward closing sentence in the breakeven result line, from "Multiply that across your whole fleet, and that's on top of..." to "Every other unit in your fleet is running up the same tab at the same time, on top of..."
- Diagnosed and resolved GitHub push access: found the Claude GitHub App was authorized but not installed on Jeff's GitHub account; walked through claude.ai/code's "Install on GitHub" flow live in the browser to fix it. Confirmed GitHub has no generic MCP connector — repo push access is a dedicated, session-scoped integration.
- Created this handoff/changelog/todo set so work can continue in a claude.ai/code session bound to the `Bottom_Line_CO_Impact` repo.

## Repo and deployment
- Committed Version 19 to `jgarizona/Bottom_Line_CO_Impact` as `index.html`, with a `README.md` documenting the model math, defaults, and the JLT-SLA-vs-competitor-estimate distinction. Version confirmed by reproducing v18's breakeven figures (1.5mo / 3.8mo / 8.6mo) and checking the v14-v19 copy markers.
- Verified the theming invariant from HANDOFF.md holds: `--banner-bg` / `--banner-fg` / `--banner-border` are declared only in the base `:root` and are not redefined in either dark-mode block.
- Fixed two latent issues found while verifying: the impact hero's static placeholders read $400,000 / $10,000 while the defaults compute $40,000 / $1,000 (a 10x flash before JS ran), and `tickerRatePerSecond()` was dead code reading an undefined `c._hoursPerDayCache`.
- Stood up GitHub Pages. An attempt to enable it from Actions via `actions/configure-pages` with `enablement: true` failed — creating a Pages site needs repo-admin rights that no integration token has ("Resource not accessible by integration") — so Jeff set Source to **GitHub Actions** manually. The workflow then deployed successfully and now republishes on every push.
- Imported HANDOFF.md, CHANGELOG.md, and TODO.md into the repo so the next session finds them alongside the code.
