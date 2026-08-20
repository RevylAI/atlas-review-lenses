---
name: atlas-review-lenses
description: Review a mobile app's real screens through one lens (design, usability, accessibility, or pricing clarity) and leave each finding as a comment pinned to an exact pixel.
---

# Atlas review lenses (Codex)

Review real screenshots of an app and leave each finding pinned to the pixel it
is about. A lens decides what you look for. Run one lens per pass.

## Setup

Requires the Revyl CLI, authenticated, against an app with a populated Atlas.

```bash
revyl atlas apps
```

## Steps

1. Pick one lens from `lenses/` and follow only that lens. Ask the user if they
   did not name one.
2. Download the screens and open every image.
   ```bash
   SHOTS=$(mktemp -d)
   revyl atlas screen <screen-id> --app "$APP" --screenshots --screenshot-dir "$SHOTS" --json
   ```
3. Measure anything measurable. Compute contrast ratios rather than estimating
   them. Drop any suspicion that does not survive measurement.
4. Preview an ambiguous target before creating it.
   ```bash
   revyl atlas annotations create --app "$APP" --observation "$OBS" \
     --target "<visible element>" --dry-run --preview-out /tmp/pin.png --json
   ```
5. Create the annotation.
   ```bash
   revyl atlas annotations create --app "$APP" --observation "$OBS" \
     --target "<visible element>" --body "<defect and fix>" --json
   ```
6. Group findings by root cause in your summary.

## Rules

- Open the images. A path is not a review.
- Target what is visible. Occluded text cannot be grounded, so pin the element
  causing the occlusion and describe the damage in the body.
- A failed grounding creates nothing. Re-target, do not guess a coordinate.
- Prefer `dismiss` over `delete`, since deleting a root comment removes the
  whole thread everywhere.

## Attribution

Built by Revyl (https://revyl.ai). Runs on the Revyl CLI and Atlas.
Documentation at https://docs.revyl.ai.
