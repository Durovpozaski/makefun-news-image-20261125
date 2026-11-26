#!/usr/bin/env python3
"""Front page for make.fun news-image-20261125.
100% PIL rendering, no network, no AI images.
Frame copied from top-1 yossapr (masthead -> region strip -> UTC strip ->
numbers -> 3 heroes -> grid -> HOW SURE legend -> map -> ALSO -> DATE CHECK)
with the lead order swapped (Hormuz first) and top-1's date errors fixed:
Shenzhou liftoff 00:18, no Tube strike, no Akwe grid item,
Bangladesh as +36% only.
Tweaks vs v1: black top band + black masthead with red-diamond subline,
segmented colour region strip, kicker/dateline strips below hero+grid
illustrations carrying the tag pills (pills moved off the artwork).
v3: 33 stories (ALSO 27 -> 20), bigger minimum type (kicker 9, pills 11,
fit_font 11), grid mini-scenes instead of flat icons, hero source lines,
HOW SURE strip above the grid, bigger spread map pins + region legend,
sources line + black footer band.
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
REGIONS = [("ASIA", 7), ("MIDDLE EAST", 6), ("EUROPE", 9), ("AMERICAS", 4),
           ("AFRICA", 3), ("OCEANIA", 3), ("WORLD", 1)]

REGION_COLORS = {
    "ASIA": (178, 38, 30),
    "MIDDLE EAST": (214, 110, 16),
    "EUROPE": (41, 98, 168),
    "AMERICAS": (46, 125, 50),
    "AFRICA": (15, 118, 110),
    "OCEANIA": (124, 58, 200),
    "WORLD": (105, 105, 105),
}

HERO_KICKERS = [
    "WAR AT SEA \u00b7 STRAIT OF HORMUZ",
    "SELL-OFF \u00b7 SEOUL \u00b7 TOKYO",
    "LIFTOFF \u00b7 JIUQUAN, CHINA \u00b7 SPACE",
]

GRID_KICKERS = [
    "CANBERRA",
    "HODEIDAH PORT",
    "DHAKA",
    "BOGOR",
    "SAMARA",
    "GAZA CITY",
    "LONDON, UK",
    "LONDON, UK",
    "JERUSALEM",
    "STRASBOURG",
]

UTC_ITEMS = [
    ("00:18", "Shenzhou lifts off"),
    ("00:30", "Aus CPI +4.9%"),
    ("03:56", "Crew docks"),
    ("06:30", "Kospi -6.2%"),
    ("18:45", "Hera: Dimorphos images"),
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

HERO_SOURCES = [
    "REUTERS \u00b7 IRNA \u00b7 OILPRICE",
    "WSJ \u00b7 AP \u00b7 JOONGANG DAILY",
    "REUTERS \u00b7 XINHUA \u00b7 PEOPLE.CN",
]

GRID = [
    {"n": 4, "tag": "OFFICIAL", "illu": "treaty",
     "head": "Solomons sign security treaty with Australia",
     "deck": "A$740m over 10 years; Canberra is the primary security "
             "partner, no foreign bases."},
    {"n": 5, "tag": "OFFICIAL", "illu": "port",
     "head": "Coalition hits Hodeidah; 4 drones downed",
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
     "head": "Hamas official killed with family of four",
     "deck": "Col. Abu al-Awf, his wife and two daughters "
             "die in al-Shati camp."},
    {"n": 10, "tag": "OFFICIAL", "illu": "bolt",
     "head": "UK energy bills jump 26% in January",
     "deck": "Ofgem cap rises to \u00a32,166 a year - \u00a3443 more for a "
             "typical household."},
    {"n": 11, "tag": "OFFICIAL", "illu": "shield",
     "head": "Met still institutionally racist",
     "deck": "0 of 14 recommendations show 'good progress'; scandals 'highly likely'."},
    {"n": 12, "tag": "OFFICIAL", "illu": "scales",
     "head": "Judges: drop gravest Netanyahu case",
     "deck": "Court sees 'considerable difficulties' in the Case 4000 "
             "bribery charge; AG to weigh it."},
    {"n": 13, "tag": "OFFICIAL", "illu": "stars",
     "head": "EU plans \u20ac50bn AI, quantum fund",
     "deck": "Sovereign Tech Equity Fund proposed in Strasbourg; needs "
             "member states and Parliament."},
]

ALSO = [
    "Australia CPI jumps to 4.9%",
    "Australia apologises to LGBTQ veterans",
    "Balkans summit: five leaders, no Serbia",
    "Ukraine blackout: 112 drones, 88 downed",
    "ESA's Hera unveils Dimorphos images",
    "Houthis claim Ras Tanura refinery hit",
    "Cartagena siege ends, hostages freed",
    "Trump shelves Russia business deals",
    "Thanksgiving storm hits 25 states",
    "Sensex jumps 1.8% to 83,938",
    "Huawei rejects US verdict",
    "Gaza: winter aid blocked as storm looms",
    "Sudan: RSF drone strikes kill 19 in Damazin",
    "Libya vows retaliation after drone strike",
    "Merz: Russia escalating threats to Europe",
    "US set to raise tariffs on China, EU, 14 more",
    "Ramaphosa wins Phala Phala court battle",
    "Iraq court backs Baghdad's oil takeover",
    "EasyJet profit falls 89% to \u00a371m",
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


def chip(draw, x, y, text, size=11):
    f = sans_b(size)
    w = tw(draw, text, f) + 12
    h = size + 8
    draw.rounded_rectangle([x, y, x + w, y + h], radius=h // 2,
                           fill=TAG_COLOR[text])
    draw.text((x + 6, y + 4), text, font=f, fill=(255, 255, 255))
    return w


def kicker(draw, x, y, w, text, tag, base_size=10, min_size=9,
           first_red=False):
    """Dateline strip: text left, tag pill at the right end; shrinks to fit.
    Pill text never below 11px."""
    size = base_size
    pill_size = 11
    while size > min_size:
        f = sans_b(int(round(size)))
        pill_w = tw(draw, tag, sans_b(pill_size)) + 12
        if tw(draw, text, f) + 6 + pill_w <= w:
            break
        size -= 0.5
    ps = int(round(size))
    f = sans_b(ps)
    if first_red and " \u00b7 " in text:
        first, rest = text.split(" \u00b7 ", 1)
        draw.text((x, y + 2), first, font=f, fill=RUST)
        fx = x + tw(draw, first, f)
        draw.text((fx, y + 2), " \u00b7 " + rest, font=sans(ps), fill=GREY)
    else:
        draw.text((x, y + 2), text, font=f, fill=NAVY_D)
    pill_w = tw(draw, tag, sans_b(pill_size)) + 12
    chip(draw, x + w - pill_w, y, tag, size=pill_size)


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


# --------------------------------------------------- grid mini-scenes ----
def illu_scene(draw, kind, x, y, w, h):
    """Small drawn scene (not a flat icon) for a grid card.
    Band is ~189 x 42 px: sky + ground + 2-4 shapes."""
    w, h = int(w), int(h)
    if kind == "treaty":
        # signing table: two figures, document, flags
        draw.rectangle([x, y, x + w, y + h], fill=(232, 226, 214))
        draw.rectangle([x, y + h - 12, x + w, y + h], fill=(150, 110, 70))
        draw.rectangle([x + w // 2 - 26, y + h - 24, x + w // 2 + 26,
                        y + h - 12], fill=(255, 255, 255), outline=NAVY,
                       width=1)
        for ly in (y + h - 21, y + h - 17):
            draw.line([x + w // 2 - 20, ly, x + w // 2 + 20, ly],
                      fill=NAVY, width=1)
        for fx, col in ((x + 34, NAVY), (x + w - 34, TEAL)):
            draw.ellipse([fx - 8, y + 4, fx + 8, y + 20],
                         fill=(232, 190, 150))
            draw.polygon([(fx - 14, y + h - 12), (fx - 10, y + 20),
                          (fx + 10, y + 20), (fx + 14, y + h - 12)],
                         fill=col)
        draw.rectangle([x + 8, y + 6, x + 22, y + 14], fill=(41, 98, 168))
        draw.rectangle([x + w - 22, y + 6, x + w - 8, y + 14], fill=TEAL)
    elif kind == "port":
        # port under strike: sky, sea, ship, crane, burst
        draw.rectangle([x, y, x + w, y + h], fill=(214, 228, 240))
        draw.rectangle([x, y + h - 12, x + w, y + h], fill=(24, 68, 96))
        draw.line([x + 10, y + 6, x + 10, y + h - 12], fill=NAVY, width=3)
        draw.line([x + 10, y + 6, x + 70, y + 16], fill=NAVY, width=3)
        draw.polygon([(x + w // 2 - 40, y + h - 12),
                      (x + w // 2 - 34, y + h - 24),
                      (x + w // 2 + 44, y + h - 24),
                      (x + w // 2 + 50, y + h - 12)], fill=(60, 30, 26))
        draw.rectangle([x + w // 2 - 20, y + h - 32, x + w // 2 + 10,
                        y + h - 24], fill=(232, 226, 214))
        draw.polygon([(x + w - 30, y + 4), (x + w - 22, y + 16),
                      (x + w - 14, y + 4)], fill=(232, 126, 32))
        draw.ellipse([x + w - 34, y + 2, x + w - 10, y + 18],
                     outline=(232, 126, 32), width=2)
    elif kind == "shirt":
        # garment factory: rack of shirts over a workbench
        draw.rectangle([x, y, x + w, y + h], fill=(228, 243, 241))
        draw.rectangle([x, y + h - 14, x + w, y + h], fill=(150, 110, 70))
        draw.line([x + 14, y + 6, x + w - 14, y + 6], fill=NAVY, width=2)
        for sx, col in ((x + 40, TEAL), (x + w // 2, (178, 38, 30)),
                        (x + w - 40, (46, 125, 50))):
            draw.polygon([(sx - 12, y + 8), (sx - 5, y + 6), (sx + 5, y + 6),
                          (sx + 12, y + 8), (sx + 16, y + 16),
                          (sx + 9, y + 18), (sx + 9, y + h - 14),
                          (sx - 9, y + h - 14), (sx - 9, y + 18),
                          (sx - 16, y + 16)], fill=col)
    elif kind == "mine":
        # mine cross-section: earth layers, tunnel, lamp glow
        draw.rectangle([x, y, x + w, y + h], fill=(120, 84, 50))
        draw.rectangle([x, y + 12, x + w, y + 20], fill=(96, 64, 38))
        draw.pieslice([x + w // 2 - 22, y + 8, x + w // 2 + 22, y + h],
                      180, 360, fill=(20, 20, 20))
        draw.rectangle([x + w // 2 - 22, y + h // 2, x + w // 2 + 22, y + h],
                       fill=(20, 20, 20))
        draw.ellipse([x + w // 2 - 6, y + h - 16, x + w // 2 + 6, y + h - 4],
                     fill=(246, 196, 70))
        draw.line([x + 10, y + 4, x + w - 10, y + 4], fill=(246, 196, 70),
                  width=1)
    elif kind == "refinery":
        # refinery towers, flames, smoke
        draw.rectangle([x, y, x + w, y + h], fill=(232, 226, 214))
        draw.rectangle([x, y + h - 8, x + w, y + h], fill=(120, 120, 110))
        draw.rectangle([x + 20, y + 10, x + 44, y + h - 8], fill=NAVY)
        draw.rectangle([x + 52, y + 4, x + 72, y + h - 8], fill=NAVY)
        draw.rectangle([x + 84, y + 16, x + 100, y + h - 8],
                       fill=(60, 60, 60))
        for fx in (x + 32, x + 62):
            draw.polygon([(fx - 8, y + 10), (fx, y + 1), (fx + 8, y + 10)],
                         fill=(232, 126, 32))
        draw.ellipse([x + w - 40, y + 2, x + w - 24, y + 14],
                     fill=(150, 150, 145))
        draw.ellipse([x + w - 52, y + 8, x + w - 38, y + 20],
                     fill=(170, 170, 165))
    elif kind == "building":
        # apartment block at night, lit windows, smoke, rubble
        draw.rectangle([x, y, x + w, y + h], fill=NAVY_D)
        draw.rectangle([x + 24, y + 6, x + w - 60, y + h],
                       fill=(40, 60, 90))
        for wy in (y + 12, y + 22, y + 32):
            for wx in (x + 32, x + 48, x + 64):
                draw.rectangle([wx, wy, wx + 8, wy + 6], fill=(246, 196, 70))
        draw.ellipse([x + w - 44, y + 2, x + w - 24, y + 16],
                     fill=(120, 120, 115))
        draw.ellipse([x + w - 56, y + 10, x + w - 38, y + 24],
                     fill=(100, 100, 95))
        draw.polygon([(x + 8, y + h), (x + 20, y + h - 10), (x + 34, y + h)],
                     fill=(120, 120, 110))
    elif kind == "bolt":
        # house + lightning bolt + price tag
        draw.rectangle([x, y, x + w, y + h], fill=(255, 251, 240))
        draw.polygon([(x + 30, y + 12), (x + 70, y + 12), (x + 50, y + 2)],
                     fill=RUST)
        draw.rectangle([x + 34, y + 12, x + 66, y + h - 6], fill=NAVY)
        draw.rectangle([x + 46, y + 22, x + 54, y + h - 6],
                       fill=(246, 196, 70))
        draw.polygon([(x + w - 40, y + 2), (x + w - 52, y + 20),
                      (x + w - 44, y + 20), (x + w - 50, y + 36),
                      (x + w - 30, y + 14), (x + w - 38, y + 14)],
                     fill=(246, 196, 70))
        draw.ellipse([x + w - 66, y + 4, x + w - 52, y + 18], fill=GOLD)
        draw.text((x + w - 62, y + 6), "\u00a3", font=sans_b(10),
                  fill=NAVY_D)
    elif kind == "shield":
        # police shield + flank markers
        draw.rectangle([x, y, x + w, y + h], fill=(228, 243, 241))
        draw.polygon([(x + w // 2 - 20, y + 4), (x + w // 2 + 20, y + 4),
                      (x + w // 2 + 20, y + 18), (x + w // 2, y + h - 6),
                      (x + w // 2 - 20, y + 18)], fill=NAVY)
        draw.line([x + w // 2 - 10, y + 20, x + w // 2 - 3, y + 27,
                   x + w // 2 + 11, y + 12], fill=(255, 255, 255), width=3)
        draw.ellipse([x + 12, y + 8, x + 24, y + 20], fill=RUST)
        draw.ellipse([x + w - 24, y + 8, x + w - 12, y + 20], fill=RUST)
    elif kind == "scales":
        # courthouse: pediment, columns, base, small scales
        draw.rectangle([x, y, x + w, y + h], fill=(232, 226, 214))
        draw.polygon([(x + w // 2 - 34, y + 8), (x + w // 2 + 34, y + 8),
                      (x + w // 2, y + 2)], fill=NAVY)
        for cx in (x + w // 2 - 28, x + w // 2 - 6, x + w // 2 + 16):
            draw.rectangle([cx, y + 10, cx + 6, y + h - 6],
                           fill=(255, 255, 255), outline=NAVY, width=1)
        draw.rectangle([x + w // 2 - 40, y + h - 8, x + w // 2 + 40,
                        y + h - 4], fill=NAVY)
        scx, scy = x + w - 30, y + 18
        draw.line([scx, scy - 6, scx, scy + 12], fill=RUST, width=2)
        draw.line([scx - 10, scy - 4, scx + 10, scy - 4], fill=RUST, width=2)
    elif kind == "stars":
        # EU circle of stars + chip in the middle
        draw.rectangle([x, y, x + w, y + h], fill=(30, 58, 95))
        import math
        for k in range(12):
            ang = math.radians(k * 30 - 90)
            sx = x + w // 2 + int(15 * math.cos(ang))
            sy = y + h // 2 + int(15 * math.sin(ang))
            draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=GOLD)
        draw.rectangle([x + w // 2 - 7, y + h // 2 - 7,
                        x + w // 2 + 7, y + h // 2 + 7],
                       fill=(255, 255, 255), outline=GOLD, width=1)
        draw.rectangle([x + w // 2 - 3, y + h // 2 - 3,
                        x + w // 2 + 3, y + h // 2 + 3], fill=TEAL)


# ------------------------------------------------------------- map --------
CONTINENTS = [  # (lon, lat, rx, ry) in map-box px, box is 664 x 96
    (-100, 45, 78, 24), (-60, -15, 36, 27), (15, 52, 32, 13),
    (20, 5, 34, 29), (100, 50, 88, 23), (115, -2, 42, 9),
    (134, -25, 30, 13),
]
PINS = [  # (story no, lon, lat)
    (1, 56, 26), (2, 127, 37), (3, 98, 40), (4, 149, -35),
    (5, 43, 15), (7, 107, -6), (10, -4, 52), (13, 10, 48),
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
        draw.ellipse([px_ - 8, py_ - 8, px_ + 8, py_ + 8], fill=RUST,
                     outline=(255, 255, 255), width=1)
        f = sans_b(10)
        t = str(n)
        draw.text((px_ - tw(draw, t, f) / 2, py_ - 5), t, font=f,
                  fill=(255, 255, 255))

# ----------------------------------------------------------- sections -----
def section_masthead(draw):
    # black top band, like top 1
    draw.rectangle([0, 0, W, 20], fill=(0, 0, 0))
    fb = sans_b(11)
    draw.text((M, 4), "THE WORLD IN ONE DAY", font=fb, fill=GOLD)
    right = "33 STORIES \u00b7 ALL FROM WEDNESDAY 25 NOVEMBER 2026"
    draw.text((W - M - tw(draw, right, fb), 4), right, font=fb,
              fill=(255, 255, 255))
    draw.rectangle([0, 20, W, 88], fill=CREAM)
    title = "Wednesday 25 November 2026"
    f = fit_font(draw, title, 44, 30, CW, bold=True, serif_font=True)
    draw.text(((W - tw(draw, title, f)) / 2, 24), title, font=f, fill=(0, 0, 0))
    parts = ["Tankers burn in Hormuz", "Asia's chip stocks crash",
             "A Pakistani flies to Tiangong"]
    fs = sans(14)
    dia = " \u25c6 "
    total = sum(tw(draw, p, fs) for p in parts) + 2 * tw(draw, dia, fs)
    x = (W - total) / 2
    for i, p in enumerate(parts):
        draw.text((x, 72), p, font=fs, fill=INK)
        x += tw(draw, p, fs)
        if i < 2:
            draw.text((x, 72), dia, font=fs, fill=RUST)
            x += tw(draw, dia, fs)
    draw.line([M, 88, W - M, 88], fill=NAVY, width=2)


def section_regions(draw):
    widths = [218, 186, 248, 124, 93, 93, 62]
    x = 0
    for (name, n), wseg in zip(REGIONS, widths):
        draw.rectangle([x, 88, x + wseg, 114], fill=REGION_COLORS[name])
        text = "%s %d" % (name, n)
        f = fit_font(draw, text, 13, 11, wseg - 8, bold=True)
        draw.text((x + (wseg - tw(draw, text, f)) / 2, 95), text, font=f,
                  fill=(255, 255, 255))
        x += wseg


def section_utc(draw):
    draw.rectangle([0, 114, W, 140], fill=PAPER)
    segs = ["THE DAY IN UTC"]
    for t, label in UTC_ITEMS:
        segs.append("%s %s" % (t, label))
    text = "   \u00b7   ".join(segs)
    f = fit_font(draw, text, 13, 11, CW, bold=False)
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
    y0, y1 = 196, 418
    col_w = (CW - 2 * 12) / 3.0
    for i, hero in enumerate(HEROES):
        x = M + i * (col_w + 12)
        draw.rectangle([x, y0, x + col_w, y1], fill=PAPER,
                       outline=(210, 206, 192), width=1)
        ih = 88
        iw = int(col_w - 2)
        box = Image.new("RGB", (iw, ih), PAPER)
        bd = ImageDraw.Draw(box)
        HERO_ILLU[hero["illu"]](bd, 0, 0, iw, ih)
        img.paste(box, (int(x + 1), y0 + 1))
        draw.text((x + 10, y0 + 8), str(hero["n"]), font=serif_b(20),
                  fill=(255, 255, 255),
                  stroke_width=2, stroke_fill=NAVY_D)
        # kicker strip below the illustration, tag pill at its right end
        ky = y0 + ih + 1
        draw.line([x + 1, ky + 20, x + col_w - 1, ky + 20],
                  fill=(210, 206, 192), width=1)
        kicker(draw, x + 8, ky, col_w - 16, HERO_KICKERS[i],
               hero["tag"], base_size=10, min_size=9, first_red=True)
        ty = y0 + ih + 26
        ty = draw_wrapped(draw, hero["head"], serif_b(19), x + 10, ty,
                          col_w - 20, NAVY_D, leading=22)
        ty = draw_wrapped(draw, hero["deck"], sans(12), x + 10, ty + 4,
                          col_w - 20, INK, leading=15)
        draw.text((x + 10, ty + 2), HERO_SOURCES[i], font=sans(9.5),
                  fill=GREY)


def section_grid(draw):
    y0 = 436
    col_w = (CW - 4 * 8) / 5.0
    row_h, gap = 129, 4
    for idx, card in enumerate(GRID):
        r, c = divmod(idx, 5)
        x = M + c * (col_w + gap)
        y = y0 + r * (row_h + gap)
        draw.rectangle([x, y, x + col_w, y + row_h], fill=PAPER,
                       outline=(210, 206, 192), width=1)
        ih = 42
        illu_scene(draw, card["illu"], x + 1, y + 1, col_w - 2, ih)
        draw.rounded_rectangle([x + 3, y + 3, x + 21, y + 17],
                               radius=3, fill=(255, 255, 255))
        draw.text((x + 6, y + 4), str(card["n"]), font=sans_b(11),
                  fill=NAVY_D)
        # kicker strip below the scene, tag pill at its right end
        ky = y + ih + 1
        draw.line([x + 1, ky + 20, x + col_w - 1, ky + 20],
                  fill=(210, 206, 192), width=1)
        kicker(draw, x + 6, ky, col_w - 12, GRID_KICKERS[idx],
               card["tag"], base_size=9, min_size=9, first_red=False)
        ty = draw_wrapped(draw, card["head"], sans_b(12), x + 7, y + ih + 23,
                          col_w - 14, NAVY_D, leading=13.5)
        draw_wrapped(draw, card["deck"], sans(10.5), x + 7, ty + 2,
                     col_w - 14, INK, leading=11.5)


def section_legend_strip(draw):
    y0 = 418
    draw.rectangle([0, y0, W, 436], fill=CREAM)
    draw.text((M, y0 + 4), "HOW SURE", font=sans_b(11), fill=NAVY_D)
    items = [
        ("OFFICIAL", "government or agency"),
        ("CONFIRMED", "two or more sources"),
        ("REPORTED", "one reputable source"),
        ("CLAIM", "one party's claim"),
    ]
    x = M + 92
    for tag, meaning in items:
        draw.rectangle([x, y0 + 6, x + 9, y0 + 15], fill=TAG_COLOR[tag])
        x += 13
        t = "%s: %s" % (tag, meaning)
        draw.text((x, y0 + 4), t, font=sans(10), fill=INK)
        x += tw(draw, t, sans(10)) + 18


def section_map(draw):
    y0, y1 = 698, 772
    draw.rectangle([0, y0, W, y1], fill=CREAM)
    draw.line([M, y0, W - M, y0], fill=(200, 196, 182), width=1)
    draw.text((M, y0 + 5), "WHERE IT HAPPENED \u00b7 PINS = STORY NUMBERS",
              font=sans_b(13), fill=NAVY_D)
    draw_map(draw, M, y0 + 20, CW, 40)
    lx = M
    ly = y0 + 62
    for name in ["ASIA", "MIDDLE EAST", "EUROPE", "AMERICAS", "AFRICA",
                 "OCEANIA", "WORLD"]:
        draw.rectangle([lx, ly, lx + 8, ly + 8], fill=REGION_COLORS[name])
        lx += 11
        label = name.title()
        draw.text((lx, ly - 1), label, font=sans(9), fill=GREY)
        lx += tw(draw, label, sans(9)) + 12


def section_also(draw):
    y0 = 772
    draw.text((M, y0), "IN BRIEF \u2014 20 MORE", font=sans_b(13),
              fill=NAVY_D)
    draw.line([M + 172, y0 + 8, W - M, y0 + 8], fill=(200, 196, 182), width=1)
    col_w = (CW - 2 * 16) / 3.0
    for idx, item in enumerate(ALSO):
        c, r = divmod(idx, 7)
        x = M + c * (col_w + 16)
        y = y0 + 20 + r * 19
        draw.text((x, y), "%d." % (14 + idx), font=sans_b(12), fill=RUST)
        draw.text((x + 26, y), item, font=sans(12), fill=INK)


def section_sources(draw):
    draw.text((M, 920),
              "Sources: Reuters \u00b7 Xinhua \u00b7 AFP \u00b7 AP \u00b7 Al Jazeera "
              "\u00b7 Anadolu \u00b7 WSJ \u00b7 BBC \u00b7 Ofgem \u00b7 UN Women \u00b7 ABS",
              font=sans(9), fill=GREY)


def section_datecheck(draw):
    y0, y1 = 930, 998
    draw.rectangle([0, y0, W, y1], fill=RUST_L)
    draw.line([0, y0, W, y0], fill=RUST, width=3)
    draw.text((M, y0 + 4), "DATE CHECK \u2014 WHAT WE LEFT OUT",
              font=sans_b(12), fill=RUST)
    y = draw_wrapped(draw, DATE_CHECK_NOT, sans(10), M, y0 + 18,
                     CW, (90, 20, 18), leading=12)
    draw_wrapped(draw, DATE_CHECK_YET, sans_b(10), M, y + 2, CW, RUST,
                 leading=12)


def section_footer(draw):
    y0 = 998
    draw.rectangle([0, y0, W, 1024], fill=(0, 0, 0))
    text = ("DRAWN BY AN AI AGENT FOR MAKE.FUN \u00b7 "
            "WEDNESDAY 25 NOVEMBER 2026 \u00b7 ONE DAY, ONE PAGE")
    f = sans_b(11)
    draw.text(((W - tw(draw, text, f)) / 2, y0 + 7), text, font=f,
              fill=GOLD)


# ---------------------------------------------------------------- main ----
def build():
    img = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(img)
    section_masthead(draw)
    section_regions(draw)
    section_utc(draw)
    section_numbers(draw)
    section_heroes(draw, img)
    section_legend_strip(draw)
    section_grid(draw)
    section_map(draw)
    section_also(draw)
    section_sources(draw)
    section_datecheck(draw)
    section_footer(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    return out


if __name__ == "__main__":
    path = build()
    size = os.path.getsize(path)
    print("wrote %s %d bytes" % (path, size))
    assert size <= 1024 * 1024, "entry.png over 1 MiB"
