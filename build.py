#!/usr/bin/env python3
"""Φτιάχνει το site από το content.json:  / (αγγλικά), /el/, /ro/, /bg/, /de/, /tr/, sitemap.xml, robots.txt
Τρέξε: python3 build.py"""
import json, os, html
from urllib.parse import quote

ROOT = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(ROOT, "content.json"), encoding="utf-8"))
SITE, LANGS, P = C["site"], C["languages"], C["photos"]
e = lambda s: html.escape(str(s), quote=True)
# Κωδικός γλώσσας για το Google (hreflang / lang): τα σερβικά είναι σε λατινικό αλφάβητο
HL = {"sr": "sr-Latn"}
hl = lambda l: HL.get(l, l)


UTM = "?utm_source=thassos_guide&utm_medium=referral"


def img(key, w=1600):
    p = P[key]
    if p.get("src"):  # Unsplash (hotlink, όπως ζητούν οι κανόνες του Unsplash)
        return f"{p['src']}&w={w}&auto=format&fit=crop&q=80"
    return f"https://commons.wikimedia.org/wiki/Special:FilePath/{quote(p['file'])}?width={w}"


def url(lang):
    return f"{SITE}/" if lang == "en" else f"{SITE}/{lang}/"


def gpath(lang, slug):
    return f"/{slug}/" if lang == "en" else f"/{lang}/{slug}/"


def gurl(lang, slug):
    return SITE + gpath(lang, slug)


def path(lang):
    return "/" if lang == "en" else f"/{lang}/"


