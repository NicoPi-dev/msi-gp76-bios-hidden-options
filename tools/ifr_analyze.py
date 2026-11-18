#!/usr/bin/env python3
"""Decode the IFR forms of an AMI Aptio V "Setup" driver and classify every
option by visibility.

Usage: python3 ifr_analyze.py <Setup.efi> <options.json>

The HII form package and the en-US string package are located automatically.
Each option is evaluated in two states:
  - stock     : MSIHiddenFun = 1 (MSI advanced menu hidden), SystemAccess = 0 (admin)
  - unlocked  : MSIHiddenFun = 0
Other conditions (hardware presence, other settings) use three-valued logic:
an unknown result marks the option as "conditional".
"""
import sys, struct, json
from collections import deque

if len(sys.argv) != 3:
    sys.exit(__doc__)
data = open(sys.argv[1], 'rb').read()
OUT = sys.argv[2]


def find_packages(d):
    """Return (form_package_offset, en-US_string_package_offset)."""
    forms, strs = [], []
    for i in range(len(d) - 0x40):
        t = d[i + 3]
        if t not in (0x02, 0x04):
            continue
        ln = d[i] | d[i + 1] << 8 | d[i + 2] << 16
        if not (0x40 < ln <= len(d) - i):
            continue
        if t == 0x02 and d[i + 4] == 0x0E and (d[i + 5] & 0x7F) >= 0x18:
            forms.append((ln, i))
        elif t == 0x04:
            hs, so = struct.unpack_from('<II', d, i + 4)
            if hs == so and 0x30 <= hs < 0x60 and d[i + 0x2E:i + hs].split(b'\0')[0] == b'en-US':
                strs.append((ln, i))
    if not forms or not strs:
        sys.exit('HII form or en-US string package not found')
    return max(forms)[1], max(strs)[1]


FORM_OFF, STR_OFF = find_packages(data)
print(f'Form package @ {FORM_OFF:#x} | en-US strings @ {STR_OFF:#x}')

u8 = lambda o: data[o]
u16 = lambda o: struct.unpack_from('<H', data, o)[0]
u32 = lambda o: struct.unpack_from('<I', data, o)[0]
u64 = lambda o: struct.unpack_from('<Q', data, o)[0]
RD = {0: u8, 1: u16, 2: u32, 3: u64}

# ---------- strings ----------
strings, sid = {}, 1
p = STR_OFF + u32(STR_OFF + 4)
def rdz(p):
    e = p
    while data[e:e+2] != b'\0\0': e += 2
    return data[p:e].decode('utf-16-le', 'replace'), e + 2
while True:
    bt = data[p]; p += 1
    if bt == 0x00: break
    if bt == 0x14: strings[sid], p = rdz(p); sid += 1
    elif bt == 0x16:
        n = u16(p); p += 2
        for _ in range(n): strings[sid], p = rdz(p); sid += 1
    elif bt == 0x20: p += 2; sid += 1
    elif bt == 0x21: sid += u16(p); p += 2
    elif bt == 0x22: sid += data[p]; p += 1
    else: raise SystemExit(f'unknown string block {bt:#x}')
S = lambda i: strings.get(i, '').strip()

# ---------- IFR pass ----------
end = FORM_OFF + (data[FORM_OFF] | data[FORM_OFF+1] << 8 | data[FORM_OFF+2] << 16)
p = FORM_OFF + 4
varstores, forms, questions = {}, {}, []
stack, conds = [], []          # conds: list of (kind, tokens)
cur_form = cur_q = None
QOPS = {0x05: 'OneOf', 0x06: 'CheckBox', 0x07: 'Numeric', 0x08: 'Password', 0x1C: 'String', 0x0C: 'Action'}

