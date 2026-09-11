# Bottom-Line Impact Calculator

An interactive, single-file web tool for JLT Mobile Computers sales conversations. It reframes a
vehicle-mount computer purchase away from unit price and toward what a *failed* computer costs the
warehouse's bottom line over five years.

The core argument the tool makes: when 1 of 10 forklift computers fails, warehouse output doesn't drop
10% — other people and equipment absorb the work. The real hit is closer to 2–3%, but applied to the
warehouse's full daily output, that's still real money, and you pay it for every day the unit is down.

## Running it

Open `index.html` in a browser. That's it — no build step, no dependencies, no server required.

The only external requests are Google Fonts (Archivo, Public Sans, IBM Plex Mono). Offline, the page
still works and falls back to system fonts.

## What's on the page

| Section | What it does |
| --- | --- |
| **Daily impact** | The headline number, and the first thing on the page: what one day of one computer being down costs. Carries the business-impact control that drives it (slider, stepper and 1% / 2.5% / 5% presets, all three views of one value), a mirrored copy of the live ticker, and a conditional block for two or three units down together. |
| **Inputs** | Annual warehouse output, working days/year and fleet size. Sits below the number it produces, under the line "Adjust the number to see what the wrong computers do to your bottom line". |
| **Live ticker** | Paces the daily impact out in real time while a unit sits unavailable, and is mirrored into the hero card so it reads without scrolling. It counts **working** seconds, not calendar seconds — the label states the basis and the per-hour rate, and a full shift of ticking equals one down-day in the comparison below. Pause / reset / fast-forward (1 hr per 10 sec). |
| **5-year comparison** | Four platform tiers — Consumer Grade, Semi-Rugged, Rugged, JLT Rugged — each priced by its own failure rate and restore time, with the delta against JLT. |
| **Free Computers… Almost** | Per tier, how long its downtime losses take to add up to the $4,000 price of one JLT unit. |
| **The Hidden Cost of Hot and Cold** | Service-life estimates per tier at normal, ~120°F, and ~−22°F ambient. |
| **Model assumptions** | The failure rates and restore times driving the comparison, editable inline, and a statement that the tool assumes an 8-hour work day. Clicking any ESTIMATE badge opens a live chart of what those assumptions produce — failures per year, days down per year, cost per year and the five-year figure, unrounded, for all four platforms. It is fed the same results as the comparison tiles, so the two cannot disagree. |

## The model

```
dailyOutput        = annualOutput / workingDays
dailyImpact        = dailyOutput × impactPct

failuresPerYear    = fleetSize × annualFailureRate
exposureDaysPerYear = failuresPerYear × repairDays
annualImpact       = exposureDaysPerYear × dailyImpact
fiveYearImpact     = annualImpact × 5

breakevenYears     = $4,000 / annualImpact        (one JLT unit's price)
```

`annualImpact` above is the flat-schedule form. What the code actually computes is the expected daily
loss averaged over how many units are down at once, which reduces exactly to
`exposureDaysPerYear × dailyImpact` when every unit is priced the same.

Concurrent failures use a **marginal schedule**, not a multiplier: one entry per unit down, each set
independently. Ticking "Additional cost with two systems down" reveals a stepper for the second unit,
which inherits the current value so opening it changes nothing until it is moved; ticking again
reveals a third. Each is a percentage of daily output in 0.5 steps with a floor of 1%, and the cost of
*k* units down together is the sum of the first *k* entries — 2.5% + 2.0% + 1.5% is 6.0% for three,
not a rate applied three times.

How much of the year is spent with two or more units down follows from each platform's own failure
rate and restore time (a Poisson exposure, λ = exposure-days ÷ working days), so a platform that fails
often and takes longer to fix spends far more time there. In practice it is a small effect next to the
impact slider. At the default settings, Consumer Grade's five-year figure across the whole range of
schedules runs from $778k (2.5% + 2.0% + 1.5%, which is *below* the flat $787k, because a second unit
priced under the base rate costs less than three at the base rate) to $892k at the maximum 2.5% + 8% +
8% — about 13% at the extreme. The impact slider alone spans **$315k at 1% to $2.5M at 8%**. The
slider is the lever that matters; concurrency is a refinement on top of it.

The model deliberately has no spare-swap shortcut: every failure is assumed to run the full restore
time. Where a customer keeps hot spares, lower the restore time to match.

### Defaults

| Input | Default |
| --- | --- |
| Annual warehouse output | $50,000,000 |
| Working days per year | 250 |
| Fleet size | 10 units |
| Impact of one unit down | 2.5% |
| Working day (ticker pace only) | 8 hours — fixed, stated on the page, not adjustable |

| Tier | Annual failure rate | Restore time |
| --- | --- | --- |
| Consumer Grade | 15% | 21 days |
| Semi-Rugged | 9% | 14 days |
| Rugged | 4% | 14 days |
| JLT Rugged | 2.5% | 10 days |

## Before presenting this externally

**The JLT figures are JLT's own commitments.** 2.5% annual failure rate comes from JLT's internal TCO
model; the 10-day restore time is 7 business days under contract plus ~3 days average shipping.

**The competitor figures are not.** Failure rates, restore times, and the temperature/service-life
table for Consumer Grade, Semi-Rugged, and Rugged are directional estimates for a sales conversation —
provisional placeholders, not published manufacturer specs. Confirm them against the specific
competitor model being quoted before you put them in front of a customer, and don't present them as
verified fact. Every one of those figures is editable inline on the page for exactly that reason.

This is a planning tool for a conversation, not a quote.

## Layout

```
index.html                  the entire tool — markup, styles and logic in one file
choose.html                 reviewer page: pick a layout and colour, preview it live, get a code like 2A
tools/build-variants.py     generates the 5 layout previews from index.html
tools/build-colors.py       generates the 5 colour schemes from index.html
tools/build-combos.py       generates all 25 combinations, and choose.html
variants/                   everything those three scripts produce — generated, never edited by hand
.github/workflows/pages.yml deploys to GitHub Pages on every push to main
README.md HANDOFF.md
CHANGELOG.md TODO.md        this file, plus session handover notes, history and open items
```

**`index.html` is the single source of truth.** Every page under `variants/` is that file plus an
appended override stylesheet, so copy, markup and JavaScript exist in exactly one place. Edit
`index.html`, then run all three generators:

```
python3 tools/build-variants.py && python3 tools/build-colors.py && python3 tools/build-combos.py
```

Keeping the tool itself to one file is intentional: it can be emailed, dropped on a shared drive, or
opened from a USB stick in a warehouse with no network.
