#!/usr/bin/env python3
"""Export options.json (from ifr_analyze.py) to CSV, Markdown and XLSX.

Usage: python3 export.py <options.json> <output_dir> [title]
Writes: options.csv, HIDDEN_OPTIONS.md (+ hidden/*.md), HIGHLIGHTS.md, options.xlsx
"""
import csv, json, os, re, sys
from collections import Counter, OrderedDict

if len(sys.argv) < 3:
    sys.exit(__doc__)
rows = json.load(open(sys.argv[1]))
out = sys.argv[2]
title = sys.argv[3] if len(sys.argv) > 3 else 'AMI Aptio V Setup options'
os.makedirs(out, exist_ok=True)
rows.sort(key=lambda r: (r['category'], r['menu']))

COLS = ['category', 'menu', 'option', 'type', 'values', 'default', 'varstore', 'offset', 'size', 'help', 'condition']
HEAD = ['Category', 'Menu', 'Option', 'Type', 'Values', 'Default (IFR)', 'VarStore', 'Offset', 'Size (bytes)', 'Help text', 'Visibility condition']

# ---------- CSV ----------
with open(os.path.join(out, 'options.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(HEAD)
    for r in rows:
        w.writerow([r[k] for k in COLS])

# ---------- Markdown ----------
def cell(s, n=None):
    s = str(s).replace('|', '\\|').replace('\n', ' ')
    return s if n is None or len(s) <= n else s[:n - 1] + '…'

HIGHLIGHT = re.compile(
    r'^(CFG Lock|Overclocking Lock|Power Limit [124]( Time Window| Override| Lock)?|Turbo Mode|Core Voltage Offset|'
    r'Offset Prefix|Core Max OC Ratio|GT Voltage Offset|Uncore Voltage Offset|Tcc Activation Offset|BIOS Lock|'
    r'Flash Protection Range Registers \(FPRR\)|ME State|Software Guard Extensions \(SGX\)|Above 4GB MMIO BIOS assignment|'
    r'Primary Display|Internal Graphics|DVMT Pre-Allocated|Aperture Size|DGPU Power Enable|CPU Fan Speed|'
    r'Critical Trip Points?|Intel\(R\) Dynamic Tuning|Hyper-Threading|VT-d|Intel Virtualization Technology|'
    r'C-State Auto Demotion|Package C State Limit|Enhanced C-states|Intel\(R\) SpeedStep\(tm\)|Ring Down Bin)$', re.I)


def table(items, with_cat=False):
    lines = ['| ' + ('Category | ' if with_cat else '') + 'Menu | Option | Values | Default | VarStore @ offset (size) |',
             '|' + ('---|' if with_cat else '') + '---|---|---|---|---|']
    for r in items:
        lines.append('| ' + (cell(r['category'][3:]) + ' | ' if with_cat else '') +
                     f"{cell(r['menu'])} | {cell(r['option'])} | {cell(r['values'], 140)} | {cell(r['default'])} | "
                     f"`{r['varstore']}` @ `{r['offset']}` ({r['size']}) |")
    return lines


cnt = Counter(r['category'] for r in rows)
hidden_dir = os.path.join(out, 'hidden')
os.makedirs(hidden_dir, exist_ok=True)
index = [f'# {title} - hidden options', '',
         'One file per menu (GitHub does not render very large Markdown files).',
         'Values longer than 140 characters are truncated; `options.csv` has the full data.', '']
for cat in sorted(c for c in cnt if c[0] in '34'):
    index += [f'## {cat[3:]} ({cnt[cat]} options)', '', '| Menu | Options |', '|---|---|']
    groups = OrderedDict()
    for r in rows:
        if r['category'] == cat:
            groups.setdefault(' > '.join(r['menu'].split(' > ')[:2]), []).append(r)
    for g, items in groups.items():
        slug = cat[0] + '-' + re.sub(r'[^a-z0-9]+', '-', g.lower()).strip('-')
        open(os.path.join(hidden_dir, slug + '.md'), 'w', encoding='utf-8').write('\n'.join(
            [f'# {g}', '', f'Category: **{cat[3:]}** - {len(items)} options', '', '[Back to index](../HIDDEN_OPTIONS.md)', '']
            + table(items)) + '\n')
        index.append(f'| [{cell(g)}](hidden/{slug}.md) | {len(items)} |')
    index.append('')
open(os.path.join(out, 'HIDDEN_OPTIONS.md'), 'w', encoding='utf-8').write('\n'.join(index))

seen, hl = set(), []
for r in rows:
    if r['category'][0] in '34' and HIGHLIGHT.search(r['option']) and (r['option'], r['menu']) not in seen:
        seen.add((r['option'], r['menu']))
        hl.append(r)
open(os.path.join(out, 'HIGHLIGHTS.md'), 'w', encoding='utf-8').write('\n'.join(
    [f'# {title} - notable hidden options', '',
     'A hand-picked subset (power limits, voltage offsets, locks, thermal, graphics, security).', ''] +
    table(hl, with_cat=True)) + '\n')

# ---------- XLSX ----------
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
FONT = 'Arial'
FILL = {'1': 'E2EFDA', '2': 'FFF2CC', '3': 'FCE4D6', '4': 'D9D9D9'}
WIDTH = [32, 48, 40, 11, 60, 22, 22, 9, 10, 70, 60]
hf, hfill = Font(name=FONT, bold=True, color='FFFFFF'), PatternFill('solid', fgColor='1F3864')
wb = Workbook()
summary = wb.active
summary.title = 'Summary'


def sheet(ws, data):
    ws.append(HEAD)
    for c in ws[1]:
        c.font, c.fill, c.alignment = hf, hfill, Alignment(vertical='center', wrap_text=True)
    for r in data:
        ws.append([r[k] for k in COLS])
        for c in ws[ws.max_row]:
            c.font = Font(name=FONT, size=9)
        ws.cell(ws.max_row, 1).fill = PatternFill('solid', fgColor=FILL[r['category'][0]])
    for i, wd in enumerate(WIDTH, 1):
        ws.column_dimensions[get_column_letter(i)].width = wd
    ws.freeze_panes = 'D2'
    ws.auto_filter.ref = ws.dimensions


sheet(wb.create_sheet('Options'), rows)
sheet(wb.create_sheet('Highlights'), hl)
summary['A1'] = title
summary['A1'].font = Font(name=FONT, bold=True, size=14)
summary['A3'], summary['B3'] = 'Category', 'Options'
for c in (summary['A3'], summary['B3']):
    c.font, c.fill = hf, hfill
cats = sorted(cnt)
for i, c in enumerate(cats, 4):
    summary.cell(i, 1, c).fill = PatternFill('solid', fgColor=FILL[c[0]])
    summary.cell(i, 2, f'=COUNTIF(Options!A:A,A{i})')
n = 4 + len(cats)
summary.cell(n, 1, 'Total')
summary.cell(n, 2, f'=SUM(B4:B{n - 1})')
notes = ['', 'Categories',
         '1. Visible: shown in the stock menu.',
         '2. Conditional: shown or not depending on detected hardware or another setting.',
         '3. Hidden - MSI advanced menu: suppressed while the MSIHiddenFun variable = 1 (factory state).',
         '4. Hidden - permanently: "SuppressIf TRUE" (Chipset tab) or forms not linked from any menu.',
         '', 'Caveats',
         '"Default (IFR)" is the default coded in the form; the value active on a machine lives in NVRAM.',
         'A raw number as default on a list means the default is defined elsewhere (AMI default variables).',
         'VarStore + Offset + Size locate the option inside its UEFI variable.']
for j, t in enumerate(notes, n + 1):
    summary.cell(j, 1, t)
for row in summary.iter_rows(min_row=3, max_row=summary.max_row):
    for c in row:
        c.font = Font(name=FONT, bold=c.font.bold or c.value in ('Total', 'Categories', 'Caveats'), color=c.font.color)
summary.column_dimensions['A'].width = 50
summary.column_dimensions['B'].width = 12
wb.save(os.path.join(out, 'options.xlsx'))
print(f'{len(rows)} options | {len(hl)} highlights -> {out}')
