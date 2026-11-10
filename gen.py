"""Generate the pixel-art SVG panels for the GitHub profile README.

Edit the DATA section below, then run:  python gen.py
Everything is drawn with a built-in 5x7 pixel font (plain <rect>s), because
GitHub strips CSS/fonts from READMEs - SVG images are the only way to get this look.
"""
from pathlib import Path

# ---------------------------------------------------------------- DATA ----
NAME = "FERDINAN NATHANAEL"
PLAYER = [
    ("NAME", "FERDINAN NATHANAEL"),
    ("CLASS", "FULL-STACK DEV"),
    ("REGION", "JAKARTA, ID  UTC+7"),
    ("QUEST", "AI + AUTOMATION"),
]
# (skill, level out of 10) - self-rated, adjust freely
STATS = [
    ("REACT / NEXT.JS", 8),
    ("PYTHON / FASTAPI", 8),
    ("SQL", 7),
    ("FLUTTER", 6),
    ("RAG / AI", 7),
]
# (title, status tag, description, stack, link)
QUESTS = [
    ("PORTFOLIO SITE", "ONLINE",
     "MY PERSONAL SITE WITH A LIVE, INTERACTIVE AI SALES-BOT DEMO.",
     "NEXT.JS / REACT / TAILWIND / GEMINI",
     "https://github.com/DINANANANAN/portfolio"),
    ("WHATSAPP SALES BOT", "NDA",
     "AUTOMATES CUSTOMER INQUIRIES, RECOMMENDS SERVICES AND ANSWERS "
     "PRODUCT QUESTIONS FROM A RAG KNOWLEDGE BANK.",
     "FASTAPI / SQLITE / CHROMADB / OLLAMA",
     "https://ferdinannathanael.vercel.app/#projects"),
    ("BILLIARD SUPER APP", "CO-OP",
     "MATCH HISTORY, TOURNAMENTS, RANKINGS AND POOL HALL DISCOVERY "
     "FOR BILLIARD PLAYERS.",
     "FLUTTER / SUPABASE / POSTGRESQL",
     "https://ptera.id/id/"),
    ("SUMBER GRAHA MAJU", "CLEARED",
     "COMPANY WEBSITE WITH SEARCHABLE PRODUCT CATALOGS AND "
     "WHATSAPP INQUIRIES.",
     "HTML / CSS / JAVASCRIPT / VERCEL",
     "https://sumbergrahamaju.vercel.app"),
]
INVENTORY = [
    ("FRONT", ["REACT", "NEXT.JS", "FLUTTER", "HTML", "CSS", "JAVASCRIPT"]),
    ("BACK", ["FASTAPI", "LARAVEL", "ASP.NET", "FIREBASE", "SUPABASE"]),
    ("DATA", ["POSTGRESQL", "MYSQL", "SQL SERVER", "SQLITE"]),
    ("AI", ["RAG", "CHROMADB", "EMBEDDINGS", "OLLAMA", "WEBHOOKS"]),
    ("TOOLS", ["GIT", "GITHUB", "VS CODE", "FIGMA", "CANVA"]),
]
CONTACTS = [  # (button label, file name) - links are set in README.md
    ("PORTFOLIO", "btn-portfolio"),
    ("LINKEDIN", "btn-linkedin"),
    ("EMAIL", "btn-email"),
]

# -------------------------------------------------------------- PALETTE ---
DARK = "#2a1d15"    # ink / title bars
PAPER = "#ecdcc0"   # panel body
TAN = "#b48c5c"     # empty bar segments, chips
BROWN = "#6e4630"   # labels, partial segments
ACCENT = "#e0a04a"  # highlights
SKIN, SHADE, SHIRT, SHIRT_D = "#c98d5c", "#9c6640", "#d9822b", "#9a5418"

W = 840
OUT = Path(__file__).parent / "assets"

