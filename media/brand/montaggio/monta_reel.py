"""VF_C01 v3: niente intro/outro, gancio subito, sottotitoli parola per parola con parole chiave caricate."""
import subprocess, numpy as np, json, sys, re
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
INK = np.array([0x12, 0x14, 0x1B], float)
PAPER = np.array([0xED, 0xE6, 0xD6], float)
GOLD = (0xC9, 0xA4, 0x5C)
PERG = (0xED, 0xE6, 0xD6)
INKT = (0x12, 0x14, 0x1B)

def prep(name):
    im = Image.open("src/" + name).convert("L")
    w, h = im.size
    mx, my = int(w * 0.075), int(h * 0.045)
    im = im.crop((mx, my, w - mx, h - my))
    w, h = im.size
    th = w * 16 / 9
    top = (h - th) / 2
    im = im.crop((0, int(top), w, int(top + th)))
    a = np.asarray(im).astype(float) / 255.0
    lo, hi = np.percentile(a, 1), np.percentile(a, 99)
    a = np.clip((a - lo) / max(hi - lo, 1e-3), 0, 1)
    rgb = INK + (PAPER - INK) * a[..., None]
    return Image.fromarray(rgb.astype(np.uint8)).resize((W * 2, H * 2), Image.LANCZOS)

# ---------------- voice timeline ----------------
dur = [3.211, 4.091, 4.131, 3.411, 4.531, 6.091, 8.171, 2.451]
GAP, LEAD = 0.15, 0.0
starts, t = [], LEAD
for d in dur:
    starts.append(round(t, 3)); t += d + GAP
VOICE_END = starts[-1] + dur[-1]
END_HOLD = 1.2
TOTAL = round(VOICE_END + END_HOLD, 3)

# speech chunks per sentence (from the pauses in each file): (from, to, text)
chunks = [
    [(0.26, 1.28, "Chi guida | la tua vita?"), (1.62, 1.80, "Tu,"), (2.09, 3.03, "o le tue | emozioni?")],
    [(0.31, 0.84, "Platone,"), (0.95, 1.58, "nel Fedro,"), (1.84, 3.94, "descrive l'uomo | come una | biga alata.")],
    [(0.29, 1.13, "Due cavalli,"), (1.30, 2.70, "uno bianco | e uno nero:"), (2.89, 3.86, "sono le | passioni.")],
    [(0.15, 2.32, "E un auriga | che tiene salde | le redini:"), (2.56, 3.35, "è la ragione.")],
    [(0.26, 1.94, "I cavalli | non sono il male."), (2.26, 3.01, "Senza di loro"), (3.15, 4.36, "la biga | non si muove.")],
    [(0.13, 1.52, "Ma dove va | la biga"), (1.75, 3.59, "non lo decidono | i cavalli."), (3.98, 4.80, "Lo decide"), (5.03, 5.92, "l'auriga.")],
    [(0.26, 0.64, "Oggi"), (0.76, 2.00, "abbiamo | ribaltato tutto."), (2.27, 4.57, "In Inside Out, | nella testa | della bambina,"),
     (4.68, 6.67, "alla console | ci sono | solo le emozioni."), (6.87, 7.92, "La ragione | non c'è.")],
    [(0.26, 0.61, "E tu,"), (0.85, 2.12, "a chi hai dato | le redini?")],
]
KEY = {"passioni", "ragione", "auriga", "l'auriga", "cavalli", "emozioni", "redini", "biga", "platone", "fedro", "inside", "out"}

def weight(w):
    return max(1, len(re.findall(r"[aeiouàèéìòù]", w.lower())))

words = []  # (start, end, word, sentence_idx, group_id)
gid = 0
for si, sent in enumerate(chunks):
    for (a, b, txt) in sent:
        parts = [p.split() for p in txt.split("|")]
        ws = [w for p in parts for w in p]
        tot = sum(weight(w) for w in ws)
        x = a
        for p in parts:
            for w in p:
                d = (b - a) * weight(w) / tot
                words.append((starts[si] + x, starts[si] + x + d, w, si, gid))
                x += d
            gid += 1
groups = []
for w in words:
    if not groups or groups[-1][-1][4] != w[4]: groups.append([])
    groups[-1].append(w)
