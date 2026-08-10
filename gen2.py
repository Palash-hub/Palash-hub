#!/usr/bin/env python3
import os, pyfiglet

OUT = "/mnt/user-data/outputs"
ASSETS = os.path.join(OUT, "assets")
os.makedirs(ASSETS, exist_ok=True)

# ---------- ASCII helpers ----------
def pad(s, w): return s + " " * (w - len(s))

def ascii_table(headers, rows):
    cols = len(headers)
    widths = [len(headers[i]) for i in range(cols)]
    for r in rows:
        for i in range(cols):
            widths[i] = max(widths[i], len(r[i]))
    def seg(l, m, r, f): return l + m.join(f * (widths[i] + 2) for i in range(cols)) + r
    def row(c): return "│" + "│".join(" " + pad(c[i], widths[i]) + " " for i in range(cols)) + "│"
    out = [seg("┌", "┬", "┐", "─"), row(headers), seg("├", "┼", "┤", "─")]
    for r in rows: out.append(row(r))
    out.append(seg("└", "┴", "┘", "─"))
    return out

def box(rows):
    w = max(len(r) for r in rows)
    out = ["┌" + "─" * (w + 2) + "┐"]
    for r in rows: out.append("│ " + pad(r, w) + " │")
    out.append("└" + "─" * (w + 2) + "┘")
    return out

def barline(label, pct, lblw, cells=22):
    fill = round(pct / 100 * cells)
    return f"{pad(label, lblw)}  {'━'*fill}{'─'*(cells-fill)}  {pct}%"

# ---------- content ----------
banner = pyfiglet.figlet_format("PAVEL", font="ansi_shadow").rstrip("\n").split("\n")

about = box([
    "OS      Arch Linux x86_64  (btw)",
    "Role    backend & ML  ·  СПбГУТ '26",
    "Lang    C#/.NET  ·  Python вторым номером",
    "Now     metrics service · матстат · JMLC->ИТМО",
    "Off     кино · стихи · манга · modded MC over LAN",
])

skills = [("C# / .NET", 82), ("ASP.NET Core", 76), ("EF Core / SQL", 70),
          ("Python · ML/data", 66), ("Go", 32), ("Arch ricing", 94)]
lblw = max(len(l) for l, _ in skills)
skill_lines = [barline(l, p, lblw) for l, p in skills]

projects = ascii_table(
    ["repo", "описание", "стек"],
    [["MOCChecker", "проверка ссылок в Obsidian", "C#"],
     ["nfad", "детектор сетевых аномалий", "Python · XGBoost"],
     ["MiniBank", "учебный банковский движок", "C# · Clean Arch"]])

contacts = ascii_table(
    ["ch", "addr"],
    [["tg", "t.me/username"],
     ["email", "you@example.com"],
     ["hh", "hh.ru/resume/xxxxxxxx"]])

# ---------- small animated SVG accents (transparent, theme-safe colors) ----------
AMBER = "#d97706"; GREEN = "#16a34a"; RED = "#e5484d"; MUT = "#6b7280"
FONT = "font-family=\"'DejaVu Sans Mono','Courier New',monospace\""

def write(name, svg):
    with open(os.path.join(ASSETS, name), "w") as f: f.write(svg)

# blinking prompt cursor line
write("prompt.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="26" viewBox="0 0 300 26" {FONT}>
<text x="0" y="19" font-size="15" fill="{AMBER}">pavel@arch</text>
<text x="92" y="19" font-size="15" fill="{MUT}">:~$</text>
<rect x="132" y="6" width="10" height="16" fill="{AMBER}">
<animate attributeName="opacity" values="1;0" keyTimes="0;0.5" dur="1s" calcMode="discrete" repeatCount="indefinite"/></rect>
</svg>''')

# online chip
write("online.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="140" height="26" viewBox="0 0 140 26" {FONT}>
<circle cx="10" cy="13" r="6" fill="{GREEN}">
<animate attributeName="opacity" values="1;0.2;1" dur="1.3s" repeatCount="indefinite"/></circle>
<text x="26" y="18" font-size="14" fill="{AMBER}">ONLINE</text>
</svg>''')

# sync spinner
write("spinner.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="120" height="26" viewBox="0 0 120 26" {FONT}>
<g transform="translate(11,13)">
<circle r="8" fill="none" stroke="{MUT}" stroke-width="2" stroke-opacity="0.35"/>
<path d="M0 -8 A 8 8 0 0 1 8 0" fill="none" stroke="{AMBER}" stroke-width="2" stroke-linecap="round">
<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="0.9s" repeatCount="indefinite"/></path>
</g>
<text x="28" y="18" font-size="14" fill="{MUT}">SYNC</text>
</svg>''')

# scrolling ops ticker
write("ticker.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="30" viewBox="0 0 760 30" {FONT}>
<defs><clipPath id="c"><rect x="0" y="0" width="760" height="30"/></clipPath></defs>
<g clip-path="url(#c)"><g>
<text x="0" y="20" font-size="14" fill="{MUT}">
<tspan fill="{AMBER}">CURRENT_OPS //</tspan>
<tspan dx="10">metrics-ingestion service (.NET 10 · Aspire · TimescaleDB)</tspan>
<tspan dx="12">·</tspan><tspan dx="12">поступление в магистратуру '26</tspan>
<tspan dx="12">·</tspan><tspan dx="12" fill="{GREEN}">JMLC 2026 -&gt; AI Talent Hub ИТМО</tspan>
<tspan dx="12">·</tspan><tspan dx="12">пробтеория &amp; матстат</tspan><tspan dx="24">///</tspan></text>
<animateTransform attributeName="transform" type="translate" from="760 0" to="-1120 0" dur="24s" repeatCount="indefinite"/>
</g></g></svg>''')

# ---------- assemble README ----------
def block(cmd, lines):
    body = "\n".join(lines)
    return f"```text\npavel@arch:~$ {cmd}\n{body}\n```"

readme = []
readme.append("```text\n" + "\n".join(banner) + "\n\n  C#/.NET backend  ·  ML practitioner  ·  Arch Linux\n  СПбГУТ '26  ·  Санкт-Петербург\n```")
readme.append('<img src="assets/online.svg" height="22" alt="online"/> &nbsp; <img src="assets/prompt.svg" height="22" alt="prompt"/>')
readme.append(block("neofetch", about))
readme.append(block("./skills --self-assessment", ["// самооценка, не сертификат. Go честно отстаёт.", ""] + skill_lines))
readme.append('<img src="assets/spinner.svg" height="22" alt="sync"/>')
readme.append(block("ls ./projects", projects))
readme.append('<sub>↳ open: <a href="https://github.com/Palash-hub/MOCChecker">MOCChecker</a> · nfad <em>(поправь ссылку)</em> · MiniBank <em>(поправь ссылку)</em></sub>')
readme.append(block("cat contacts.txt", contacts))
readme.append('<sub>↳ write: <a href="https://t.me/username">Telegram</a> · <a href="mailto:you@example.com">Email</a> · <a href="https://hh.ru/resume/xxxxxxxx">hh.ru</a></sub>')
readme.append('<img src="assets/ticker.svg" height="26" alt="current ops"/>')

with open(os.path.join(OUT, "README.md"), "w") as f:
    f.write("\n\n".join(readme) + "\n")

print("done. assets:", sorted(os.listdir(ASSETS)))
