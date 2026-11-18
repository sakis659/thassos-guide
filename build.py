#!/usr/bin/env python3
"""Φτιάχνει το site από το content.json:  / (αγγλικά), /el/, /ro/, /bg/, /de/, /tr/, sitemap.xml, robots.txt
Τρέξε: python3 build.py"""
import json, os, html
from urllib.parse import quote

ROOT = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(ROOT, "content.json"), encoding="utf-8"))
SITE, LANGS, P = C["site"], C["languages"], C["photos"]
e = lambda s: html.escape(str(s), quote=True)


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
:root{--sea:#0b4f6c;--deep:#062a3a;--emerald:#0f8b6f;--sand:#f6f1e7;--marble:#fbfaf7;--ink:#14212b;--muted:#5d6b75;--gold:#d9a441}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans",Arial,sans-serif;color:var(--ink);background:var(--marble);line-height:1.65}
h1,h2,h3{font-family:Georgia,"Times New Roman",serif;line-height:1.15;letter-spacing:-.01em}
a{color:var(--sea)}
.wrap{max-width:1120px;margin:0 auto;padding:0 22px}
header.top{position:absolute;top:0;left:0;right:0;z-index:20}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;height:70px;gap:16px}
.brand{color:#fff;font-family:Georgia,serif;font-size:1.3rem;font-weight:700;text-decoration:none;display:flex;align-items:center;gap:10px}
.brand i{width:30px;height:30px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#5fd3b3,var(--emerald) 60%,var(--deep));display:inline-block;box-shadow:0 0 0 3px #ffffff40}
nav.links{display:flex;gap:20px}
nav.links a{color:#ffffffdd;text-decoration:none;font-size:.93rem}
nav.links a:hover{color:#fff}
.langsel{position:relative}
.langsel select{appearance:none;background:#ffffff22;color:#fff;border:1px solid #ffffff55;border-radius:999px;padding:7px 30px 7px 14px;font-size:.88rem;cursor:pointer;backdrop-filter:blur(6px)}
.langsel select option{color:#14212b}
.langsel:after{content:"▾";position:absolute;right:12px;top:50%;transform:translateY(-50%);color:#fff;pointer-events:none;font-size:.8rem}
@media(max-width:860px){nav.links{display:none}}
.hero{position:relative;min-height:88vh;display:flex;align-items:flex-end;color:#fff;
 background:linear-gradient(180deg,#06293a55 0%,#06293a33 40%,#062a3ae6 100%),var(--hero) center/cover no-repeat,linear-gradient(135deg,#0b4f6c,#0f8b6f)}
.hero .wrap{padding-bottom:70px;padding-top:120px}
.kicker{display:inline-block;font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;background:#ffffff26;border:1px solid #ffffff4d;padding:6px 14px;border-radius:999px;backdrop-filter:blur(6px)}
.hero h1{font-size:clamp(2.6rem,7vw,5rem);margin:18px 0 14px;max-width:820px;text-shadow:0 2px 30px #0006}
.hero p{font-size:clamp(1.05rem,2vw,1.3rem);max-width:640px;color:#ffffffe6}
.btn{display:inline-block;margin-top:28px;background:var(--gold);color:#1e1503;font-weight:700;padding:14px 26px;border-radius:12px;text-decoration:none}
.btn:hover{background:#e6b65a}
.credit{position:absolute;right:14px;top:78px;font-size:.7rem;color:#ffffffaa}
.credit a{color:#ffffffcc}
.facts{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:-46px;position:relative;z-index:5}
@media(max-width:760px){.facts{grid-template-columns:repeat(2,1fr)}}
.fact{background:#fff;border-radius:18px;padding:20px 22px;box-shadow:0 14px 40px -18px #062a3a55;border:1px solid #e8e2d6}
.fact .ic{font-size:1.4rem}.fact b{display:block;font-size:1.25rem;margin-top:6px;font-family:Georgia,serif}.fact span{color:var(--muted);font-size:.9rem}
section{padding:80px 0 10px}
.sh{display:flex;align-items:center;gap:14px;margin-bottom:26px}
.sh:before{content:"";width:34px;height:3px;background:var(--emerald);border-radius:3px}
h2{font-size:clamp(1.8rem,4vw,2.6rem)}
.routes{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
@media(max-width:860px){.routes{grid-template-columns:1fr}}
.route{background:var(--sand);border-radius:18px;padding:24px;border:1px solid #ebe3d2}
.route h3{font-size:1.2rem;color:var(--sea);margin-bottom:8px}
.note{margin-top:16px;font-size:.92rem;color:var(--muted);border-left:3px solid var(--gold);padding-left:12px}
.around{margin-top:34px;display:grid;grid-template-columns:1.2fr 1fr;gap:26px;align-items:center}
@media(max-width:860px){.around{grid-template-columns:1fr}}
.around img{width:100%;border-radius:18px;aspect-ratio:16/10;object-fit:cover;background:linear-gradient(135deg,#cfe7dc,#9fd0c0)}
.around h3{font-size:1.5rem;margin-bottom:10px}
figure{margin:0}
img{display:block}figcaption{font-size:.72rem;color:var(--muted);margin-top:6px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px}
.card{border-radius:18px;padding:22px;color:#fff;min-height:190px;display:flex;flex-direction:column;justify-content:flex-end;position:relative;overflow:hidden}
.card:nth-child(1){background:linear-gradient(160deg,#16a6a0,#0b4f6c)}
.card:nth-child(2){background:linear-gradient(160deg,#9fd8cf,#2a8f86)}
.card:nth-child(3){background:linear-gradient(160deg,#e6c27a,#c08a2e)}
.card:nth-child(4){background:linear-gradient(160deg,#4fa37a,#1d5a46)}
.card:nth-child(5){background:linear-gradient(160deg,#7fb6d6,#2d5f86)}
.card:after{content:"";position:absolute;right:-40px;top:-40px;width:140px;height:140px;border-radius:50%;border:2px solid #ffffff33}
.card h3{font-size:1.25rem;margin-bottom:6px}.card p{font-size:.93rem;color:#ffffffe6}
.vgrid{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:start}
@media(max-width:860px){.vgrid{grid-template-columns:1fr}}
.vlist{list-style:none;display:grid;gap:12px}
.vlist li{background:#fff;border:1px solid #e8e2d6;border-radius:16px;padding:18px 20px}
.vlist b{display:block;font-family:Georgia,serif;font-size:1.12rem;color:var(--sea)}
.vlist span{color:#3c4a54;font-size:.95rem}
.vgrid img{width:100%;border-radius:18px;aspect-ratio:4/3;object-fit:cover;background:linear-gradient(135deg,#d8e6ee,#9db8c8)}
.tips{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:760px){.tips{grid-template-columns:1fr}}
.tips li{background:var(--sand);border-radius:16px;padding:18px 20px 18px 50px;position:relative;border:1px solid #ebe3d2}
.tips li:before{content:"✓";position:absolute;left:18px;top:17px;width:22px;height:22px;border-radius:50%;background:var(--emerald);color:#fff;font-size:.8rem;display:grid;place-items:center}
.space{margin-top:50px;border-radius:22px;overflow:hidden;position:relative;background:#062a3a}
.space img{width:100%;max-height:420px;object-fit:cover;display:block;opacity:.9}
footer{margin-top:80px;background:var(--deep);color:#c9d6dd;padding:44px 0;font-size:.88rem}
footer a{color:#fff}
footer .cols{display:grid;grid-template-columns:1fr 1fr;gap:30px}
@media(max-width:760px){footer .cols{grid-template-columns:1fr}}
footer h4{color:#fff;font-family:Georgia,serif;font-size:1.05rem;margin-bottom:10px}
footer ul{list-style:none;display:grid;gap:6px}
.langs a{margin-right:12px;color:#c9d6dd}
.glist{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px}
.gcard{display:block;text-decoration:none;color:var(--ink);background:#fff;border:1px solid #e8e2d6;border-radius:18px;overflow:hidden;transition:.2s}
.gcard:hover{transform:translateY(-3px);box-shadow:0 14px 40px -18px #062a3a55}
.gcard .ph{height:170px;background:var(--ph) center/cover no-repeat,linear-gradient(135deg,#16a6a0,#0b4f6c)}
.gcard .tx{padding:18px 20px}.gcard h3{font-size:1.15rem;color:var(--sea);margin-bottom:6px}.gcard p{font-size:.92rem;color:#3c4a54}
.gcard .more{display:inline-block;margin-top:10px;font-weight:600;color:var(--emerald)}
.ghero{position:relative;min-height:62vh;display:flex;align-items:flex-end;color:#fff;
 background:linear-gradient(180deg,#06293a66 0%,#06293a22 40%,#062a3ae6 100%),var(--hero) center/cover no-repeat,linear-gradient(135deg,#0b4f6c,#0f8b6f)}
.ghero .wrap{padding-bottom:50px;padding-top:110px}.ghero h1{font-size:clamp(2.2rem,6vw,4rem);margin-top:14px;text-shadow:0 2px 30px #0006}
.article{max-width:760px;margin:0 auto;padding:50px 22px 0}
.article .lead{font-size:1.18rem;color:#2b3a44;margin-bottom:30px}
.article h2{font-size:1.6rem;margin:34px 0 10px;color:var(--sea)}
.article p{font-size:1.04rem;color:#2b3a44}
.tipbox{margin-top:40px;background:var(--sand);border:1px solid #ebe3d2;border-radius:18px;padding:24px 26px}
.tipbox h3{font-size:1.2rem;margin-bottom:10px}.tipbox ul{margin-left:20px;display:grid;gap:8px}
.srcs{margin-top:30px;font-size:.88rem;color:var(--muted)}.srcs a{margin-right:10px}
.backl{display:inline-block;margin-top:30px;font-weight:600;text-decoration:none}
"""


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
<html lang="{lang}">
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
<meta property="og:url" content="{canon}"><meta property="og:locale" content="{lang}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='30' fill='%230f8b6f'/%3E%3Cpath d='M10 40c8-6 14-6 22 0s14 6 22 0' stroke='%23fff' stroke-width='5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E">
<style>{CSS}</style>"""


def topbar(lang, opts_for):
    t = C["i18n"][lang]
    opts = "".join(f'<option value="{opts_for(l)}"{" selected" if l == lang else ""}>{e(C["i18n"][l]["name"])}</option>' for l in LANGS)
    return f"""<header class="top"><div class="wrap">
  <a class="brand" href="{path(lang)}"><i></i>{e(t['brand'])}</a>
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
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{gurl(l, g["slug"])}">' for l in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{gurl("en", g["slug"])}">'
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": gt["h1"], "description": gt["description"],
          "inLanguage": lang, "dateModified": g["updated"], "image": img(g["photo"], 1200), "mainEntityOfPage": gurl(lang, g["slug"])}
    secs = "".join(f"<h2>{e(h)}</h2><p>{e(p)}</p>" for h, p in gt["sections"])
    tips = "".join(f"<li>{e(x)}</li>" for x in gt["tips"])
    srcs = " ".join(f'<a href="{e(s["url"])}" target="_blank" rel="noopener">{e(s["name"])}</a>' for s in g["sources"])
    return (head(lang, gt["title"], gt["description"], gurl(lang, g["slug"]), alts, img(g["photo"], 1200))
            + f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head><body>'
            + topbar(lang, lambda l: gpath(l, g["slug"]))
            + f"""<section class="ghero" style="--hero:url('{img(g['photo'])}')"><div class="wrap">
  <span class="kicker">{e(t['hero_kicker'])}</span><h1>{e(gt['h1'])}</h1></div>
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
                    f'<span class="more">{e(t["read"])} →</span></div></a>' for g in gs)
    return f'<section id="guides"><div class="wrap"><div class="sh"><h2>{e(t["guides_h"])}</h2></div><div class="glist">{cards}</div></div></section>'


def page(lang):
    t = C["i18n"][lang]
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{url(l)}">' for l in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{url("en")}">'
    opts = "".join(f'<option value="{path(l)}"{" selected" if l == lang else ""}>{e(C["i18n"][l]["name"])}</option>' for l in LANGS)
    facts = "".join(f'<div class="fact"><div class="ic">{a}</div><b>{e(b)}</b><span>{e(c)}</span></div>' for a, b, c in t["facts"])
    routes = "".join(f'<div class="route"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in t["getting"])
    beaches = "".join(f'<div class="card"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in t["beaches"])
    vill = "".join(f'<li><b>{e(h)}</b><span>{e(p)}</span></li>' for h, p in t["villages"])
    tips = "".join(f"<li>{e(x)}</li>" for x in t["tips"])
    ld = {"@context": "https://schema.org", "@type": "TouristDestination", "name": "Thassos", "url": url(lang),
          "description": t["description"], "image": img("giola", 1200), "inLanguage": lang,
          "geo": {"@type": "GeoCoordinates", "latitude": 40.68, "longitude": 24.65}}
    nav = t["nav"]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['description'])}">
<meta name="google-site-verification" content="bIGBCT5ZKMfr6wYTzHqtlYJxI6Z6y_axiCzH9b8dbJc" />
<link rel="canonical" href="{url(lang)}">
{alts}
<meta property="og:type" content="website"><meta property="og:title" content="{e(t['title'])}">
<meta property="og:description" content="{e(t['description'])}"><meta property="og:image" content="{img('sunrise', 1200)}">
<meta property="og:url" content="{url(lang)}"><meta property="og:locale" content="{lang}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='30' fill='%230f8b6f'/%3E%3Cpath d='M10 40c8-6 14-6 22 0s14 6 22 0' stroke='%23fff' stroke-width='5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="{path(lang)}"><i></i>{e(t['brand'])}</a>
  <nav class="links"><a href="#getting">{e(nav['getting'])}</a><a href="#beaches">{e(nav['beaches'])}</a><a href="#villages">{e(nav['villages'])}</a><a href="#guides">{e(C['i18n'][lang]['guides_h'])}</a><a href="#tips">{e(nav['tips'])}</a></nav>
  <label class="langsel" aria-label="{e(t['lang_label'])}"><select onchange="location.href=this.value">{opts}</select></label>
</div></header>

<section class="hero" style="--hero:url('{img('sunrise', 2000)}')">
  <div class="wrap">
    <span class="kicker">{e(t['hero_kicker'])}</span>
    <h1>{e(t['hero_title'])}</h1>
    <p>{e(t['hero_sub'])}</p>
    <a class="btn" href="#getting">{e(t['cta'])} →</a>
  </div>
  <div class="credit">{short_credit('sunrise')}</div>
</section>

<div class="wrap"><div class="facts">{facts}</div></div>

<section id="getting"><div class="wrap">
  <div class="sh"><h2>{e(t['getting_h'])}</h2></div>
  <div class="routes">{routes}</div>
  <p class="note">{e(t['getting_note'])}</p>
  <div class="around">
    <div><h3>{e(t['around_h'])}</h3><p>{e(t['around'])}</p></div>
    <figure><img loading="lazy" src="{img('village', 1200)}" alt="Mountain village on Thassos"><figcaption>{short_credit('village')}</figcaption></figure>
  </div>
</div></section>

<section id="beaches"><div class="wrap">
  <div class="sh"><h2>{e(t['beaches_h'])}</h2></div>
  <div class="cards">{beaches}</div>
</div></section>

<section id="villages"><div class="wrap">
  <div class="sh"><h2>{e(t['villages_h'])}</h2></div>
  <div class="vgrid">
    <ul class="vlist">{vill}</ul>
    <figure><img loading="lazy" src="{img('theologos', 1200)}" alt="Theologos village, Thassos"><figcaption>Theologos · {short_credit('theologos')}</figcaption></figure>
  </div>
</div></section>

{guides_html(lang)}
<section id="tips"><div class="wrap">
  <div class="sh"><h2>{e(t['tips_h'])}</h2></div>
  <ul class="tips">{tips}</ul>
  <figure class="space"><img loading="lazy" src="{img('beach_aerial', 1800)}" alt="Aerial view of a beach on Thassos"></figure>
  <figcaption>{short_credit('beach_aerial')}</figcaption>
</div></section>

<footer><div class="wrap cols">
  <div>
    <h4>{e(t['brand'])}</h4>
    <p>{e(t['disclaimer'])}</p>
    <p style="margin-top:10px">{e(t['updated_label'])}: {C['updated']}</p>
    <p class="langs" style="margin-top:14px">{''.join(f'<a href="{path(l)}">{e(C["i18n"][l]["name"])}</a>' for l in LANGS)}</p>
  </div>
  <div>
    <h4>{e(t['photo_credits'])}</h4>
    <ul>{''.join(f'<li>{credit(k)}</li>' for k in P)}</ul>
  </div>
</div></footer>
</body></html>
"""


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
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url(l)}"/>' for l in LANGS)
        sm.append(f"<url><loc>{url(lang)}</loc><lastmod>{C['updated']}</lastmod>{alts}</url>")
    for g in C.get("guides", []):
        for lang in LANGS:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{gurl(l, g["slug"])}"/>' for l in LANGS)
            sm.append(f"<url><loc>{gurl(lang, g['slug'])}</loc><lastmod>{g['updated']}</lastmod>{alts}</url>")
    sm.append("</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm))
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("OK:", ", ".join(LANGS))


if __name__ == "__main__":
    main()
