# Beemik brand kit

The mark is a regular octagon (all eight sides equal, flat top) with a capital **B** set in Inter Tight ExtraBold.
The wordmark is "beemik" in lowercase Inter Tight Bold.

## Colors

| Name  | Hex       | Use                                      |
|-------|-----------|------------------------------------------|
| Ink   | `#1d1d1f` | Primary. The mark, headlines, buttons    |
| White | `#ffffff` | Backgrounds, the B on an ink octagon     |
| Gray  | `#6e6e73` | Secondary text                           |
| Panel | `#f5f5f7` | Light section backgrounds                |
| Honey | `#f5a524` | Accent only, sparingly (app icons, merch)|

## What's where

```
logo/
  svg/                 Master vector files. Use these whenever possible.
    beemik-mark-black        ink octagon, white B (default)
    beemik-mark-white        white octagon, ink B (for dark backgrounds)
    beemik-mark-honey        honey octagon, ink B
    beemik-mark-mono-*       one color, B cut out (stamps, embroidery, single-color print)
    beemik-wordmark-*        mark + "beemik", horizontal
    beemik-wordmark-stacked-*  mark above "beemik"
    beemik-appicon-*         full square, no transparency (app stores)
  png/
    mark/              every mark color at 16–1024 px, transparent
    wordmark/          high-res transparent wordmarks
    app-icons/         1024 (App Store), 512 (Google Play), 180 (Apple touch)
    android-adaptive/  432 px foreground/background/monochrome layers
  3d/                  rendered 3D versions, transparent, 1024 and 2048 px
  favicon/             favicon.ico (16/32/48), favicon.svg, apple-touch-icon, 192/512
social/
  og-image.png         1200×630 link preview image
source/                scripts that generate all of the above
```

## Rules of thumb

- Default to the **black mark on white**. Use the white mark only on dark backgrounds.
- Leave clear space around the mark of at least a quarter of its width.
- Don't stretch, rotate, recolor outside the palette, or add effects (glows, gradients, shadows) to the flat mark.
- Smallest size: 16 px for the mark, 80 px wide for the horizontal wordmark.

## Regenerating

`source/make_logo.py` builds every SVG from the Inter Tight font (download it from Google Fonts, then make
static Bold/ExtraBold instances with fontTools). `source/render3d.html` renders the 3D versions with three.js in
headless Chrome.
