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

## Model, defaults and the Right Now panel
- Defaults set to $50,000,000 output / 250 days / **10 units**, matching the hero
  callout's own example ("10 forklifts. 1 computer fails. Output doesn't fall
  10%") so the opening screen and the opening sentence agree. Fleet had briefly
  been 25, which contradicted both the "10 forklifts" line and the 10% figure.
- Annual output is a text field carrying thousands separators (50,000,000), with
  the caret held in place as you type. Every reader strips commas, so the value
  is still a plain number to the maths.
- Relabelled "Number of vehicle computers" to "Units / Vehicles".
- Concurrency reworked twice. First a single 2x multiplier, then replaced by
  per-unit controls: ticking "Additional cost with two systems down" reveals a
  0.5-step stepper (floor 1.0) for that unit, and a checkbox for a third. Three
  is the ceiling. Each revealed control inherits the value above it, so opening
  one changes nothing until it is moved.
- The annual maths generalise rather than change: expected daily loss is the
  schedule averaged over the distribution of concurrent failures implied by each
  platform's failure rate and repair time. A flat schedule reduces exactly to the
  original annualExposureDays x dailyImpact, so the untouched page still computes
  the spec's formula chain.
- Added a note stating how the current schedule compares with that flat baseline
  and which way the totals move, because a step-down schedule lowers the totals
  and looked like a bug.
- Breakeven shows working days under a month ("1.1 working days") instead of
  "0.1 months".
- Right Now copy quotes the live percentages rather than a multiplier.
- The live ticker is mirrored into the impact hero under "Money Leaving Your
  Bottom Line", so it reads without scrolling; both copies show the same value.
- The business-impact control moved into the impact hero beside the number it
  drives, and gained a stepper alongside the slider and chips. All three are
  views of one value.
- Added "Adjust the number to see what the wrong computers do to your bottom
  line" above the inputs.
- The elapsed line now names the basis the money is counted on: "Elapsed
  00:01:59 of an 8-hour shift  $500 per working hour". The ticker always counted
  working seconds (dailyImpact / hoursPerDay x 3600), so a full shift of it
  equals one down-day in the comparison below -- but the clock read like wall
  time, which invited the objection that the whole model was on a 24-hour basis.
  Both halves read from hoursPerDay and the concurrency schedule, and the
  per-hour rate is the sanity check that makes the ticker verifiable in someone's
  head. Past a shift the clock says "one full shift", then "2.4 shifts".
  The two halves are separated by a flex gap, not a printed middot: the line
  wraps to two centred lines below 560px, and a middot would dangle at the start
  of the wrapped line. No breakpoint could fix that, since the text length moves
  with the numbers.
- Working hours per day went from a 0.5-step field to an 8 / 16 / 24 stepper, then
  out of the page entirely. It only ever paced the ticker -- none of the annual or
  five-year figures depend on it, because the shift pattern is already carried by
  annual output, and scaling the loss by hours as well would count throughput
  twice -- so an editable control that changed nothing in the money was pure
  confusion for a demonstration tool. It is now the constant TICKER_HOURS_PER_DAY
  = 8, stated in the foldout as "this is based on an 8-hour work day". The
  article() helper went with it: it existed only to pick "a" or "an" for a
  variable number of hours.

## The derived chart in Model assumptions
- The assumption fields are only interesting as the numbers they produce, so
  clicking any ESTIMATE badge in that foldout opens a chart below Working hours
  per day: failure rate, failures per year, days down per year, cost per year,
  the five-year figure and failures over five years, for all four platforms.
  Unrounded, where the tiles show $787k.
- It is fed the same results array the tiles are fed, so the two cannot disagree,
  and it re-renders from renderAll -- every input above changes it live.
- A live basis line states the inputs it rests on, and a footnote says the failure
  counts are expected values rather than a forecast, and points out that the
  days-down column does as much work as the failure rate.
- With the concurrency schedule open the footnote names it. When the schedule is
  flat it says so and says the totals will not move -- a flat schedule reduces
  exactly to days down x daily cost, so ticking the box otherwise looks broken.
  (An earlier draft of this line claimed the figures "run above" the flat rate,
  which is false: with 2.5% + 2.0% the five-year total falls to $778k.)
- The badges are real buttons with aria-expanded and a +/- marker, so the control
  is findable and keyboard-reachable. Hide returns focus to the badge.
- Below 900px each platform becomes a card with every value labelled. The
  seven-column table needs about 816px, so on a phone it would have scrolled the
  five-year column out of sight -- the one number that has to be seen. Header
  cells wrap now, which is what let the table survive down to 900px at all.
- The JLT SLA badge in the prose carries the same tooltip as the one beside the
  repair-time field.

## Narrow-screen overflow, and the deploy trigger
- `.chip-row` and `.slider-row` now wrap. `display:flex` defaults to `nowrap`, so
  the four platform pills in the breakeven foldout ran off a 360px phone -- the
  last one, JLT Rugged, was unreachable rather than merely clipped -- and the
  impact stepper ran 10px past a 320px viewport. A range input also needs
  `min-width:0`, or it refuses to shrink and pushes the row wide anyway.
  Verified: no horizontal overflow at 1280 / 600 / 414 / 390 / 375 / 360 / 340 /
  320px, with zero, one and two concurrency boxes ticked, foldouts open and shut,
  and no chip off-screen in any of the 25 combinations.
- The Pages workflow triggers on `main` only. The `github-pages` environment's
  deployment branch rule names `main`, so a push to the working branch started a
  run that failed in 2-3 seconds with no steps and no logs -- a red X on the
  commit that had nothing to do with the change. Development still happens on
  `claude/hopeful-albattani-owrfne`; promoting to the live site is a fast-forward
  of `main`.

## Brand and presentation
- Palette taken from jltmobile.com: #fe5002 accent, #0f172a navy, #33333a body,
  #f2f2f2 page, #757575 muted, #f39200 amber. Neutrals moved from warm brown to
  these cool values; corners rounded.
- Fixed invisible ticker buttons: .tbtn used --paper, which flips with the theme,
  inside a panel that is always dark.
- Tokenised the last hardcoded banner colours, and added --banner-scheme so a
  light-panel scheme gets light native stepper arrows (Signal was showing dark
  arrows on orange).
- Five layouts under /variants/, five colour schemes under /variants/colors/,
  and all 25 combinations under /variants/combo/ behind /choose.html, which
  previews a pairing live and names it with a code like 2E.
- Three generators in tools/ derive every one of those pages from index.html, so
  copy, markup and JS have a single source of truth.

