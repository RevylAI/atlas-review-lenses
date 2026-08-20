# Accessibility lens

Measurable barriers visible in a static screenshot. This lens produces numbers,
so do not estimate any value you can compute.

## Look for

- **Text contrast.** Sample the actual pixels and compute the WCAG ratio. The
  AA floor is 4.5:1 for normal text and 3:1 for large text (18pt regular or
  14pt bold and above). Secondary and helper text is where this fails.
- **Non-text contrast.** Icons, input borders, focus rings, and the filled
  state of a control need 3:1 against their background.
- **Tap targets.** 44x44pt on iOS, 48x48dp on Android. Icon-only buttons in
  headers and trailing accessory buttons in list rows are the usual offenders.
- **Color as the only signal.** A state distinguished purely by hue, with no
  shape, icon, label, or weight difference.
- **Text that is an image.** Rasterized copy will not scale with Dynamic Type.
- **Truncation at default size.** If it is tight at the default text size, it
  is broken at accessibility sizes.

## Ignore

Anything needing VoiceOver, focus order, or runtime state. A screenshot cannot
tell you a label is missing, only that a control has no visible text.

## How to measure contrast

Use the bundled helper, which samples the glyph core rather than its edge:

```bash
python3 scripts/contrast.py screen.png --box 50,648,200,668
python3 scripts/contrast.py screen.png --box 50,648,200,668 --large
```

It prints the sampled colors, the ratio, AA and AAA verdicts, and flags a
reading within 0.3 of the threshold as borderline.

The formula, if you would rather inline it. Sample the darkest pixel of the glyph body and the flat background near it,
then compute the WCAG ratio. Antialiasing softens edges, so read the glyph
core rather than its boundary, and report a borderline result as borderline.

```python
def _lin(v):
    v = v / 255
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4

def luminance(c):
    r, g, b = c[:3]
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)

def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)
```

## Severity

Rank by what the barrier hides. A contrast failure on a price or a total
outranks the same failure on a marketing caption.

## Phrasing

Lead with the measured number and the threshold it missed.

```bash
revyl atlas annotations create --app "$APP" --observation "$OBS" \
  --target "the gray Subtotal label on the left side of the price summary" \
  --body "Contrast failure. These labels measure about 4.3:1 against white, under the 4.5:1 WCAG AA floor for normal text. The values on the right are near-black and pass."
```