gtimes = []
for i, g in enumerate(groups):
    st = g[0][0] - 0.05
    en = groups[i + 1][0][0] - 0.05 if i + 1 < len(groups) else VOICE_END + 0.3
    if en - g[-1][1] > 0.6: en = g[-1][1] + 0.6   # don't linger over pauses
    gtimes.append((st, en))

# ---------------- images ----------------
F7_SPLIT = starts[6] + 2.13
segs = [
    (0, starts[1], "I1.png", 1.00, 1.08, .5, .65),
    (starts[1], starts[2], "I2.png", 1.00, 1.08, .5, .70),
    (starts[2], starts[3], "I3.png", 1.00, 1.08, .5, .65),
    (starts[3], starts[4], "I4.png", 1.00, 1.08, .5, .65),
    (starts[4], starts[5], "I5.png", 1.00, 1.07, .5, .70),
    (starts[5], starts[6], "I6.png", 1.00, 1.12, .55, .55),
    (starts[6], F7_SPLIT, "I7a.png", 1.00, 1.05, .5, .70),
    (F7_SPLIT, starts[7], "I7b.png", 1.00, 1.08, .5, .70),
    (starts[7], TOTAL + 1, "I8.png", 1.00, 1.08, .5, .72),
]
titles = [
    (0.0, starts[1], "CHI GUIDA?", PERG),
    (starts[1] + 0.1, starts[2], "PLATONE · FEDRO", PERG),
    (starts[2] + 2.89, starts[3], "PASSIONI", PERG),
    (starts[3] + 2.56, starts[4], "RAGIONE", GOLD),
    (starts[5] + 1.75, starts[5] + 3.95, "NON DECIDONO\nI CAVALLI", PERG),
    (starts[5] + 3.98, starts[6], "DECIDE\nL'AURIGA", GOLD),
    (F7_SPLIT + 0.1, starts[7], "OGGI:\nSOLO EMOZIONI", PERG),
    (starts[7] + 0.05, TOTAL + 1, "A CHI HAI DATO\nLE REDINI?", GOLD),
]

LORA = "fonts/Lora-SemiBold.ttf"
fonts = {}
def F(size):
    size = int(size)
    if size not in fonts: fonts[size] = ImageFont.truetype(LORA, size)
    return fonts[size]

def ease_out(x):
    x = min(max(x, 0), 1); return 1 - (1 - x) ** 3

def draw_spaced(d, x, y, s, font, fill, spacing, stroke=0, stroke_fill=None):
    for c in s:
        d.text((x, y), c, font=font, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
        x += d.textlength(c, font=font) + spacing

def spaced_w(d, s, font, spacing):
    return sum(d.textlength(c, font=font) for c in s) + spacing * (len(s) - 1)

def title_layer(txt, col, age, remain):
    a = min(age / 0.2, 1.0, remain / 0.15)
    sc = 0.86 + 0.14 * ease_out(age / 0.25)        # pop-in
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    size = 112
    while max(spaced_w(d, s, F(size), 8) for s in txt.split("\n")) > W * 0.84: size -= 4
    size *= sc
    font = F(size)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    lines = txt.split("\n"); lh = size * 1.18; sp = 8 * sc
    y0 = H * 0.165 - lh * len(lines) / 2
    for i, s in enumerate(lines):
        x = (W - spaced_w(d, s, font, sp)) / 2; y = y0 + i * lh
        draw_spaced(ds, x, y, s, font, INKT + (int(230 * a),), sp)
        draw_spaced(d, x, y, s, font, col + (int(255 * a),), sp)
    ry = y0 + lh * len(lines) + 16
    d.line([(W / 2 - 90 * sc, ry), (W / 2 + 90 * sc, ry)], fill=GOLD + (int(255 * a),), width=4)
    return Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)), lay)