CSS = """
:root{--marble:#F6F7F4;--vein:#E3E7E1;--pine:#143D30;--pine2:#1E5443;--aegean:#0D6C80;--shallow:#9ED8CC;--honey:#C9952F;--ink:#1D2622;--muted:#5A6862;
--disp:"Literata",Georgia,"Times New Roman",serif;--body:"Manrope",system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans",Arial,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--body);color:var(--ink);background:var(--marble);line-height:1.65;font-size:17px}
h1,h2,h3{font-family:var(--disp);font-weight:600;line-height:1.12;letter-spacing:-.012em;color:var(--pine)}
a{color:var(--aegean);text-underline-offset:3px}
a:focus-visible,select:focus-visible,.btn:focus-visible{outline:3px solid var(--honey);outline-offset:3px}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
.ic{width:26px;height:26px;stroke:currentColor;fill:none;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;flex:none}
/* top bar */
header.top{position:absolute;top:0;left:0;right:0;z-index:20}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;height:72px;gap:16px}
.brand{color:#fff;font-family:var(--disp);font-size:1.25rem;font-weight:600;text-decoration:none;display:flex;align-items:center;gap:10px}
.brand svg{width:30px;height:30px}
nav.links{display:flex;gap:24px}
nav.links a{color:#fffd;text-decoration:none;font-size:.92rem}
nav.links a:hover{color:#fff;text-decoration:underline}
.langsel{position:relative}
.langsel select{appearance:none;background:#0003;color:#fff;border:1px solid #fff6;border-radius:8px;padding:8px 32px 8px 12px;font:inherit;font-size:.88rem;cursor:pointer;backdrop-filter:blur(6px)}
.langsel select option{color:var(--ink)}
.langsel:after{content:"";position:absolute;right:13px;top:50%;width:7px;height:7px;border:solid #fff;border-width:0 1.5px 1.5px 0;transform:translateY(-70%) rotate(45deg);pointer-events:none}
@media(max-width:900px){nav.links{display:none}}
/* hero: the one orchestrated moment */
.hero{position:relative;min-height:92vh;display:flex;align-items:flex-end;color:#fff;overflow:hidden;background:var(--pine)}
.hero .bg{position:absolute;inset:0;background:var(--hero) center/cover no-repeat;transform:scale(1.06);animation:settle 2.4s cubic-bezier(.2,.7,.2,1) forwards}
.hero:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,#0b231b55 0%,#0b231b10 35%,#0b231bd9 100%)}
.hero .wrap{position:relative;z-index:2;padding-bottom:88px;padding-top:130px;width:100%}
.hero h1{color:#fff;font-size:clamp(2.8rem,8vw,6.2rem);font-weight:500;max-width:11ch;letter-spacing:-.025em;opacity:0;animation:rise 1.2s .35s cubic-bezier(.2,.7,.2,1) forwards}
.hero p{font-size:clamp(1.05rem,1.8vw,1.25rem);max-width:34em;color:#ffffffe6;margin-top:22px;opacity:0;animation:rise 1.2s .6s cubic-bezier(.2,.7,.2,1) forwards}
.hero .where{display:block;font-size:.95rem;color:var(--shallow);margin-bottom:6px;opacity:0;animation:rise 1s .2s forwards}
.btn{display:inline-block;margin-top:30px;background:var(--honey);color:#22180a;font-weight:700;padding:14px 24px;border-radius:6px;text-decoration:none;opacity:0;animation:rise 1s .85s forwards}
.btn:hover{background:#d8a63f}
.credit{position:absolute;right:16px;bottom:12px;z-index:2;font-size:.7rem;color:#ffffffb3}
@keyframes settle{to{transform:scale(1)}}
@keyframes rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@media(prefers-reduced-motion:reduce){.hero .bg,.hero h1,.hero p,.hero .where,.btn{animation:none;opacity:1;transform:none}}
/* facts band */
.facts{background:var(--pine);color:#fff}
.facts ul{list-style:none;display:grid;grid-template-columns:repeat(4,1fr)}
.facts li{display:flex;gap:14px;align-items:flex-start;padding:26px 22px;border-left:1px solid #ffffff1f}
.facts li:first-child{border-left:0;padding-left:0}
.facts .ic{color:var(--shallow);margin-top:3px}
.facts b{display:block;font-family:var(--disp);font-weight:500;font-size:1.35rem;line-height:1.2}
.facts span{color:#ffffffb8;font-size:.9rem}
@media(max-width:820px){.facts ul{grid-template-columns:1fr 1fr}.facts li{border-left:0;padding-left:0;border-top:1px solid #ffffff1f}.facts li:nth-child(-n+2){border-top:0}}
/* sections */
section.s{padding:96px 0 0}
h2{font-size:clamp(1.9rem,4vw,2.9rem);max-width:20ch}
.lede{font-size:1.12rem;color:var(--muted);max-width:40em;margin-top:14px}
/* getting there: a route line between ports */
.routes{margin-top:36px;display:grid;grid-template-columns:repeat(3,1fr);gap:36px}
@media(max-width:860px){.routes{grid-template-columns:1fr;gap:26px}}
.route h3{font-size:1.25rem;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.route h3 .ic{color:var(--aegean)}
.route .line{height:2px;margin:14px 0 14px;background:repeating-linear-gradient(90deg,var(--aegean) 0 8px,transparent 8px 14px)}
.route p{color:#34413b;max-width:34em}
.note{margin-top:26px;font-size:.93rem;color:var(--muted);max-width:44em}
.around{margin-top:64px;display:grid;grid-template-columns:1fr 1.15fr;gap:40px;align-items:center}
@media(max-width:860px){.around{grid-template-columns:1fr}}
.around h3{font-size:1.6rem;margin-bottom:12px}
.around p{color:#34413b}
figure{margin:0}
figure img{display:block;width:100%;height:auto;border-radius:4px;object-fit:cover;background:var(--vein)}
.around>*,.vgrid>*,.mapgrid>*,.routes>*,.blist>*{min-width:0}
figcaption{font-size:.74rem;color:var(--muted);margin-top:8px}
/* map: the memorable piece */
.mapsec{margin-top:96px;background:#fff;border-top:1px solid var(--vein);border-bottom:1px solid var(--vein);padding:80px 0}
.mapgrid{display:grid;grid-template-columns:1.35fr 1fr;gap:48px;align-items:center}
@media(max-width:900px){.mapgrid{grid-template-columns:1fr}}
.map svg{width:100%;height:auto;display:block}
.map .sea{fill:#EAF5F2}
.map .land{fill:#DCE9DF;stroke:var(--pine2);stroke-width:1.4}
.map .road{fill:none;stroke:#fff;stroke-width:2.5;stroke-dasharray:1 7;stroke-linecap:round}
.map text{font-family:var(--body);font-size:13px;fill:var(--ink);paint-order:stroke;stroke:#EAF5F2;stroke-width:4px;stroke-linejoin:round}
.map .k-port{fill:var(--pine)}.map .k-beach{fill:var(--aegean)}.map .k-village{fill:var(--honey)}
@media(max-width:600px){.map text{font-size:21px;stroke-width:5px}}
.map a:hover text,.map a:focus text{fill:var(--aegean);text-decoration:underline}
.legend{list-style:none;display:grid;gap:22px}
.legend h3{font-size:1.05rem;font-family:var(--body);font-weight:700;color:var(--ink);display:flex;align-items:center;gap:10px;margin-bottom:6px}
.legend .sw{width:12px;height:12px;border-radius:50%;display:inline-block}
.legend .sw.port{border-radius:2px;background:var(--pine)}.legend .sw.beach{background:var(--aegean)}.legend .sw.village{background:var(--honey);transform:rotate(45deg);border-radius:2px}
.legend p{color:#34413b;font-size:.97rem}
.mapnote{font-size:.8rem;color:var(--muted);margin-top:10px}
/* beaches: an editorial index, not a card kit */
.blist{margin-top:34px;display:grid;grid-template-columns:1fr 1fr;column-gap:56px}
@media(max-width:860px){.blist{grid-template-columns:1fr}}
.blist div{padding:22px 0;border-top:1px solid var(--vein)}
.blist h3{font-size:1.45rem;font-weight:500}
.blist h3 a{color:inherit;text-decoration:none;border-bottom:2px solid var(--shallow)}
.blist h3 a:hover{border-color:var(--aegean)}
.blist p{color:#34413b;margin-top:6px;max-width:34em}
/* villages */
.vgrid{margin-top:34px;display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start}
@media(max-width:860px){.vgrid{grid-template-columns:1fr}}
.vlist{list-style:none}
.vlist li{padding:18px 0 18px 26px;border-top:1px solid var(--vein);position:relative}
.vlist li:before{content:"";position:absolute;left:2px;top:27px;width:9px;height:9px;background:var(--honey);transform:rotate(45deg)}
.vlist b{display:block;font-family:var(--disp);font-weight:600;font-size:1.18rem;color:var(--pine)}
.vlist span{color:#34413b}
.vgrid figure img{aspect-ratio:4/5}
/* guides */
.glist{margin-top:34px;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:28px}
.gcard{display:block;text-decoration:none;color:var(--ink)}
.gcard .ph{aspect-ratio:3/2;border-radius:4px;background:var(--ph) center/cover no-repeat,var(--vein);transition:filter .3s}
.gcard:hover .ph{filter:saturate(1.15) brightness(1.04)}
.gcard h3{font-size:1.3rem;margin-top:14px}
.gcard:hover h3{color:var(--aegean)}
.gcard p{color:#34413b;font-size:.95rem;margin-top:6px}
.gcard .more{display:inline-block;margin-top:8px;font-weight:700;color:var(--aegean)}
/* tips */
.tips{list-style:none;margin-top:30px;display:grid;grid-template-columns:1fr 1fr;column-gap:56px}
@media(max-width:760px){.tips{grid-template-columns:1fr}}
.tips li{padding:18px 0 18px 34px;border-top:1px solid var(--vein);position:relative;color:#34413b}
.tips li:before{content:"";position:absolute;left:2px;top:24px;width:14px;height:8px;border:solid var(--aegean);border-width:0 0 2px 2px;transform:rotate(-45deg)}
.wide{margin-top:56px}
.wide img{max-height:460px}
/* guide article */
.ghero{position:relative;min-height:64vh;display:flex;align-items:flex-end;color:#fff;background:linear-gradient(180deg,#0b231b55 0%,#0b231b10 40%,#0b231bd9 100%),var(--hero) center/cover no-repeat,var(--pine)}
.ghero .wrap{padding-bottom:56px;padding-top:120px;width:100%}
.ghero .where{display:block;color:var(--shallow);font-size:.95rem;margin-bottom:8px}
.ghero h1{color:#fff;font-size:clamp(2.3rem,6vw,4.4rem);font-weight:500;max-width:16ch}
.article{max-width:700px;margin:0 auto;padding:56px 24px 0}
.article .lead{font-family:var(--disp);font-size:1.3rem;line-height:1.6;color:var(--pine);margin-bottom:34px}
.article h2{font-size:1.65rem;margin:40px 0 10px}
.article p{color:#2b3833}
.tipbox{margin-top:46px;border-left:3px solid var(--honey);padding:4px 0 4px 22px}
.tipbox h3{font-size:1.25rem;margin-bottom:10px}
.tipbox ul{margin-left:18px;display:grid;gap:8px;color:#2b3833}
.srcs{margin-top:34px;font-size:.9rem;color:var(--muted)}.srcs a{margin-right:10px}
.backl{display:inline-block;margin-top:26px;font-weight:700;text-decoration:none}
/* footer */
footer{margin-top:110px;background:var(--pine);color:#cfdcd5;padding:52px 0;font-size:.9rem}
footer a{color:#fff}
footer .cols{display:grid;grid-template-columns:1fr 1fr;gap:40px}
@media(max-width:760px){footer .cols{grid-template-columns:1fr}}
footer h4{color:#fff;font-family:var(--disp);font-weight:600;font-size:1.1rem;margin-bottom:12px}
footer ul{list-style:none;display:grid;gap:7px}
.langs{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:16px}.langs a{color:#cfdcd5}
footer li,footer p{overflow-wrap:anywhere}
footer .cols>div{min-width:0}
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,400..700&family=Manrope:wght@400;600;700&display=swap" rel="stylesheet">')

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="15" fill="#9ED8CC"/>'
        '<path d="M8 19c3-6 6-9 8-9s5 3 8 9" fill="#143D30"/><path d="M5 22c4-2 7-2 11 0s7 2 11 0" stroke="#0D6C80" stroke-width="2" fill="none" stroke-linecap="round"/></svg>')

ICONS = {  # σχεδιασμένα για το site, ίδιο πάχος γραμμής
  "ship": '<path d="M3 17h18l-2.5 3.5h-13z"/><path d="M6 17l1-6h10l1 6"/><path d="M10 11V6h4v5"/><path d="M12 6V3"/>',
  "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
  "waves": '<path d="M2 9c2.5-2 5-2 7.5 0s5 2 7.5 0 3.5-1.5 5-1"/><path d="M2 15c2.5-2 5-2 7.5 0s5 2 7.5 0 3.5-1.5 5-1"/>',
  "jar": '<path d="M8 3h8"/><path d="M9 3v3c-2 1-3 3-3 5v7a3 3 0 0 0 3 3h6a3 3 0 0 0 3-3v-7c0-2-1-4-3-5V3"/><path d="M6 12h12"/>',
  "car": '<path d="M5 16l1.5-5h11L19 16"/><rect x="3" y="16" width="18" height="3" rx="1"/><circle cx="7" cy="19" r="1"/><circle cx="17" cy="19" r="1"/>',
  "plane": '<path d="M2 14l20-7-7 15-3-6z"/><path d="M12 16l3-6"/>',
}


def icon(name):
    return f'<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


def place_name(p, lang):
    n = p["name"]
    return n.get(lang) or n["default"]


def island_map(lang):
    """Σχηματικός χάρτης της Θάσου (SVG), από τα σημεία του content.json."""
    S, X0, Y0, K = 1638, 170, 40, 0.758
    px = lambda lon, lat: (X0 + (lon - 24.52) * K * S, Y0 + (40.81 - lat) * S)
    outline = [(24.70,40.802),(24.745,40.792),(24.778,40.770),(24.795,40.738),(24.802,40.700),(24.795,40.660),(24.780,40.622),
               (24.752,40.592),(24.712,40.568),(24.665,40.556),(24.620,40.568),(24.582,40.590),(24.552,40.622),(24.533,40.662),
               (24.530,40.702),(24.548,40.742),(24.585,40.772),(24.625,40.792),(24.665,40.802)]
    pts = [px(*q) for q in outline]
    n = len(pts)
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(n):  # Catmull-Rom → Bézier για ομαλή ακτογραμμή
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    # ο περιφερειακός δρόμος: μια μικρότερη, εσωτερική εκδοχή της ακτής
    cx = sum(p[0] for p in pts) / n; cy = sum(p[1] for p in pts) / n
    road = " ".join(f"{'M' if i == 0 else 'L'}{cx + (x - cx) * .9:.1f},{cy + (y - cy) * .9:.1f}" for i, (x, y) in enumerate(pts)) + "Z"
    marks = []
    for p in C["map"]["places"]:
        x, y = px(p["lon"], p["lat"])
        left = p["lon"] < 24.64
        tx, anchor = (x - 11, "end") if left else (x + 11, "start")
        k = p["kind"]
        shape = (f'<rect class="k-port" x="{x-5:.1f}" y="{y-5:.1f}" width="10" height="10" rx="1.5"/>' if k == "port" else
                 f'<circle class="k-beach" cx="{x:.1f}" cy="{y:.1f}" r="5.5"/>' if k == "beach" else
                 f'<rect class="k-village" x="{x-4.5:.1f}" y="{y-4.5:.1f}" width="9" height="9" transform="rotate(45 {x:.1f} {y:.1f})"/>')
        sn = p.get("short") or p["name"]
        label = f'<text x="{tx:.1f}" y="{y+4.5:.1f}" text-anchor="{anchor}">{e(sn.get(lang) or sn["default"])}</text>'
        href = gpath(lang, p["guide"]) if p.get("guide") else ("#beaches" if k == "beach" else "#villages" if k == "village" else "#getting")
        marks.append(f'<a href="{href}">{shape}{label}</a>')
    W, H = 700, 40 + 0.26 * S + 40
    return (f'<svg viewBox="0 0 {W} {H:.0f}" role="img" aria-label="{e(C["i18n"][lang]["map_h"])}">'
            f'<rect class="sea" width="{W}" height="{H:.0f}" rx="6"/><path class="land" d="{d}Z"/><path class="road" d="{road}"/>'
            + "".join(marks) + "</svg>")


def credit(key):
    p = P[key]
    if p.get("src"):
        return (f'Photo by <a href="{e(p["author_url"])}{UTM}" target="_blank" rel="noopener">{e(p["author"])}</a> on '
                f'<a href="https://unsplash.com/{UTM}" target="_blank" rel="noopener">Unsplash</a>'
                f' · <a href="{e(p["page"])}{UTM}" target="_blank" rel="noopener">{e(p.get("alt") or "photo")}</a>')
    lic = f'<a href="{e(p["license_url"])}" target="_blank" rel="noopener">{e(p["license"])}</a>' if p["license_url"] else e(p["license"])
    return (f'<a href="https://commons.wikimedia.org/wiki/File:{quote(p["file"])}" target="_blank" rel="noopener">{e(p["file"].rsplit(".",1)[0].replace("_"," "))}</a>'
            f' · {e(p["author"])} · {lic} · Wikimedia Commons')


def short_credit(key):
    p = P[key]
    if p.get("src"):
        return f'Photo: {e(p["author"])} / Unsplash'
    p = P[key]
    return f'Photo: {e(p["author"])} / Wikimedia Commons, {e(p["license"])}'


def head(lang, title, desc, canon, alts, ogimg):
    return f"""<!DOCTYPE html>
