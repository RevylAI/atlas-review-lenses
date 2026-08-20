---
name: atlas-review-lenses
description: Run a design, usability, accessibility, or pricing-clarity review pass over a mobile app's real screens and leave grounded comments pinned to exact pixels. Use when asked to review an app's UI, audit screens for design or accessibility problems, do a design review, check contrast, find UI bugs in an app, or leave feedback on app screenshots. Works through the Revyl CLI against an app's Atlas.
---

# Atlas review lenses

One review pass looks at real screenshots of an app and leaves each finding as
a comment pinned to the exact pixel it is about. A lens is the instruction set
that decides what you are looking for. Running one lens at a time is the whole
point: four narrow passes find four different classes of bug, while one broad
pass finds a shallow mix.

## Before you start

Requires the Revyl CLI, authenticated, and an app with a populated Atlas.

```bash
revyl atlas apps
```

If the app has no screens yet, populate it first with `revyl explore run <app>`.

## Workflow

**1. Pick exactly one lens.** Read its file in `lenses/` and hold to it. If the
user did not name one, ask. Do not run all four in a single pass.

- `lenses/design.md` for visual correctness of what is rendered
- `lenses/usability.md` for whether the screen tells the truth about state
- `lenses/accessibility.md` for measurable barriers, computed not estimated
- `lenses/pricing-clarity.md` for what the user is about to pay and with what

**2. Pull the screens and actually open them.**

```bash
SHOTS=$(mktemp -d)
revyl atlas graph --app "$APP" --json --limit 200
revyl atlas screen <screen-id> --app "$APP" --screenshots --screenshot-dir "$SHOTS" --json
```

Open every image. A URL or a downloaded path is not a review. If you did not
look at the pixels, you have no finding.

**3. Verify before you claim.** Anything measurable must be measured. Compute
contrast ratios, and sample pixel coordinates before asserting a misalignment.
A suspicion that does not survive measurement is not a finding, it is noise.

**4. Preview any ambiguous target.**

```bash
revyl atlas annotations create --app "$APP" --observation "$OBS" \
  --target "<visible element and location>" \
  --dry-run --preview-out /tmp/pin.png --json
```

Open the preview and confirm the pin landed. A failed grounding creates
nothing, which is the correct outcome: it means the element cannot be seen,
so re-target something visible rather than guessing a coordinate.

**5. Leave the comment.**

```bash
revyl atlas annotations create --app "$APP" --observation "$OBS" \
  --target "<visible element and location>" \
  --body "<what is wrong and what to change>" --json
```

Target what is visible. Occluded text usually cannot be grounded, so pin the
element causing the problem and describe the damage in the body.

**6. Cluster before you report.** Findings that share a root cause are one bug
reported N times. Say so. "Five comments, three root causes" is a more useful
result than five unrelated line items.

## Writing a finding

A good body states the defect, the evidence, and the change. It does not
restate the target, and it does not hedge.

Bad: "This button placement could potentially be improved."
Good: "The Total row is clipped by this button. The scroll container needs
bottom padding equal to the CTA height plus the safe-area inset."

## Managing what you left

```bash
revyl atlas annotations list --app "$APP" --status open --json
revyl atlas annotations reply <thread-id> --app "$APP" --body "<text>"
revyl atlas annotations resolve <thread-id> --app "$APP"
```

Deleting a root comment removes the whole thread everywhere, so prefer
`dismiss` over `delete` when a finding turns out to be wrong.

## Writing your own lens

A lens is four sections: what to look for, what to ignore, how to rank
severity, and how to phrase the target. The ignore list matters as much as the
look-for list, because it is what keeps two lenses from returning the same bug.
Copy any file in `lenses/` and change those four sections.
