# To Do — Bottom-Line Impact Calculator

## Done
- [x] Initial push of `index.html` (+ `README.md`) to https://github.com/jgarizona/Bottom_Line_CO_Impact — landed as commit `66b805e`. The content is artifact Version 19, verified against the v14–v19 changelog markers and by reproducing v18's breakeven figures (1.5mo / 3.8mo / 8.6mo).
- [x] Decided on GitHub Pages, and it is live: **https://jgarizona.github.io/Bottom_Line_CO_Impact/**
      Source is set to **GitHub Actions**; `.github/workflows/pages.yml` redeploys on every push, so no manual step to republish.
- [x] Process note confirmed in practice: a session's GitHub push access is fixed at session start from the repo picker. This session had `jgarizona/Bottom_Line_CO_Impact` selected up front and pushed with no 403.

## Live now
The live site is current as of commit `fb44a42`. It carries the shift-basis ticker
label, the aligned comparison tiles, the derived estimate chart in Model
assumptions, the narrow-phone overflow fixes, the 8-hour work day stated as a
fixed assumption rather than an editable field, and the daily-impact card moved
above the inputs panel so the number reads before the form.

## Open — needs Jeff
- [ ] **Pick a layout and colour** at https://jgarizona.github.io/Bottom_Line_CO_Impact/choose.html
      and send the code (e.g. `2E`); it then becomes the main page.
- [ ] **Decide the impact slider default.** It drives everything and is the single
      biggest lever. At 2.5% with the current defaults Consumer Grade reaches
      $787k over five years; 4% (one unit's proportional share of a 10-unit
      fleet is 10%, so 4% is conservative) roughly doubles it. Concurrency
      settings move it far less.
- [ ] **Delete `claude/hopeful-albattani-owrfne` when work on it is finished.** The
      workflow no longer triggers on it, so it causes no failed runs; it is just
      the working branch. `main` is the default branch and the deploy source.
      Nothing depends on the old branch once its work is merged.
- [ ] Get the boss's review/approval — either the Pages link above or the private artifact link (https://claude.ai/code/artifact/f4601223-ab03-4629-a84f-e49e40d2e555).
- [ ] Confirm the named example platforms in "The Hidden Cost of Hot and Cold" (Apple, Dell Latitude Rugged / Panasonic Toughbook, Honeywell) are okay to name explicitly for this audience, or should be genericized before it goes external.
- [ ] Reconfirm the fixed $4,000 JLT unit price assumption used in "Free Computers… Almost" is still the right number to use.
- [ ] Final copy pass on "Free Computers… Almost" and "The Hidden Cost of Hot and Cold" before external sharing — most wording issues raised so far have been fixed, but this hasn't had a full top-to-bottom proofread pass.

## Note on external exposure
The repo is **public** and Pages is **live**, so the provisional competitor
figures (failure rates, restore times, the hot/cold service-life table) and the
named platforms are now publicly reachable and indexable — ahead of the two
validation items above. Options if that's not wanted yet: flip the repo to
private (Pages on a private repo needs GitHub Pro), genericize the competitor
names, or turn Pages off until the copy pass is done.

## Not part of this project (parked earlier, unrelated)
These were set aside before this project started and haven't been touched since — listed here only so they aren't lost, not because they belong to this calculator:
- PowerShell tool repos inventory project
- VERSO 12 cellular no-service case
- Inside-sales configurator architecture decision