<html lang="{hl(lang)}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="google-site-verification" content="bIGBCT5ZKMfr6wYTzHqtlYJxI6Z6y_axiCzH9b8dbJc" />
<link rel="canonical" href="{canon}">
{alts}
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}"><meta property="og:image" content="{ogimg}">
<meta property="og:url" content="{canon}"><meta property="og:locale" content="{hl(lang)}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='30' fill='%230f8b6f'/%3E%3Cpath d='M10 40c8-6 14-6 22 0s14 6 22 0' stroke='%23fff' stroke-width='5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E">
{FONTS}
<style>{CSS}</style>"""


def topbar(lang, opts_for):
    t = C["i18n"][lang]
    opts = "".join(f'<option value="{opts_for(l)}"{" selected" if l == lang else ""}>{e(C["i18n"][l]["name"])}</option>' for l in LANGS)
    return f"""<header class="top"><div class="wrap">
  <a class="brand" href="{path(lang)}">{LOGO}{e(t['brand'])}</a>
  <label class="langsel" aria-label="{e(t['lang_label'])}"><select onchange="location.href=this.value">{opts}</select></label>
</div></header>"""


def footer(lang):
    t = C["i18n"][lang]
    return f"""<footer><div class="wrap cols">
  <div>
    <h4>{e(t['brand'])}</h4>
    <p>{e(t['disclaimer'])}</p>
    <p class="langs" style="margin-top:14px">{''.join(f'<a href="{path(l)}">{e(C["i18n"][l]["name"])}</a>' for l in LANGS)}</p>
  </div>
  <div>
    <h4>{e(t['photo_credits'])}</h4>
    <ul>{''.join(f'<li>{credit(k)}</li>' for k in P)}</ul>
  </div>
