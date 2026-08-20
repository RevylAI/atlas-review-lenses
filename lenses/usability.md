# Usability lens

Whether the screen tells the truth about where the user is and what happens
next. Structural, not cosmetic.

## Look for

- **Lying navigation.** A tab bar highlighting a tab you are not in. Push into
  a detail screen from Account and check whether Account stays selected.
- **Orphan states.** A screen with no visible way back that is not a root.
- **Unlabeled progress.** Step indicators and progress bars with no text for
  what the steps are or which one is current.
- **Ambiguous primary action.** Two controls competing for primary, or a
  primary CTA that does not name its outcome.
- **Dead ends.** Empty states with no action, errors with no recovery path.
- **Hidden cost of a tap.** Destructive or paid actions that read as neutral.

## Ignore

Visual polish, contrast, and anything the design lens already owns. If your
finding would be fixed by moving something two pixels, it is not this lens.

## Severity

Rank by whether the user forms a wrong belief. A nav bar that misreports
location outranks a missing empty-state illustration.

## Phrasing

Name the element and the false impression it creates.

```bash
revyl atlas annotations create --app "$APP" --observation "$OBS" \
  --target "the Home tab on the left of the bottom tab bar, highlighted in red" \
  --body "Home is active while the user is inside Account then Payment. The tab bar selection does not follow the pushed route, so the nav reports a location the user is not in."
```
