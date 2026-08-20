# Affordance lens

Whether an element looks like what it does. You are judging the promise the
styling makes, not whether the screen is pretty or correctly laid out.

## Look for

- **Static content styled as a control.** Badges, chips, and pills that borrow
  button geometry. The tell is a non-interactive element sharing a shape,
  icon-plus-label pattern, or row position with real buttons nearby.
- **Controls with no control chrome.** Tappable rows with no chevron, no
  underline, no tint, and no elevation. If the only hint is that a designer
  knows it is tappable, the user does not.
- **Ambiguous selected state.** Segmented controls and toggles where the
  selected option is not obvious without reading both. A gray fill reads as
  disabled to as many people as it reads as selected, so selection needs a
  second signal such as weight, tint, or elevation.
- **Two styles for one action.** The same operation rendered as a stepper on
  one row and a plus button on the next, so the user learns the control twice.
- **Decorative elements that invite a tap.** Illustrations, hero images, and
  stat tiles that look pressable and do nothing.
- **Disabled that reads as enabled.** A dimmed primary button that still looks
  like the next step, with no reason given for why it is unavailable.

## Ignore

Whether the element is in the right place (design lens), whether the label is
readable (accessibility lens), and whether the flow makes sense (usability
lens). This lens asks one question: does the styling predict the behavior.

## How to test it

Cover the labels and look only at shape, fill, border, and elevation. Sort
everything on screen into "looks tappable" and "looks static," then check that
sort against what actually is. Every mismatch is a finding.

## Severity

Rank by the cost of the wrong guess. A static badge that looks tappable costs
one dead tap. A primary action that does not look tappable costs the flow.

## Phrasing

Name the element, then name the neighbor it is being confused with. The
comparison is the whole argument.

```bash
revyl atlas annotations create --app "$APP" --observation "$OBS" \
  --target "the red Free garlic knots over 30 pill below the Store info and ratings buttons" \
  --body "Affordance collision. This is a promotional badge, but it is a rounded pill with a leading icon and a label, sitting directly under Store info and 1,832+ ratings, which are the same shape and are tappable. Give promos a different container, or make the badge open the offer."
```