# ----------------------------------------------------------- PIXEL FONT ---
F = {
    "A": "01110 10001 10001 11111 10001 10001 10001",
    "B": "11110 10001 10001 11110 10001 10001 11110",
    "C": "01110 10001 10000 10000 10000 10001 01110",
    "D": "11110 10001 10001 10001 10001 10001 11110",
    "E": "11111 10000 10000 11110 10000 10000 11111",
    "F": "11111 10000 10000 11110 10000 10000 10000",
    "G": "01110 10001 10000 10111 10001 10001 01111",
    "H": "10001 10001 10001 11111 10001 10001 10001",
    "I": "01110 00100 00100 00100 00100 00100 01110",
    "J": "00111 00010 00010 00010 00010 10010 01100",
    "K": "10001 10010 10100 11000 10100 10010 10001",
    "L": "10000 10000 10000 10000 10000 10000 11111",
    "M": "10001 11011 10101 10101 10001 10001 10001",
    "N": "10001 10001 11001 10101 10011 10001 10001",
    "O": "01110 10001 10001 10001 10001 10001 01110",
    "P": "11110 10001 10001 11110 10000 10000 10000",
    "Q": "01110 10001 10001 10001 10101 10010 01101",
    "R": "11110 10001 10001 11110 10100 10010 10001",
    "S": "01111 10000 10000 01110 00001 00001 11110",
    "T": "11111 00100 00100 00100 00100 00100 00100",
    "U": "10001 10001 10001 10001 10001 10001 01110",
    "V": "10001 10001 10001 10001 10001 01010 00100",
    "W": "10001 10001 10001 10101 10101 10101 01010",
    "X": "10001 10001 01010 00100 01010 10001 10001",
    "Y": "10001 10001 01010 00100 00100 00100 00100",
    "Z": "11111 00001 00010 00100 01000 10000 11111",
    "0": "01110 10001 10011 10101 11001 10001 01110",
    "1": "00100 01100 00100 00100 00100 00100 01110",
    "2": "01110 10001 00001 00010 00100 01000 11111",
    "3": "11111 00010 00100 00010 00001 10001 01110",
    "4": "00010 00110 01010 10010 11111 00010 00010",
    "5": "11111 10000 11110 00001 00001 10001 01110",
    "6": "00110 01000 10000 11110 10001 10001 01110",
    "7": "11111 00001 00010 00100 01000 01000 01000",
    "8": "01110 10001 10001 01110 10001 10001 01110",
    "9": "01110 10001 10001 01111 00001 00010 01100",
    " ": "00000 00000 00000 00000 00000 00000 00000",
    ".": "00000 00000 00000 00000 00000 01100 01100",
    ",": "00000 00000 00000 00000 01100 00100 01000",
    "-": "00000 00000 00000 11111 00000 00000 00000",
    "+": "00000 00100 00100 11111 00100 00100 00000",
    "/": "00001 00001 00010 00100 01000 10000 10000",
    ":": "00000 01100 01100 00000 01100 01100 00000",
    "'": "00100 00100 01000 00000 00000 00000 00000",
    "&": "01100 10010 10100 01000 10101 10010 01101",
    "(": "00010 00100 01000 01000 01000 00100 00010",
    ")": "01000 00100 00010 00010 00010 00100 01000",
    "!": "00100 00100 00100 00100 00100 00000 00100",
    "#": "01010 01010 11111 01010 11111 01010 01010",
    "@": "01110 10001 10111 10101 10111 10000 01111",
    "*": "00000 00100 10101 01110 10101 00100 00000",
    ">": "10000 11000 11100 11110 11100 11000 10000",  # play arrow
}
F = {k: v.split() for k, v in F.items()}


def tw(s, sc):
    """Width in px of string s at pixel scale sc."""
    return max(len(s) * 6 * sc - sc, 0)


def text(s, x, y, sc, color):
    out = []
    for i, ch in enumerate(s.upper()):
        rows = F[ch]
        ox = x + i * 6 * sc
        for r, row in enumerate(rows):
            c = 0
            while c < 5:  # merge horizontal runs into one rect
                if row[c] == "1":
                    start = c
                    while c < 5 and row[c] == "1":
                        c += 1
                    out.append(f'<rect x="{ox + start * sc}" y="{y + r * sc}" '
                               f'width="{(c - start) * sc}" height="{sc}"/>')
                else:
                    c += 1
    return f'<g fill="{color}">{"".join(out)}</g>'


def rect(x, y, w, h, fill):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>'


def notched(x, y, w, h, fill, u=4):
    """Rectangle with pixel-cut corners."""
    return rect(x + u, y, w - 2 * u, h, fill) + rect(x, y + u, w, h - 2 * u, fill)


def panel(h, title, right=""):
    """Card with a dark title bar; body area starts at y=52."""
    p = [notched(0, 0, W, h, DARK, 8),
         notched(6, 46, W - 12, h - 52, PAPER, 4),
         text(title, 22, 14, 3, PAPER)]
    if right:
        p.append(text(right, W - 22 - tw(right, 3), 14, 3, ACCENT))
    return p


def svg(name, h, body, w=W):
    OUT.mkdir(exist_ok=True)
    (OUT / f"{name}.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" shape-rendering="crispEdges">'
        + "".join(body) + "</svg>", encoding="utf-8")


def wrap(s, n):
    lines, cur = [], ""
    for word in s.split():
        if cur and len(cur) + 1 + len(word) > n:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    return lines + [cur] if cur else lines