</div></footer>
</body></html>
"""


def guide_page(lang, g):
    t, gt = C["i18n"][lang], g["i18n"][lang]
    alts = "".join(f'<link rel="alternate" hreflang="{hl(l)}" href="{gurl(l, g["slug"])}">' for l in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{gurl("en", g["slug"])}">'
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": gt["h1"], "description": gt["description"],
          "inLanguage": hl(lang), "dateModified": g["updated"], "image": img(g["photo"], 1200), "mainEntityOfPage": gurl(lang, g["slug"])}
    secs = "".join(f"<h2>{e(h)}</h2><p>{e(p)}</p>" for h, p in gt["sections"])
    tips = "".join(f"<li>{e(x)}</li>" for x in gt["tips"])
    srcs = " ".join(f'<a href="{e(s["url"])}" target="_blank" rel="noopener">{e(s["name"])}</a>' for s in g["sources"])
    return (head(lang, gt["title"], gt["description"], gurl(lang, g["slug"]), alts, img(g["photo"], 1200))
            + f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head><body>'
            + topbar(lang, lambda l: gpath(l, g["slug"]))
            + f"""<section class="ghero" style="--hero:url('{img(g['photo'])}')"><div class="wrap">
  <span class="where">{e(t['hero_kicker'])}</span><h1>{e(gt['h1'])}</h1></div>
  <div class="credit">{short_credit(g['photo'])}</div></section>
