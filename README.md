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
| **Inputs** | Annual warehouse output, working days/year, fleet size, and the business-impact % of one unit being down (slider plus 1% / 2.5% / 5% presets). |
| **Daily impact** | The headline number: what one day of one computer being down costs. Optionally shows the two-units-down case. |
| **Live ticker** | Paces the daily impact out in real time, second by second, while a unit sits unavailable. Pause / reset / fast-forward (1 hr per 10 sec). |
| **5-year comparison** | Four platform tiers — Consumer Grade, Semi-Rugged, Rugged, JLT Rugged — each priced by its own failure rate and restore time, with the delta against JLT. |
| **Free Computers… Almost** | Per tier, how long its downtime losses take to add up to the $4,000 price of one JLT unit. |
| **The Hidden Cost of Hot and Cold** | Service-life estimates per tier at normal, ~120°F, and ~−22°F ambient. |
| **Model assumptions** | The failure rates and restore times driving the comparison, editable inline, plus working hours/day for the ticker. |

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

Two-units-down is modeled as `impactPct + (2 × impactPct)` — the second concurrent failure is assumed
to hurt twice as much as the first, since there's less slack left to absorb it. That 2× is an
illustrative estimate, not a measured figure.

The model deliberately has no spare-swap shortcut: every failure is assumed to run the full restore
time. Where a customer keeps hot spares, lower the restore time to match.

### Defaults

| Input | Default |
| --- | --- |
| Annual warehouse output | $10,000,000 |
| Working days per year | 250 |
| Fleet size | 10 units |
| Impact of one unit down | 2.5% |
| Working hours per day | 8 |

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
index.html    the entire tool — markup, styles, and logic in one file
README.md     this file
```

Keeping it to one file is intentional: it can be emailed, dropped on a shared drive, or opened from a
USB stick in a warehouse with no network.
