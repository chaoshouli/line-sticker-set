#!/usr/bin/env python3
import argparse
from collections import deque
from pathlib import Path

from PIL import Image


def parse_args():
    parser = argparse.ArgumentParser(
        description="Slice a pure-white 4x4 sticker sheet into transparent PNG stickers."
    )
    parser.add_argument("--input", required=True, help="Path to the generated 4x4 sticker sheet.")
    parser.add_argument("--outdir", required=True, help="Directory for exported PNG stickers.")
    parser.add_argument("--rows", type=int, default=4)
    parser.add_argument("--cols", type=int, default=4)
    parser.add_argument("--white-threshold", type=int, default=248)
    parser.add_argument("--padding-ratio", type=float, default=0.08)
    parser.add_argument("--canvas-width", type=int, default=370)
    parser.add_argument("--canvas-height", type=int, default=320)
    parser.add_argument("--no-normalize", action="store_true")
    return parser.parse_args()


def is_white(pixel, threshold):
    r, g, b, a = pixel
    return a == 0 or (r >= threshold and g >= threshold and b >= threshold)


def remove_edge_white(cell, threshold):
    image = cell.convert("RGBA")
    width, height = image.size
    pixels = image.load()
    seen = set()
    queue = deque()

    for x in range(width):
        queue.append((x, 0))
        queue.append((x, height - 1))
    for y in range(height):
        queue.append((0, y))
        queue.append((width - 1, y))

    while queue:
        x, y = queue.popleft()
        if (x, y) in seen or x < 0 or y < 0 or x >= width or y >= height:
            continue
        seen.add((x, y))
        if not is_white(pixels[x, y], threshold):
            continue
        r, g, b, _ = pixels[x, y]
        pixels[x, y] = (r, g, b, 0)
        queue.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))

    return image


def crop_to_alpha(image, padding_ratio):
    bbox = image.getchannel("A").getbbox()
    if bbox is None:
        return image

    width, height = image.size
    left, top, right, bottom = bbox
    pad = round(max(right - left, bottom - top) * padding_ratio)
    left = max(0, left - pad)
    top = max(0, top - pad)
    right = min(width, right + pad)
    bottom = min(height, bottom + pad)
    return image.crop((left, top, right, bottom))


def normalize_canvas(image, canvas_width, canvas_height):
    canvas = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))
    max_width = int(canvas_width * 0.92)
    max_height = int(canvas_height * 0.92)
    working = image.copy()
    working.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
    x = (canvas_width - working.width) // 2
    y = (canvas_height - working.height) // 2
    canvas.alpha_composite(working, (x, y))
    return canvas


def make_contact_sheet(stickers, out_path, cols=4):
    if not stickers:
        return
    cell_w = max(sticker.width for sticker in stickers)
    cell_h = max(sticker.height for sticker in stickers)
    rows = (len(stickers) + cols - 1) // cols
    sheet = Image.new("RGBA", (cell_w * cols, cell_h * rows), (255, 255, 255, 255))
    for index, sticker in enumerate(stickers):
        x = (index % cols) * cell_w + (cell_w - sticker.width) // 2
        y = (index // cols) * cell_h + (cell_h - sticker.height) // 2
        sheet.alpha_composite(sticker, (x, y))
    sheet.convert("RGB").save(out_path)


def main():
    args = parse_args()
    source = Image.open(args.input).convert("RGBA")
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    cell_width = source.width // args.cols
    cell_height = source.height // args.rows
    stickers = []

    for row in range(args.rows):
        for col in range(args.cols):
            index = row * args.cols + col + 1
            box = (
                col * cell_width,
                row * cell_height,
                (col + 1) * cell_width if col < args.cols - 1 else source.width,
                (row + 1) * cell_height if row < args.rows - 1 else source.height,
            )
            cell = source.crop(box)
            transparent = remove_edge_white(cell, args.white_threshold)
            cropped = crop_to_alpha(transparent, args.padding_ratio)
            final = (
                cropped
                if args.no_normalize
                else normalize_canvas(cropped, args.canvas_width, args.canvas_height)
            )
            output_path = outdir / f"sticker_{index:02d}.png"
            final.save(output_path)
            stickers.append(final)

    make_contact_sheet(stickers, outdir / "contact_sheet.png", cols=args.cols)
    print(f"Exported {len(stickers)} stickers to {outdir}")


if __name__ == "__main__":
    main()