<article class="article">
  <p class="lead">{e(gt['intro'])}</p>
  {secs}
  <div class="tipbox"><h3>{e(t['tips_box'])}</h3><ul>{tips}</ul></div>
  <p class="srcs">{e(t['sources'])}: {srcs} · {e(t['updated'])}: {g['updated']}</p>
  <a class="backl" href="{path(lang)}">← {e(t['back'])}</a>
</article>"""
            + footer(lang))


def guides_html(lang):
    gs = C.get("guides", [])
    if not gs:
        return ""
    t = C["i18n"][lang]
    cards = "".join(f'<a class="gcard" href="{gpath(lang, g["slug"])}"><div class="ph" style="--ph:url(\'{img(g["photo"], 800)}\')"></div>'
                    f'<div class="tx"><h3>{e(g["i18n"][lang]["h1"])}</h3><p>{e(g["i18n"][lang]["description"][:150])}…</p>'
                    f'<span class="more">{e(t["read"])}</span></div></a>' for g in gs)
    return f'<section class="s" id="guides"><div class="wrap"><h2>{e(t["guides_h"])}</h2><div class="glist">{cards}</div></div></section>'


def page(lang):
    t = C["i18n"][lang]
    alts = "".join(f'<link rel="alternate" hreflang="{hl(l)}" href="{url(l)}">' for l in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{url("en")}">'
    opts = "".join(f'<option value="{path(l)}"{" selected" if l == lang else ""}>{e(C["i18n"][l]["name"])}</option>' for l in LANGS)
    ficons = ["ship", "sun", "waves", "jar"]
    facts = "".join(f'<li>{icon(ficons[i % 4])}<div><b>{e(b)}</b><span>{e(c)}</span></div></li>' for i, (_, b, c) in enumerate(t["facts"]))
    ricons = ["ship", "ship", "plane"]
    routes = "".join(f'<div class="route"><h3>{icon(ricons[i % 3])}{e(h)}</h3><div class="line"></div><p>{e(p)}</p></div>' for i, (h, p) in enumerate(t["getting"]))
    gslugs = {g["slug"] for g in C.get("guides", [])}
    def bname(i, h):
        slug = ["giola", "marble-beach", "golden-beach", "paradise-beach", "aliki"][i] if i < 5 else None
        return f'<a href="{gpath(lang, slug)}">{e(h)}</a>' if slug in gslugs else e(h)
    beaches = "".join(f'<div><h3>{bname(i, h)}</h3><p>{e(p)}</p></div>' for i, (h, p) in enumerate(t["beaches"]))
    vill = "".join(f'<li><b>{e(h)}</b><span>{e(p)}</span></li>' for h, p in t["villages"])
    tips = "".join(f"<li>{e(x)}</li>" for x in t["tips"])
    ld = {"@context": "https://schema.org", "@type": "TouristDestination", "name": "Thassos", "url": url(lang),
          "description": t["description"], "image": img("sunrise", 1200), "inLanguage": hl(lang),
          "geo": {"@type": "GeoCoordinates", "latitude": 40.68, "longitude": 24.65}}
    nav = t["nav"]
    return (head(lang, t["title"], t["description"], url(lang), alts, img("sunrise", 1200))
            + f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head><body>'
            + f"""<header class="top"><div class="wrap">
  <a class="brand" href="{path(lang)}">{LOGO}{e(t['brand'])}</a>
  <nav class="links"><a href="#getting">{e(nav['getting'])}</a><a href="#map">{e(t['map_h'])}</a><a href="#beaches">{e(nav['beaches'])}</a><a href="#villages">{e(nav['villages'])}</a><a href="#tips">{e(nav['tips'])}</a></nav>
  <label class="langsel" aria-label="{e(t['lang_label'])}"><select onchange="location.href=this.value">{opts}</select></label>