def sub_layer(gi, t):
    g = groups[gi]; st, en = gtimes[gi]
    age, remain = t - st, en - t
    a = min(age / 0.1, 1.0, remain / 0.08)
    sc = 0.92 + 0.08 * ease_out(age / 0.14)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    items = []
    for (ws, we, w, si, c) in g:
        key = re.sub(r"[^\wàèéìòù']", "", w.lower()) in KEY
        active = ws - 0.03 <= t < we + 0.05
        base = 96 * sc * (1.22 if key else 1.0)
        if active: base *= 1.10
        col = GOLD if (key or active) else PERG
        if active and not key: col = (0xF6, 0xF0, 0xE2)
        items.append((w.upper(), F(base), col, key, active))
    sp_word = 22
    widths = [d.textlength(s, font=f) for s, f, *_ in items]
    total = sum(widths) + sp_word * (len(items) - 1)
    lines = [list(range(len(items)))]
    if total > W * 0.88 and len(items) > 1:
        lines = [list(range(len(items) - 1)), [len(items) - 1]]
    lh = 132 * sc
    yc = 0.19 if starts[5] <= g[0][0] < starts[6] else 0.30
    y0 = H * yc - lh * len(lines) / 2
    for li, idxs in enumerate(lines):
        lw = sum(widths[i] for i in idxs) + sp_word * (len(idxs) - 1)
        x = (W - lw) / 2
        for i in idxs:
            s, f, col, key, active = items[i]
            yb = y0 + li * lh + (lh - f.size) * 0.55
            d.text((x, yb), s, font=f, fill=col + (int(255 * a),), stroke_width=5, stroke_fill=INKT + (int(235 * a),))
            x += widths[i] + sp_word
    maxw = max(sum(widths[i] for i in idxs) + sp_word * (len(idxs) - 1) for idxs in lines)
    pill = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dp = ImageDraw.Draw(pill)
    dp.rounded_rectangle([(W - maxw) / 2 - 34, y0 - 6, (W + maxw) / 2 + 34, y0 + lh * len(lines) + 10],
                         radius=26, fill=INKT + (int(140 * a),))
    return Image.alpha_composite(pill, lay)

def frame_from(big, z, fx, fy):
    bw, bh = big.size; cw, ch = bw / z, bh / z
    cx = min(max(fx * bw, cw / 2), bw - cw / 2); cy = min(max(fy * bh, ch / 2), bh - ch / 2)
    return big.resize((W, H), Image.BICUBIC, box=(cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2))

cache = {s[2]: prep(s[2]) for s in segs}
n = int(round(TOTAL * FPS))
ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                       "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt",
                       "yuv420p", "video_muto_v4.mp4"], stdin=subprocess.PIPE)
for f in range(n):
    t = f / FPS
    for (st, en, img, z0, z1, fx, fy) in segs:
        if st <= t < en:
            p = (t - st) / (min(en, TOTAL) - st)
            fr = frame_from(cache[img], z0 + (z1 - z0) * p, fx, fy).convert("RGBA"); break
    for (st, en, txt, col) in []:
        if st <= t < en:
            age = t - st
            fr = Image.alpha_composite(fr, title_layer(txt, col, age if st > 0 else 1.0, min(en, TOTAL + 0.2) - t))
    for gi, (st, en) in enumerate(gtimes):
        if st <= t < en:
            fr = Image.alpha_composite(fr, sub_layer(gi, t)); break
    if t > VOICE_END + 0.2:   # brand name in the final second, where the subtitles were
        a = min((t - VOICE_END - 0.2) / 0.3, 1.0)
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); font = F(76)
        s = "VITAFORTE"; sw = spaced_w(d, s, font, 14); x = (W - sw) / 2; y = H * 0.30 - 40
        d.rounded_rectangle([x - 40, y - 20, x + sw + 40, y + 112], radius=26, fill=INKT + (int(190 * a),))
        draw_spaced(d, x, y, s, font, PERG + (int(255 * a),), 14)
        fr = Image.alpha_composite(fr, lay)
    ff.stdin.write(fr.convert("RGB").tobytes())
    if f % 300 == 0: print(f, "/", n, file=sys.stderr)
ff.stdin.close(); ff.wait()
json.dump({"starts": starts, "total": TOTAL, "voice_end": VOICE_END,
           "groups": [[" ".join(w[2] for w in g), round(gtimes[i][0], 2)] for i, g in enumerate(groups)]},
          open("timeline_v3.json", "w"), ensure_ascii=False, indent=0)
print("TOTAL", TOTAL, "starts", starts)