while p < end:
    op = data[p]; ln = data[p+1] & 0x7F; scope = data[p+1] >> 7; b = p + 2
    if ln < 2: break
    if op == 0x24:
        varstores[u16(b+16)] = data[b+20:p+ln].split(b'\0')[0].decode()
    elif op == 0x26:
        varstores[u16(b)] = data[b+24:p+ln].split(b'\0')[0].decode()
    elif op == 0x01:
        cur_form = {'id': u16(b), 'title': S(u16(b+2)), 'refs': [], 'qs': []}
        forms[cur_form['id']] = cur_form
    elif op == 0x0F and cur_form is not None and ln >= 15:
        cur_form['refs'].append((u16(b+11), [list(c) for c in conds], S(u16(b))))
    elif op in QOPS:
        q = {'type': QOPS[op], 'prompt': S(u16(b)), 'help': S(u16(b+2)), 'qid': u16(b+4),
             'varstore': varstores.get(u16(b+6), '') if u16(b+6) else '', 'offset': u16(b+8),
             'size': 1, 'options': [], 'default': None, 'conds': [list(c) for c in conds],
             'form': cur_form['id'] if cur_form else None}
        if op in (0x05, 0x07):
            fl = data[b+11]; q['size'] = 1 << (fl & 3); r = RD[fl & 3]; s = q['size']
            q['min'], q['max'], q['step'] = r(b+12), r(b+12+s), r(b+12+2*s)
        if op == 0x06: q['default'] = 'Enabled' if data[b+11] & 1 else 'Disabled'
        if op == 0x08: q['size'] = None
        questions.append(q)
        if cur_form is not None: cur_form['qs'].append(q)
        cur_q = q if scope else None
    elif op == 0x09 and cur_q is not None:
        v = RD.get(data[b+3], u8)(b+4); t = S(u16(b))
        cur_q['options'].append((v, t))
        if data[b+2] & 0x30: cur_q['default'] = t
    elif op == 0x5B and cur_q is not None and u16(b) == 0:
        v = RD.get(data[b+2], u8)(b+3)
        cur_q['default'] = next((t for vv, t in cur_q['options'] if vv == v), v) if cur_q['options'] else v
    elif op in (0x0A, 0x19, 0x30):
        conds.append(({0x0A: 'S', 0x19: 'G', 0x30: 'S'}[op], []))
    elif op == 0x12 and conds: conds[-1][1].append(('eq', u16(b), [u16(b+2)]))
    elif op == 0x14 and conds:
        n = u16(b+2); conds[-1][1].append(('eq', u16(b), [u16(b+4+2*i) for i in range(n)]))
    elif op == 0x13 and conds: conds[-1][1].append(('unk',))
    elif op in (0x15, 0x16, 0x17, 0x46, 0x47) and conds:
        conds[-1][1].append({0x15: 'AND', 0x16: 'OR', 0x17: 'NOT', 0x46: 'T', 0x47: 'F'}[op])
    elif conds and stack and stack[-1] in (0x0A, 0x19, 0x30) and op not in (0x29,) and op not in QOPS \
            and op not in (0x01, 0x02, 0x03, 0x0F, 0x09, 0x5B, 0x0A, 0x19, 0x30):
        # unhandled expression opcode inside a condition => unknown
        if 0x12 <= op <= 0x60 and op not in (0x24, 0x26, 0x5C, 0x5F): conds[-1][1].append(('unk',))
    if op == 0x29:
        if stack:
            top = stack.pop()
            if top in (0x0A, 0x19, 0x30) and conds: conds.pop()
            if top in QOPS: cur_q = None
            if top == 0x01: cur_form = None
    elif scope:
        stack.append(op)
    p += ln

qname = {q['qid']: q for q in questions}

# ---------- evaluation (three-valued logic: True / False / None) ----------
def ev(tokens, env):
    st = []
    for t in tokens:
        if t == 'T': st.append(True)
        elif t == 'F': st.append(False)
        elif t == 'NOT':
            a = st.pop() if st else None; st.append(None if a is None else not a)
        elif t in ('AND', 'OR'):
            b_ = st.pop() if st else None; a = st.pop() if st else None
            if t == 'AND':
                st.append(False if (a is False or b_ is False) else (True if (a and b_) else None))
            else:
                st.append(True if (a is True or b_ is True) else (False if (a is False and b_ is False) else None))
        elif t[0] == 'eq':
            v = env.get(t[1]); st.append(None if v is None else (v in t[2]))
        else: st.append(None)
    # expression without a final operator (rare): take the top of the stack
    return st[-1] if st else None

def suppressed(cond_list, env):
    """True = surely hidden, None = depends on something else, False = shown"""
    res = False
    for kind, toks in cond_list:
        if kind != 'S': continue
        r = ev(toks, env)
        if r is True: return True
        if r is None: res = None
    return res