# ------------------------------------------------------------- PANELS -----
def header():
    sc = 5
    x = (W - tw(NAME, sc)) // 2
    prompt = "> PRESS START"
    px = (W - tw(prompt, 2)) // 2
    svg("header", 110, [
        text(NAME, x + 5, 15, sc, BROWN),   # drop shadow
        text(NAME, x, 10, sc, ACCENT),
        f'<g>{text(prompt, px, 74, 2, TAN)}'
        '<animate attributeName="opacity" values="1;1;0;0" dur="1.2s" '
        'repeatCount="indefinite"/></g>',
    ])


AVATAR = [
    "................",
    ".....hhhhhh.....",
    "....hhhhhhhh....",
    "...hhhhhhhhhh...",
    "...hhsssssshh...",
    "...hssssssssh...",
    "...sseesseess...",
    "...ssssssssss...",
    "...sssmmmmsss...",
    "....dssssssd....",
    "......ssss......",
    "...cccckkcccc...",
    "..cccccccccccc..",
    ".cccccccccccccc.",
    ".cccccccccccccc.",
    ".cccccccccccccc.",
]
AV_COLORS = {"h": DARK, "s": SKIN, "d": SHADE, "e": DARK, "m": BROWN,
             "c": SHIRT, "k": SHIRT_D}


def player():
    h = 52 + 28 + 140 + 24
    p = panel(h, "PLAYER", "SAVE 01")
    ax, ay, px = 30, 72, 8
    p.append(rect(ax - 6, ay - 6, 16 * px + 12, 16 * px + 12, DARK))
    p.append(rect(ax, ay, 16 * px, 16 * px, TAN))
    for r, row in enumerate(AVATAR):
        for c, ch in enumerate(row):
            if ch != ".":
                p.append(rect(ax + c * px, ay + r * px, px, px, AV_COLORS[ch]))
    lx, vx = 196, 196 + 7 * 18
    for i, (k, v) in enumerate(PLAYER):
        y = 78 + i * 34
        p.append(text(k, lx, y, 3, BROWN))
        p.append(text(v, vx, y, 3, DARK))
    svg("player", h, p)


def stats():
    rows = len(STATS)
    h = 52 + 20 + rows * 44 + 10
    p = panel(h, "STATS", "SELF-RATED")
    seg_w, gap = 40, 6
    bx = W - 24 - 10 * seg_w - 9 * gap
    for i, (k, lvl) in enumerate(STATS):
        y = 72 + i * 44
        p.append(text(k, 24, y + 4, 3, DARK))
        for s in range(10):
            fill = DARK if s < lvl - 1 else BROWN if s == lvl - 1 else TAN
            x = bx + s * (seg_w + gap)
            p.append(rect(x, y, seg_w, 28, DARK))
            p.append(rect(x + 3, y + 3, seg_w - 6, 22, fill))
    svg("stats", h, p)


def quests():
    for n, (title, tag, desc, stack, _) in enumerate(QUESTS, 1):
        lines = wrap(desc, (W - 48) // 12)
        h = 52 + 22 + 21 + 18 + len(lines) * 24 + 14 + 30 + 10
        p = panel(h, f"QUEST {n}/{len(QUESTS)}", tag)
        y = 74
        p.append(text("*", 24, y, 3, ACCENT))
        p.append(text(title, 24 + 24, y, 3, DARK))
        y += 21 + 18
        for line in lines:
            p.append(text(line, 24, y, 2, BROWN))
            y += 24
        y += 14
        p.append(notched(24, y - 8, tw(stack, 2) + 24, 30, DARK, 3))
        p.append(text(stack, 36, y, 2, PAPER))
        svg(f"quest-{n}", h, p)


def inventory():
    label_w = 6 * 12 + 24
    body, y = [], 70
    for label, items in INVENTORY:
        body.append(text(label, 24, y + 8, 2, BROWN))
        x = 24 + label_w
        for it in items:
            cw = tw(it, 2) + 24
            if x + cw > W - 24:
                x, y = 24 + label_w, y + 40
            body.append(notched(x, y, cw, 30, DARK, 3))
            body.append(rect(x + 3, y + 3, cw - 6, 24, TAN))
            body.append(text(it, x + 12, y + 8, 2, DARK))
            x += cw + 10
        y += 44
    h = y + 10
    svg("inventory", h, panel(h, "INVENTORY", "EQUIPPED") + body)


def buttons():
    bw, bh = 260, 56
    for label, name in CONTACTS:
        svg(name, bh, [
            notched(0, 0, bw, bh, DARK, 6),
            notched(5, 5, bw - 10, bh - 14, ACCENT, 3),
            text("> " + label, (bw - tw("> " + label, 3)) // 2, 15, 3, DARK),
        ], w=bw)


if __name__ == "__main__":
    header(); player(); stats(); quests(); inventory(); buttons()
    print("wrote", len(list(OUT.glob("*.svg"))), "SVGs to", OUT)
