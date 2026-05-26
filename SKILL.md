---
name: line-sticker-set
description: 表情包制作。Generate complete 16-piece LINE-style sticker sets from an uploaded character/theme photo and a conversation scene description. Use when the user says 表情包制作 or asks to reference a character image, create cute/stylized chat stickers, produce Chinese dialogue stickers, avoid cropping/overflow, remove white backgrounds, export transparent PNG stickers, or slice a 4x4 sticker sheet into individual files.
---

# LINE Sticker Set

## Workflow

Use this skill to make a complete sticker pack from a reference image and a scene brief.

1. Inspect the uploaded theme or character image and extract only stable identity traits: character type, face/hair/shape, clothing, colors, signature objects, and mood. Do not overfit to background or pose.
2. Write a single image-generation prompt for a 4x4 sticker sheet on a pure white background. Require every sticker to stay centered inside its own invisible cell safe box with large internal padding and clear gutters between neighboring stickers.
3. Generate the image with the image generation tool. If the first result has cropped bodies, cut-off text, or repeated poses, regenerate with stricter margin language instead of trying to fix it in slicing.
4. Save the generated sheet in the user's requested output folder, or in the current workspace if unspecified.
5. Run `scripts/slice_sticker_sheet.py` on the generated sheet to remove edge-connected white background, crop each cell by content, and export 16 transparent PNG files.
6. Review the output contact sheet or individual PNGs when practical. Regenerate when more than minor edge cleanup would be required.

## Generation Prompt Rules

For the detailed prompt template and phrase bank, read `references/prompt-template.md`.

Always include these constraints in the image prompt:

- 16 stickers arranged as a clean 4x4 grid.
- Pure white background.
- Treat the sheet as 16 separate invisible square cells with clear white gutters between cells.
- Each complete sticker group must be fully inside its own invisible cell safe box.
- At least 25% safe margin inside every cell; keep the usable content inside the central 50-60% of each cell.
- Character should be smaller rather than too large.
- No character parts, props, speech bubbles, effects, decorative marks, or Chinese text may touch or cross a cell boundary.
- Keep all decorative elements attached to the same sticker group; do not let confetti, stars, moons, hats, bubbles, text, hair, hands, or feet spill into neighboring cells.
- All dialogue text must be Chinese, trendy, short, and useful in everyday chat.
- The 16 stickers must have clearly different poses, expressions, props, and text layouts.
- Avoid panel borders, grid lines, watermarks, mockup frames, and shadows on the white background.

If the user supplies a scene placeholder like `【场景】`, replace it with the user's actual scene description. If the user does not supply specific scenes, choose practical daily chat scenes such as greeting, thanks, OK, waiting, working, tired, happy, apology, praise, refusal, hurry, eating, crying, shocked, good night, and cheering.

## Slicing

Use the bundled script after a 4x4 sheet is generated:

```bash
python3 /Users/gormanlee/.codex/skills/line-sticker-set/scripts/slice_sticker_sheet.py \
  --input /path/to/generated_sheet.png \
  --outdir /path/to/output_stickers
```

If `python3` cannot import Pillow, call `load_workspace_dependencies` and run the same script with the bundled Python executable returned by that tool.

Default output:

- `sticker_01.png` through `sticker_16.png`
- transparent background
- centered on a 370x320 transparent canvas suitable for LINE-style stickers
- `contact_sheet.png` for quick review

Useful options:

```bash
# Preserve each cropped sticker's natural size instead of normalizing to 370x320.
--no-normalize

# Change final canvas size.
--canvas-width 512 --canvas-height 512

# Increase retained transparent padding around each sticker.
--padding-ratio 0.12

# Make white removal stricter or looser.
--white-threshold 248
```

## Quality Bar

Before final delivery, check that:

- all 16 PNG files exist;
- each file has transparency;
- no character, prop, bubble, or text is clipped;
- dialogue text is legible after slicing;
- no two stickers use the same pose/layout;
- the set covers everyday conversation needs rather than only decorative expressions.

If slicing reveals clipped elements, do not hide the issue with cropping. Regenerate the sheet with stronger safety-margin constraints.
