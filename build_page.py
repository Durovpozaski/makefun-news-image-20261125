#!/usr/bin/env python3
"""Front page for make.fun news-image-20261125.
100% PIL rendering, no network, no AI images.
Frame copied from top-1 yossapr (masthead -> region strip -> UTC strip ->
numbers -> 3 heroes -> grid -> HOW SURE legend -> map -> ALSO -> DATE CHECK)
with the lead order swapped (Hormuz first) and top-1's date errors fixed:
Shenzhou liftoff 00:18, no Tube strike, no Akwe grid item,
Bangladesh as +36% only.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
M = 24
CW = W - 2 * M

CREAM = (247, 244, 235)
PAPER = (253, 251, 245)
NAVY = (30, 58, 95)
NAVY_D = (16, 36, 64)
INK = (34, 34, 34)
RUST = (178, 38, 30)
RUST_L = (251, 233, 231)
TEAL = (15, 118, 110)
TEAL_L = (228, 243, 241)
OCHRE = (180, 83, 9)
GOLD = (198, 158, 40)
GREY = (96, 96, 96)
SKY = (214, 228, 240)

FD = "/usr/share/fonts/truetype/dejavu"


def F(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)


def serif_b(s):
    return F("DejaVuSerif-Bold.ttf", s)


def serif(s):
    return F("DejaVuSerif.ttf", s)


def sans_b(s):
    return F("DejaVuSans-Bold.ttf", s)


def sans(s):
    return F("DejaVuSans.ttf", s)


TAG_COLOR = {
    "OFFICIAL": TEAL,
    "CONFIRMED": NAVY,
    "REPORTED": OCHRE,
    "CLAIM": RUST,
}

# ---------------------------------------------------------------- data ----
REGIONS = [("ASIA", 7), ("MIDDLE EAST", 6), ("EUROPE", 11), ("AMERICAS", 5),
           ("AFRICA", 4), ("OCEANIA", 5), ("WORLD", 2)]

UTC_ITEMS = [
    ("00:18", "Shenzhou-24 lifts off"),
    ("00:30", "Australia CPI +4.9%"),
    ("03:56", "Crew docks at Tiangong"),
    ("06:30", "Kospi closes -6.2%"),
    ("18:45", "Hera unveils Dimorphos images"),
]

NUMBERS = [
    ("1st", "foreign astronaut to Tiangong"),
    ("-6.2%", "Kospi, 10-month low"),
    ("2", "tankers hit mines"),
    ("47,000", "women killed by partner/kin, 2025"),
    ("26", "miners trapped (3 dead)"),
    ("+36%", "Bangladesh wage rise"),
]

HEROES = [
    {"n": 1, "tag": "CLAIM",
     "head": "Two tankers hit mines and burn in Hormuz, Iran says",
     "deck": "IRGC Navy says the vessels took an 'unauthorised route'; "
             "engine rooms on fire. No independent confirmation.",
     "illu": "hormuz"},
    {"n": 2, "tag": "CONFIRMED",
     "head": "Asia's chip stocks crash on AI doubts",
     "deck": "Kospi -6.2% to a 10-month low; SK Hynix -11%, "
             "Samsung -10%, SoftBank -15%.",
     "illu": "kospi"},
    {"n": 3, "tag": "CONFIRMED",
     "head": "Shenzhou-24 flies a Pakistani to Tiangong",
     "deck": "Muhammad Zeeshan Ali, 40, is the first Pakistani in orbit - "
             "and the first foreigner aboard China's station.",
     "illu": "rocket"},
]

GRID = [
    {"n": 4, "tag": "OFFICIAL", "illu": "treaty",
     "head": "Solomons sign security treaty with Australia",
     "deck": "A$740m over 10 years; Canberra is the primary security "
             "partner, no foreign bases."},
    {"n": 5, "tag": "OFFICIAL", "illu": "port",
     "head": "Coalition strikes Hodeidah port; 4 drones downed over Ras Tanura",
     "deck": "After a warning, Houthis threaten Jeddah and Red Sea ports."},
    {"n": 6, "tag": "OFFICIAL", "illu": "shirt",
     "head": "Garment workers win 36% pay rise",
     "deck": "Wage board approves the rise after ~12 hours of talks; "
             "takes effect 1 Dec, paid in January."},
    {"n": 7, "tag": "OFFICIAL", "illu": "mine",
     "head": "Mine flood: 3 bodies found, 23 still trapped",
     "deck": "Rescuers reach the flooded illegal shafts near Bogor; "
             "26 were trapped, 11 escaped."},
    {"n": 8, "tag": "CLAIM", "illu": "refinery",
     "head": "Ukrainian drones set two Russian refineries ablaze",
     "deck": "Fires at Syzran and Kuibyshev plants; governor says 1 killed, "
             "145 drones downed."},
    {"n": 9, "tag": "OFFICIAL", "illu": "building",
     "head": "Strike kills Hamas official and his family of four",
     "deck": "Col. Muhammad Majid Abu al-Awf, his wife and two daughters "
             "die in al-Shati camp, Gaza City."},
    {"n": 10, "tag": "OFFICIAL", "illu": "bolt",
     "head": "UK energy bills to jump 26% in January",
     "deck": "Ofgem cap rises to \u00a32,166 a year - \u00a3443 more for a "
             "typical household."},
    {"n": 11, "tag": "OFFICIAL", "illu": "shield",
     "head": "Met still institutionally racist, review finds",
     "deck": "0 of 14 recommendations show 'good progress'; scandals 'highly likely'."},
    {"n": 12, "tag": "OFFICIAL", "illu": "scales",
     "head": "Judges urge prosecutors to drop gravest Netanyahu case",
     "deck": "Court sees 'considerable difficulties' in the Case 4000 "
             "bribery charge; AG to weigh it."},
    {"n": 13, "tag": "OFFICIAL", "illu": "stars",
     "head": "EU plans \u20ac50bn AI and quantum fund",
     "deck": "Sovereign Tech Equity Fund proposed in Strasbourg; needs "
             "member states and Parliament."},
]

ALSO = [
    "Australia CPI jumps to 4.9%",
    "Australia apologises to LGBTQ veterans",
    "Balkans summit: five leaders, no Serbia",
    "Ukraine blackout: 112 drones, 88 downed",
    "ESA's Hera unveils Dimorphos images",
    "Pete Edochie dies at 79",
    "Houthis claim Ras Tanura refinery hit",
    "Cartagena siege ends, hostages freed",
    "UN: 16 Days against gender violence begin",
    "Trump shelves Russia business deals",
    "Sydney CBD gas leak shuts streets",
    "Thanksgiving storm hits 25 states",
    "Sensex jumps 1.8% to 83,938",
    "Ex-officer guilty of double murder",
    "Huawei rejects US verdict",
    "Gaza: winter aid blocked as storm looms",
    "Tonight: Lille-Bayern, PSG-Roma (UCL)",
    "Sudan: RSF drone strikes kill 19 in Damazin",
    "Libya vows retaliation after drone strike",
    "Merz: Russia escalating threats to Europe",
    "US set to raise tariffs on China, EU, 14 more",
    "Ramaphosa wins Phala Phala court battle",
    "Bodies of 6 recovered off Mississippi",
    "Iraq court backs Baghdad's oil takeover",
    "EasyJet profit falls 89% to \u00a371m",
    "Spain votes Sunday; S\u00e1nchez warns of right",
    "EU court orders cage-ban timeline",
]

DATE_CHECK_NOT = (
    "NOT 25 NOVEMBER: Huawei Brooklyn verdict \u00b7 Chen Jining probe \u00b7 "
    "CIA-ODNI breach \u00b7 WHO Akwe evacuation \u00b7 Odesa strike \u00b7 "
    "Democrats 259 seats \u00b7 CRP Bunia halt \u00b7 Riyadh PIF tower, 2nd strike "
    "\u00b7 CAS AFCON ruling \u00b7 Miss Universe crowning \u00b7 "
    "Zelenskyy-Magyar meeting \u00b7 US-Ecuador pause \u00b7 Amazon-Decart deal "
    "- all Tue 24 Nov \u00b7 Huang's return to Nvidia \u00b7 Colombia car bomb "
    "- Mon 23 Nov \u00b7 COP31 collapse \u00b7 Libya ship attack - Sun 22 Nov "
    "\u00b7 UK-EU summit deal \u00b7 Akvan landfall - Fri 20 Nov \u00b7 "
    "ICJ Rohingya judgment \u00b7 Anthropic first trade - Wed 19 Nov"
)
DATE_CHECK_YET = (
    "NOT YET: London Tube strike (Thu 26 Nov) \u00b7 "
    "US Thanksgiving (Thu 26 Nov) \u00b7 "
    "Special European Council (Thu 26 Nov)"
)

# ------------------------------------------------------------- helpers ----
def tw(draw, text, font):
    return draw.textlength(text, font=font)


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if tw(draw, trial, font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, text, font, x, y, max_w, fill, leading=None):
    if leading is None:
        leading = font.size + 3
    lines = wrap(draw, text, font, max_w)
    for ln in lines:
        draw.text((x, y), ln, font=font, fill=fill)
        y += leading
    return y


def chip(draw, x, y, text, size=10):
    f = sans_b(size)
    w = tw(draw, text, f) + 12
    h = size + 8
    draw.rounded_rectangle([x, y, x + w, y + h], radius=h // 2,
                           fill=TAG_COLOR[text])
    draw.text((x + 6, y + 4), text, font=f, fill=(255, 255, 255))
    return w


def fit_font(draw, text, start, min_size, max_w, bold=True, serif_font=False):
    size = start
    while size > min_size:
        f = (serif_b(size) if serif_font else sans_b(size)) if bold else (
            serif(size) if serif_font else sans(size))
        if tw(draw, text, f) <= max_w:
            return f
        size -= 1
    return (serif_b(min_size) if serif_font else sans_b(min_size)) if bold else (
        serif(min_size) if serif_font else sans(min_size))

# -------------------------------------------------------- illustrations ----
def illu_hormuz(draw, x, y, w, h):
    w, h = int(w), int(h)
    draw.rectangle([x, y, x + w, y + h], fill=NAVY_D)
    draw.rectangle([x, y + int(h * 0.62), x + w, y + h], fill=(24, 68, 96))
    for i in range(5):
        yy = y + int(h * 0.66) + i * 6
        draw.line([x + 8, yy, x + w - 8, yy], fill=(70, 130, 160), width=2)
    # two tanker hulls
    for hx, hw in ((x + 14, 128), (x + w - 150, 118)):
        hy = y + int(h * 0.52)
        draw.polygon([(hx, hy), (hx + hw, hy), (hx + hw - 14, hy + 16),
                      (hx + 10, hy + 16)], fill=(60, 30, 26))
        draw.rectangle([hx + 18, hy - 14, hx + 52, hy], fill=(232, 226, 214))
        draw.rectangle([hx + 60, hy - 9, hx + 96, hy], fill=(178, 38, 30))
        # flames
        fx = hx + hw // 2
        draw.polygon([(fx - 16, hy - 12), (fx - 4, hy - 34), (fx + 4, hy - 16),
                      (fx + 16, hy - 36), (fx + 22, hy - 12)],
                     fill=(232, 126, 32))
        draw.polygon([(fx - 8, hy - 12), (fx, hy - 26), (fx + 9, hy - 12)],
                     fill=(246, 196, 70))
    # mines
    for mx, my in ((x + w - 34, y + 14), (x + 26, y + 22)):
        draw.ellipse([mx - 5, my - 5, mx + 5, my + 5], fill=(20, 20, 20))
        for ang in (0, 45, 90, 135):
            import math
            dx = math.cos(math.radians(ang)) * 8
            dy = math.sin(math.radians(ang)) * 8
            draw.line([mx, my, mx + dx, my + dy], fill=(20, 20, 20), width=2)


def illu_kospi(draw, x, y, w, h):
    w, h = int(w), int(h)
    draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    draw.rectangle([x, y, x + w, y + h], outline=NAVY, width=2)
    gx0, gy0 = x + 12, y + 10
    gx1, gy1 = x + w - 12, y + h - 26
    for i in range(4):
        gy = gy0 + (gy1 - gy0) * i // 3
        draw.line([gx0, gy, gx1, gy], fill=(220, 224, 230), width=1)
    pts = [(gx0, gy0 + 8), (gx0 + 52, gy0 + 22), (gx0 + 104, gy0 + 18),
           (gx0 + 156, gy0 + 44), (gx0 + 208, gy0 + 40),
           (gx0 + 252, gy0 + 66), (gx1, gy1 - 4)]
    draw.line(pts, fill=RUST, width=4, joint="curve")
    for px, py in pts:
        draw.ellipse([px - 3, py - 3, px + 3, py + 3], fill=RUST)
    f = sans_b(30)
    draw.text((x + 14, y + h - 26), "-6.2%", font=f, fill=RUST)
    cap = "KOSPI 4,697.51"
    draw.text((x + w - 12 - tw(draw, cap, sans_b(12)), y + h - 22), cap,
              font=sans_b(12), fill=NAVY)


def illu_rocket(draw, x, y, w, h):
    w, h = int(w), int(h)
    draw.rectangle([x, y, x + w, y + h], fill=NAVY_D)
    import random
    rnd = random.Random(42)
    for _ in range(26):
        sx = x + rnd.randint(4, w - 4)
        sy = y + rnd.randint(4, h - 30)
        r = rnd.choice([1, 1, 2])
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(255, 255, 255))
    # earth arc at bottom
    draw.ellipse([x + w // 2 - 150, y + h - 26, x + w // 2 + 150, y + h + 130],
                 fill=TEAL)
    draw.arc([x + w // 2 - 150, y + h - 26, x + w // 2 + 150, y + h + 130],
             180, 360, fill=(120, 200, 190), width=3)
    # rocket
    cx = x + w // 2
    ry = y + 12
    draw.polygon([(cx - 13, ry + 46), (cx - 13, ry + 18), (cx, ry),
                  (cx + 13, ry + 18), (cx + 13, ry + 46)], fill=(240, 236, 226))
    draw.polygon([(cx, ry), (cx - 13, ry + 18), (cx + 13, ry + 18)],
                 fill=RUST)
    draw.rectangle([cx - 13, ry + 46, cx + 13, ry + 56], fill=NAVY)
    draw.polygon([(cx - 13, ry + 46), (cx - 24, ry + 58), (cx - 13, ry + 56)],
                 fill=RUST)
    draw.polygon([(cx + 13, ry + 46), (cx + 24, ry + 58), (cx + 13, ry + 56)],
                 fill=RUST)
    draw.polygon([(cx - 8, ry + 56), (cx, ry + 76), (cx + 8, ry + 56)],
                 fill=(246, 196, 70))
    draw.ellipse([cx - 5, ry + 24, cx + 5, ry + 34], outline=NAVY, width=2)


HERO_ILLU = {"hormuz": illu_hormuz, "kospi": illu_kospi, "rocket": illu_rocket}


def illu_icon(draw, kind, x, y, w, h):
    cx, cy = x + w // 2, y + h // 2
    if kind == "treaty":  # paper sheet + seal
        draw.rectangle([cx - 11, cy - 13, cx + 9, cy + 13], fill=(255, 255, 255),
                       outline=NAVY, width=2)
        for i, ly in enumerate((-7, -1, 5)):
            draw.line([cx - 7, cy + ly, cx + 5, cy + ly], fill=NAVY, width=2)
        draw.ellipse([cx + 3, cy + 3, cx + 15, cy + 15], fill=RUST)
    elif kind == "port":  # crane + burst
        draw.line([cx - 14, cy + 12, cx - 14, cy - 12], fill=NAVY, width=3)
        draw.line([cx - 14, cy - 12, cx + 12, cy - 4], fill=NAVY, width=3)
        draw.line([cx + 12, cy - 4, cx + 12, cy + 4], fill=NAVY, width=2)
        draw.polygon([(cx + 2, cy + 8), (cx + 6, cy - 2), (cx + 10, cy + 8)],
                     fill=(232, 126, 32))
    elif kind == "shirt":
        draw.polygon([(cx - 12, cy - 8), (cx - 5, cy - 12), (cx + 5, cy - 12),
                      (cx + 12, cy - 8), (cx + 16, cy + 2), (cx + 9, cy + 4),
                      (cx + 9, cy + 13), (cx - 9, cy + 13), (cx - 9, cy + 4),
                      (cx - 16, cy + 2)], fill=TEAL)
    elif kind == "mine":  # tunnel arch + lamp
        draw.pieslice([cx - 13, cy - 12, cx + 13, cy + 14], 180, 360, fill=NAVY)
        draw.rectangle([cx - 13, cy, cx + 13, cy + 14], fill=NAVY)
        draw.ellipse([cx - 3, cy + 2, cx + 3, cy + 8], fill=(246, 196, 70))
    elif kind == "refinery":
        draw.rectangle([cx - 14, cy - 4, cx - 4, cy + 13], fill=NAVY)
        draw.rectangle([cx - 1, cy - 10, cx + 9, cy + 13], fill=NAVY)
        draw.polygon([(cx + 12, cy + 2), (cx + 16, cy - 8), (cx + 20, cy + 2)],
                     fill=(232, 126, 32))
        draw.polygon([(cx - 9, cy - 4), (cx - 6, cy - 12), (cx - 3, cy - 4)],
                     fill=(232, 126, 32))
    elif kind == "building":
        draw.rectangle([cx - 12, cy - 10, cx + 12, cy + 13], fill=NAVY)
        for wy in (-5, 2):
            for wx in (-8, -1, 6):
                draw.rectangle([cx + wx, cy + wy, cx + wx + 4, cy + wy + 4],
                               fill=(246, 196, 70))
        draw.ellipse([cx + 8, cy - 16, cx + 14, cy - 10], fill=RUST)
    elif kind == "bolt":
        draw.polygon([(cx + 3, cy - 14), (cx - 7, cy + 1), (cx - 1, cy + 1),
                      (cx - 4, cy + 14), (cx + 8, cy - 2), (cx + 1, cy - 2)],
                     fill=(246, 196, 70))
    elif kind == "shield":
        draw.polygon([(cx - 11, cy - 11), (cx + 11, cy - 11), (cx + 11, cy + 1),
                      (cx, cy + 14), (cx - 11, cy + 1)], fill=NAVY)
        draw.line([cx - 5, cy, cx - 1, cy + 5, cx + 6, cy - 5], fill=(255, 255, 255),
                  width=2)
    elif kind == "scales":
        draw.line([cx, cy - 12, cx, cy + 12], fill=NAVY, width=2)
        draw.line([cx - 12, cy - 10, cx + 12, cy - 10], fill=NAVY, width=2)
        draw.arc([cx - 14, cy - 2, cx - 4, cy + 8], 0, 180, fill=NAVY, width=2)
        draw.arc([cx + 4, cy - 2, cx + 14, cy + 8], 0, 180, fill=NAVY, width=2)
        draw.ellipse([cx - 2, cy - 14, cx + 2, cy - 10], fill=RUST)
    elif kind == "stars":  # EU circle of stars
        import math
        for k in range(12):
            ang = math.radians(k * 30 - 90)
            sx = cx + int(11 * math.cos(ang))
            sy = cy + int(11 * math.sin(ang))
            draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=GOLD)


# ------------------------------------------------------------- map --------
CONTINENTS = [  # (lon, lat, rx, ry) in map-box px, box is 664 x 96
    (-100, 45, 78, 24), (-60, -15, 36, 27), (15, 52, 32, 13),
    (20, 5, 34, 29), (100, 50, 88, 23), (115, -2, 42, 9),
    (134, -25, 30, 13),
]
PINS = [  # (story no, lon, lat)
    (1, 56, 26), (2, 127, 37), (3, 98, 40), (4, 149, -35),
    (5, 43, 15), (7, 107, -6), (10, 0, 51), (13, 8, 49),
]


def draw_map(draw, x, y, w, h):
    def px(lon, lat):
        return (x + (lon + 180) / 360.0 * w,
                y + (75 - lat) / 130.0 * h)

    def inside(px_, py_):
        for lon, lat, rx, ry in CONTINENTS:
            cx_, cy_ = px(lon, lat)
            sx = rx * w / 664.0
            sy = ry * h / 96.0
            if ((px_ - cx_) / sx) ** 2 + ((py_ - cy_) / sy) ** 2 <= 1:
                return True
        return False

    step = 6
    yy = y + 4
    while yy < y + h - 2:
        xx = x + 4
        while xx < x + w - 2:
            if inside(xx, yy):
                draw.ellipse([xx - 1, yy - 1, xx + 1, yy + 1],
                             fill=(70, 100, 140))
            xx += step
        yy += step
    for n, lon, lat in PINS:
        px_, py_ = px(lon, lat)
        draw.ellipse([px_ - 7, py_ - 7, px_ + 7, py_ + 7], fill=RUST,
                     outline=(255, 255, 255), width=1)
        f = sans_b(9)
        t = str(n)
        draw.text((px_ - tw(draw, t, f) / 2, py_ - 5), t, font=f,
                  fill=(255, 255, 255))

# ----------------------------------------------------------- sections -----
def section_masthead(draw):
    draw.rectangle([0, 0, W, 88], fill=CREAM)
    title = "Wednesday 25 November 2026"
    f = fit_font(draw, title, 46, 30, CW, bold=True, serif_font=True)
    draw.text(((W - tw(draw, title, f)) / 2, 10), title, font=f, fill=NAVY_D)
    sub = ("Tankers burn in Hormuz  \u00b7  Asia's chip stocks crash  "
           "\u00b7  A Pakistani flies to Tiangong")
    fs = sans(14)
    draw.text(((W - tw(draw, sub, fs)) / 2, 62), sub, font=fs, fill=INK)
    draw.line([M, 88, W - M, 88], fill=NAVY, width=2)


def section_regions(draw):
    draw.rectangle([0, 88, W, 114], fill=NAVY)
    parts = []
    for name, n in REGIONS:
        parts.append("%s %d" % (name, n))
    text = "  \u00b7  ".join(parts) + "   =   40 STORIES"
    f = fit_font(draw, text, 14, 10, CW, bold=True)
    draw.text(((W - tw(draw, text, f)) / 2, 95), text, font=f,
              fill=(255, 255, 255))


def section_utc(draw):
    draw.rectangle([0, 114, W, 140], fill=PAPER)
    segs = ["THE DAY IN UTC"]
    for t, label in UTC_ITEMS:
        segs.append("%s %s" % (t, label))
    text = "   \u00b7   ".join(segs)
    f = fit_font(draw, text, 13, 9, CW, bold=False)
    draw.text(((W - tw(draw, text, f)) / 2, 121), text, font=f, fill=NAVY_D)
    draw.line([M, 140, W - M, 140], fill=(200, 200, 190), width=1)


def section_numbers(draw):
    draw.rectangle([0, 140, W, 196], fill=CREAM)
    cell_w = CW / 6.0
    for i, (big, label) in enumerate(NUMBERS):
        cx = M + cell_w * i
        if i:
            draw.line([cx, 148, cx, 188], fill=(200, 196, 182), width=1)
        fb = sans_b(24)
        bw = tw(draw, big, fb)
        draw.text((cx + (cell_w - bw) / 2, 144), big, font=fb, fill=RUST
                  if i in (1, 2, 4) else NAVY_D)
        draw_wrapped(draw, label, sans(9.5), cx + 8, 172, cell_w - 16, GREY,
                     leading=11.5)
    draw.line([M, 196, W - M, 196], fill=NAVY, width=2)


def section_heroes(draw, img):
    y0, y1 = 196, 414
    col_w = (CW - 2 * 12) / 3.0
    for i, hero in enumerate(HEROES):
        x = M + i * (col_w + 12)
        draw.rectangle([x, y0, x + col_w, y1], fill=PAPER,
                       outline=(210, 206, 192), width=1)
        ih = 96
        iw = int(col_w - 2)
        box = Image.new("RGB", (iw, ih), PAPER)
        bd = ImageDraw.Draw(box)
        HERO_ILLU[hero["illu"]](bd, 0, 0, iw, ih)
        img.paste(box, (int(x + 1), y0 + 1))
        draw.text((x + 10, y0 + 8), str(hero["n"]), font=serif_b(20),
                  fill=(255, 255, 255),
                  stroke_width=2, stroke_fill=NAVY_D)
        chip(draw, x + col_w - 92, y0 + 8, hero["tag"], size=10)
        ty = y0 + ih + 10
        ty = draw_wrapped(draw, hero["head"], serif_b(19), x + 10, ty,
                          col_w - 20, NAVY_D, leading=23)
        draw_wrapped(draw, hero["deck"], sans(12), x + 10, ty + 4,
                     col_w - 20, INK, leading=15)


def section_grid(draw):
    y0 = 414
    col_w = (CW - 4 * 8) / 5.0
    row_h, gap = 120, 8
    for idx, card in enumerate(GRID):
        r, c = divmod(idx, 5)
        x = M + c * (col_w + gap)
        y = y0 + r * (row_h + gap)
        draw.rectangle([x, y, x + col_w, y + row_h], fill=PAPER,
                       outline=(210, 206, 192), width=1)
        ih = 38
        draw.rectangle([x + 1, y + 1, x + col_w - 1, y + ih],
                       fill=SKY if idx % 2 == 0 else TEAL_L)
        illu_icon(draw, card["illu"], x, y + 1, col_w, ih)
        draw.text((x + 6, y + 4), str(card["n"]), font=sans_b(11),
                  fill=NAVY_D)
        chip(draw, x + col_w - 76, y + 5, card["tag"], size=9)
        ty = draw_wrapped(draw, card["head"], sans_b(12), x + 7, y + ih + 5,
                          col_w - 14, NAVY_D, leading=13.5)
        draw_wrapped(draw, card["deck"], sans(10), x + 7, ty + 2,
                     col_w - 14, INK, leading=11.5)


def section_legend_map(draw):
    y0, y1 = 662, 758
    draw.rectangle([0, y0, W, y1], fill=CREAM)
    draw.line([M, y0, W - M, y0], fill=(200, 196, 182), width=1)
    draw.text((M, y0 + 8), "HOW SURE", font=sans_b(13), fill=NAVY_D)
    defs = [
        ("OFFICIAL", "government or agency announcement"),
        ("CONFIRMED", "two or more independent sources agree"),
        ("REPORTED", "one reputable source or wire"),
        ("CLAIM", "one party's assertion, not confirmed"),
    ]
    yy = y0 + 28
    for tag, meaning in defs:
        draw.rectangle([M, yy + 2, M + 10, yy + 12], fill=TAG_COLOR[tag])
        draw.text((M + 14, yy), tag, font=sans_b(10), fill=INK)
        draw.text((M + 88, yy), meaning, font=sans(10), fill=GREY)
        yy += 15
    mx = M + 330
    draw.text((mx, y0 + 8), "WHERE IT HAPPENED", font=sans_b(13),
              fill=NAVY_D)
    draw_map(draw, mx, y0 + 26, W - M - mx, y1 - y0 - 30)


def section_also(draw):
    y0 = 758
    draw.text((M, y0), "IN BRIEF \u2014 27 MORE", font=sans_b(13),
              fill=NAVY_D)
    draw.line([M + 170, y0 + 8, W - M, y0 + 8], fill=(200, 196, 182), width=1)
    col_w = (CW - 2 * 16) / 3.0
    for idx, item in enumerate(ALSO):
        c, r = divmod(idx, 9)
        x = M + c * (col_w + 16)
        y = y0 + 20 + r * 18
        draw.text((x, y), "%d." % (14 + idx), font=sans_b(12), fill=RUST)
        draw.text((x + 26, y), item, font=sans(12), fill=INK)


def section_datecheck(draw):
    y0, y1 = 936, 1024
    draw.rectangle([0, y0, W, y1], fill=RUST_L)
    draw.line([0, y0, W, y0], fill=RUST, width=3)
    draw.text((M, y0 + 6), "DATE CHECK \u2014 WHAT WE LEFT OUT",
              font=sans_b(13), fill=RUST)
    y = draw_wrapped(draw, DATE_CHECK_NOT, sans(10.5), M, y0 + 24,
                     CW, (90, 20, 18), leading=13)
    draw_wrapped(draw, DATE_CHECK_YET, sans_b(10.5), M, y + 3, CW, RUST,
                 leading=13)


# ---------------------------------------------------------------- main ----
def build():
    img = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(img)
    section_masthead(draw)
    section_regions(draw)
    section_utc(draw)
    section_numbers(draw)
    section_heroes(draw, img)
    section_grid(draw)
    section_legend_map(draw)
    section_also(draw)
    section_datecheck(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    return out


if __name__ == "__main__":
    path = build()
    size = os.path.getsize(path)
    print("wrote %s %d bytes" % (path, size))
    assert size <= 1024 * 1024, "entry.png over 1 MiB"