</div></header>

<section class="hero" style="--hero:url('{img('sunrise', 2000)}')">
  <div class="bg" aria-hidden="true"></div>
  <div class="wrap">
    <span class="where">{e(t['hero_kicker'])}</span>
    <h1>{e(t['hero_title'])}</h1>
    <p>{e(t['hero_sub'])}</p>
    <a class="btn" href="#getting">{e(t['cta'])}</a>
  </div>
  <div class="credit">{short_credit('sunrise')}</div>
</section>

<div class="facts"><div class="wrap"><ul>{facts}</ul></div></div>

<section class="s" id="getting"><div class="wrap">
  <h2>{e(t['getting_h'])}</h2>
  <div class="routes">{routes}</div>
  <p class="note">{e(t['getting_note'])}</p>
  <div class="around">
    <div><h3>{e(t['around_h'])}</h3><p>{e(t['around'])}</p></div>
    <figure><img loading="lazy" src="{img('village', 1200)}" alt="Mountain village on Thassos" width="1200" height="800"><figcaption>{short_credit('village')}</figcaption></figure>
  </div>
</div></section>

<section class="mapsec" id="map"><div class="wrap mapgrid">
  <div class="map">{island_map(lang)}<p class="mapnote">{e(t['map_note'])}</p></div>
  <div>
    <h2>{e(t['map_h'])}</h2>
    <p class="lede">{e(t['map_lead'])}</p>
    <ul class="legend" style="margin-top:28px">
      <li><h3><span class="sw port"></span>{e(t['legend_ports'])}</h3><p>{e(', '.join(place_name(p, lang) for p in C['map']['places'] if p['kind']=='port'))}</p></li>
      <li><h3><span class="sw beach"></span>{e(t['legend_beaches'])}</h3><p>{e(', '.join(place_name(p, lang) for p in C['map']['places'] if p['kind']=='beach'))}</p></li>
      <li><h3><span class="sw village"></span>{e(t['legend_villages'])}</h3><p>{e(', '.join(place_name(p, lang) for p in C['map']['places'] if p['kind']=='village'))}</p></li>
    </ul>
  </div>
