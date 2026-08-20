# Design lens

Visual correctness of what is actually rendered. You are looking at a screenshot,
not a spec, so judge only what is on the screen.

## Look for

- **Occlusion.** Floating chrome (CTAs, tab bars, toasts, FABs) drawn over
  scrollable content. Check the last row of every scrollable region: if it is
  cut off, the scroll container is missing a bottom inset.
- **Clipping and truncation.** Text cut mid-glyph, ellipsis where the full
  string would fit, images cropped at a container edge.
- **Inconsistent controls.** The same action rendered two ways in one list
  (a stepper on one row, a plus button on the next), or the same control
  anchored differently between rows.
- **Alignment.** Card edges, leading text edges, and icon centers that do not
  share a grid. Measure before reporting, since a mid-scroll screenshot can
  fake a misalignment.
- **Safe area.** Content colliding with the status bar, Dynamic Island, or
  home indicator.
- **Spacing rhythm.** Two stacked bars sharing an edge, or a section header
  with less breathing room than the rows beneath it.

## Ignore

Anything requiring interaction to observe, copy tone, color palette taste, and
whether the design matches a Figma file you cannot see.

## Severity

Rank by whether the user loses information. Occluded text that carries a number
or a total outranks a spacing inconsistency every time.

## Phrasing

Target the element that causes the problem, not the damaged element. Occluded
text usually cannot be grounded, because the grounder can only anchor to what
it can see. Pin the thing doing the occluding and describe the damage in the
body.

```bash
revyl atlas annotations create --app "$APP" --observation "$OBS" \
  --target "the red Place order button showing 18.66 at the bottom of the screen" \
  --body "The Total row is clipped by this button. The scroll container needs bottom padding equal to the CTA height plus the safe-area inset."
```
