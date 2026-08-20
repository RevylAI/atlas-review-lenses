#!/usr/bin/env python3
"""Compute the WCAG contrast ratio of text in a screenshot region.

Samples the darkest pixel in the region as the glyph color and the most common
pixel as the background, so it reads the glyph core rather than its antialiased
edge.

    python3 scripts/contrast.py shot.png --box 50,648,200,668
    python3 scripts/contrast.py shot.png --box 50,648,200,668 --large
"""
import argparse
from collections import Counter

from PIL import Image

AA_NORMAL, AA_LARGE = 4.5, 3.0
AAA_NORMAL, AAA_LARGE = 7.0, 4.5


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


def sample(path, box):
    x0, y0, x1, y1 = box
    px = Image.open(path).convert("RGB").crop((x0, y0, x1, y1)).getdata()
    pixels = list(px)
    if not pixels:
        raise SystemExit("empty region: check the --box coordinates")
    fg = min(pixels, key=luminance)
    bg = Counter(pixels).most_common(1)[0][0]
    return fg, bg


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("image")
    ap.add_argument("--box", required=True, help="x0,y0,x1,y1 region around the text")
    ap.add_argument(
        "--large",
        action="store_true",
        help="text is 18pt regular or 14pt bold and above",
    )
    args = ap.parse_args()

    box = tuple(int(v) for v in args.box.split(","))
    if len(box) != 4:
        raise SystemExit("--box needs four comma-separated integers")

    fg, bg = sample(args.image, box)
    ratio = contrast(fg, bg)
    aa = AA_LARGE if args.large else AA_NORMAL
    aaa = AAA_LARGE if args.large else AAA_NORMAL

    print(f"foreground #{fg[0]:02x}{fg[1]:02x}{fg[2]:02x}")
    print(f"background #{bg[0]:02x}{bg[1]:02x}{bg[2]:02x}")
    print(f"contrast   {ratio:.2f}:1")
    print(f"AA  ({aa}:1)  {'pass' if ratio >= aa else 'FAIL'}")
    print(f"AAA ({aaa}:1) {'pass' if ratio >= aaa else 'FAIL'}")

    # Antialiasing puts a near-threshold reading on either side of the line.
    if abs(ratio - aa) < 0.3:
        print("\nwithin 0.3 of the AA threshold, report it as borderline")


if __name__ == "__main__":
    main()