</div></section>

<section class="s" id="beaches" style="padding-top:88px"><div class="wrap">
  <h2>{e(t['beaches_h'])}</h2>
  <div class="blist">{beaches}</div>
</div></section>

<section class="s" id="villages"><div class="wrap">
  <h2>{e(t['villages_h'])}</h2>
  <div class="vgrid">
    <ul class="vlist">{vill}</ul>
    <figure><img loading="lazy" src="{img('theologos', 1000)}" alt="Theologos village, Thassos" width="1000" height="1250"><figcaption>Theologos · {short_credit('theologos')}</figcaption></figure>
  </div>
</div></section>

{guides_html(lang)}

<section class="s" id="tips"><div class="wrap">
  <h2>{e(t['tips_h'])}</h2>
  <ul class="tips">{tips}</ul>
  <figure class="wide"><img loading="lazy" src="{img('beach_aerial', 1800)}" alt="Aerial view of a beach on Thassos" width="1800" height="1012"><figcaption>{short_credit('beach_aerial')}</figcaption></figure>
  <p class="note">{e(t['updated_label'])}: {C['updated']}</p>
</div></section>
"""
            + footer(lang))


def main():
    for lang in LANGS:
        d = ROOT if lang == "en" else os.path.join(ROOT, lang)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(lang))
    for g in C.get("guides", []):
        for lang in LANGS:
            d = os.path.join(ROOT, g["slug"]) if lang == "en" else os.path.join(ROOT, lang, g["slug"])
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(guide_page(lang, g))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for lang in LANGS:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{hl(l)}" href="{url(l)}"/>' for l in LANGS)
        sm.append(f"<url><loc>{url(lang)}</loc><lastmod>{C['updated']}</lastmod>{alts}</url>")
    for g in C.get("guides", []):
        for lang in LANGS:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{hl(l)}" href="{gurl(l, g["slug"])}"/>' for l in LANGS)
            sm.append(f"<url><loc>{gurl(lang, g['slug'])}</loc><lastmod>{g['updated']}</lastmod>{alts}</url>")
    sm.append("</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm))
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("OK:", ", ".join(LANGS))


if __name__ == "__main__":
    main()