QID_HIDDEN = next(q['qid'] for q in questions if q['varstore'] == 'MSIHiddenFun')
QID_ACCESS = next((q['qid'] for q in questions if q['varstore'] == 'SystemAccess'), None)
ENVS = {'stock': {QID_HIDDEN: 1, QID_ACCESS: 0}, 'unlocked': {QID_HIDDEN: 0, QID_ACCESS: 0}}
ROOT = next(iter(forms))  # first declared form (0x2710 "Setup" on this BIOS)

def visibility(env):
    """BFS over forms via Ref (goto) opcodes; keeps the most certain path to each form."""
    best = {ROOT: (False, [forms[ROOT]['title']])}   # form -> (incertain?, chemin)
    dq = deque([ROOT])
    while dq:
        f = dq.popleft(); unc, path = best[f]
        for to, cl, prompt in forms[f]['refs']:
            if to not in forms: continue
            s = suppressed(cl, env)
            if s is True: continue
            nu = unc or (s is None)
            if to not in best or (best[to][0] and not nu):
                best[to] = (nu, path + [prompt or forms[to]['title']]); dq.append(to)
    return best

vis = {k: visibility(e) for k, e in ENVS.items()}

def state(q, env_key):
    v = vis[env_key].get(q['form'])
    if v is None: return 'hidden'
    s = suppressed(q['conds'], ENVS[env_key])
    if s is True: return 'hidden'
    if v[0] or s is None: return 'conditional'
    return 'visible'

def cond_text(cl):
    out = []
    for kind, toks in cl:
        parts = []
        for t in toks:
            if isinstance(t, tuple) and t[0] == 'eq':
                qq = qname.get(t[1]); n = (qq['prompt'] or f"{qq['varstore']}+{qq['offset']:#x}") if qq else f"Q{t[1]:#x}"
                parts.append(f"[{n}]∈{[hex(x) for x in t[2]]}" if len(t[2]) > 1 else f"[{n}]={t[2][0]:#x}")
            elif isinstance(t, tuple): parts.append('?')
            else: parts.append({'T': 'TRUE', 'F': 'FALSE'}.get(t, t))
        if parts: out.append(('Suppressed if ' if kind == 'S' else 'Grayed out if ') + ' '.join(parts))
    return ' ; '.join(out)

rows = []
for q in questions:
    if not q['prompt'] or q['type'] == 'Action': continue
    su, sd = state(q, 'stock'), state(q, 'unlocked')
    if su == 'visible': cat = '1. Visible'
    elif su == 'conditional': cat = '2. Conditional (hardware/settings)'
    elif sd in ('visible', 'conditional'): cat = '3. Hidden - MSI advanced menu'
    else: cat = '4. Hidden - permanently'
    path = (vis['unlocked'].get(q['form']) or vis['stock'].get(q['form']) or (None, ['(orphan form) ' + forms.get(q['form'], {}).get('title', '?')]))[1]
    if q['options']: vals = ' | '.join(f"{t} ({v:#x})" for v, t in q['options'])
    elif 'min' in q: vals = f"{q['min']} … {q['max']} (step {q['step']})"
    elif q['type'] == 'CheckBox': vals = 'Disabled (0) | Enabled (1)'
    else: vals = ''
    rows.append({'category': cat, 'menu': ' > '.join(path[1:]) or path[0], 'option': q['prompt'], 'type': q['type'],
                 'values': vals, 'default': '' if q['default'] is None else str(q['default']),
                 'varstore': q['varstore'], 'offset': f"{q['offset']:#05x}", 'size': q['size'] or '',
                 'help': q['help'].replace('\n', ' '), 'condition': cond_text(q['conds'])})

json.dump(rows, open(OUT, 'w'), ensure_ascii=False, indent=0)
from collections import Counter
print('QId MSIHiddenFun =', hex(QID_HIDDEN), '| QId SystemAccess =', hex(QID_ACCESS))
print('Reachable forms - stock:', len(vis['stock']), '| unlocked:', len(vis['unlocked']), '| total:', len(forms))
for k, v in sorted(Counter(r['category'] for r in rows).items()): print(f"{v:6}  {k}")
print('Total options:', len(rows))
