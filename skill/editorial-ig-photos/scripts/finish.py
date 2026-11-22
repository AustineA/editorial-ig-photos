#!/usr/bin/env python3
"""Finish generated photos in code: a gentle vignette plus fine film grain, then an optional contact sheet.

usage: finish.py IMG [IMG ...] [--sheet sheet.jpg] [--vignette 0.13] [--grain 0.05] [--inplace | --out DIR]
Grain goes last and is never prompted: below 4K, prompted grain renders as digital noise.
"""
import argparse, os
import numpy as np
from PIL import Image

def finish(path, out, vig, grain, seed):
    im = np.asarray(Image.open(path).convert("RGB")).astype(np.float32) / 255
    h, w, _ = im.shape
    y, x = np.ogrid[:h, :w]
    r = np.sqrt(((x - w / 2) / (w / 2)) ** 2 + ((y - h / 2) / (h / 2)) ** 2)
    im *= (1 - vig * np.clip(r - 0.45, 0, 1) ** 1.6)[..., None]
    g = np.random.default_rng(seed).normal(0, 1, (h // 2, w // 2)).astype(np.float32)
    g = Image.fromarray((g * 40 + 128).clip(0, 255).astype(np.uint8)).resize((w, h), Image.BILINEAR)
    g = np.asarray(g).astype(np.float32) / 255 - 0.5
    lum = im.mean(2, keepdims=True)
    im += g[..., None] * grain * (1 - np.abs(lum - 0.5) * 1.2)  # grain sits in the midtones
    Image.fromarray((im.clip(0, 1) * 255).astype(np.uint8)).save(out, quality=92)

def sheet(paths, out, cols=4, tw=340):
    ims = [Image.open(p) for p in paths]
    th = round(tw * ims[0].height / ims[0].width)
    rows = (len(ims) + cols - 1) // cols
    s = Image.new("RGB", (cols * (tw + 10) + 10, rows * (th + 10) + 10), "white")
    for k, im in enumerate(ims):
        s.paste(im.resize((tw, th)), (10 + (k % cols) * (tw + 10), 10 + (k // cols) * (th + 10)))
    s.save(out, quality=85)

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("images", nargs="+")
    a.add_argument("--vignette", type=float, default=0.13)
    a.add_argument("--grain", type=float, default=0.05)
    a.add_argument("--out", help="output folder (default: alongside, suffix -finished)")
    a.add_argument("--inplace", action="store_true")
    a.add_argument("--sheet")
    o = a.parse_args()
    done = []
    for i, p in enumerate(o.images):
        if o.inplace: dst = p
        elif o.out:
            os.makedirs(o.out, exist_ok=True); dst = os.path.join(o.out, os.path.basename(p))
        else:
            b, e = os.path.splitext(p); dst = f"{b}-finished{e}"
        finish(p, dst, o.vignette, o.grain, i + 1); done.append(dst); print(dst)
    if o.sheet: sheet(done, o.sheet); print(o.sheet)
