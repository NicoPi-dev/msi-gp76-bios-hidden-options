#!/usr/bin/env python3
"""Read-only check of the live BIOS state on an MSI GP76 Leopard (E17K2IMS.30F) under Linux.
Nothing is written: it reads UEFI variables, two CPU MSRs, one chipset register and /proc/cpuinfo.
Run with: sudo python3 -I check_live.py

Offsets come from results/options.csv. Most AMI setup variables are boot-service only,
so Linux usually cannot see them; the MSR and BIOS_CNTL checks show the real state anyway.
"""
import os, struct, subprocess

EFI = '/sys/firmware/efi/efivars'
GUID = {
    'Setup':           'ec87d643-eba4-4bb5-a1e5-3f3e36b20da9',
    'MSIHiddenFun':    '2a28a81a-dcbf-42f2-8366-b92fa64fe7f7',
    'CpuSetup':        'b08f97ff-e6e8-4193-a997-5e9e9b0adb32',
    'SaSetup':         '72c5e28c-7783-43a1-8767-fad73fccafa4',
    'PchSetup':        '4570b7f1-ade8-4943-8dc3-406472842384',
    'MeSetupStorage':  '5432122d-d034-49d2-a6de-65a829eb4c74',
    'SecureBootSetup': '7b59104a-c00d-4158-87ff-f04d6396a915',
}
ONOFF = {0: 'Disabled', 1: 'Enabled'}
# (label, variable, offset, size, value names)
OPTIONS = [
    ('MSI advanced menu (MSIHiddenFun)', 'MSIHiddenFun', 0x000, 1, {0: '0 = advanced menu SHOWN', 1: '1 = advanced menu hidden'}),
    ('CFG Lock',                         'CpuSetup', 0x03e, 1, ONOFF),
    ('Overclocking Lock',                'CpuSetup', 0x0da, 1, ONOFF),
    ('BIOS Guard',                       'CpuSetup', 0x0db, 1, ONOFF),
    ('BIOS Lock',                        'PchSetup', 0x017, 1, ONOFF),
    ('Flash Protection Range Registers', 'PchSetup', 0x6dd, 1, ONOFF),
    ('Allow BIOS Downgrade',             'Setup',    0x730, 1, ONOFF),
    ('ME State',                         'MeSetupStorage', 0x002, 1, ONOFF),
    ('Secure Boot Support',              'SecureBootSetup', 0x000, 1, ONOFF),
    ('Software Guard Extensions (SGX)',  'CpuSetup', 0x0e0, 1, {0: 'Disabled', 1: 'Enabled', 2: 'Software Controlled'}),
    ('Hyper-Threading',                  'CpuSetup', 0x005, 1, ONOFF),
    ('Virtualization (VT-x)',            'CpuSetup', 0x0b4, 1, ONOFF),
    ('VT-d',                             'SaSetup',  0x0f9, 1, ONOFF),
    ('Turbo Mode',                       'CpuSetup', 0x011, 1, ONOFF),
    ('Power Limit 1 (mW, 0 = auto)',     'CpuSetup', 0x012, 4, None),
    ('Power Limit 2 (mW, 0 = auto)',     'CpuSetup', 0x019, 4, None),
    ('Tcc Activation Offset (C)',       'CpuSetup', 0x07a, 1, None),
    ('Core Voltage Offset (mV)',         'CpuSetup', 0x1bd, 2, None),
    ('Core Voltage Offset sign',      'CpuSetup', 0x1bf, 1, {0: '+', 1: '-'}),
]


def read_var(name):
    path = f'{EFI}/{name}-{GUID[name]}'
    try:
        with open(path, 'rb') as f:
            return f.read()[4:]          # first 4 bytes = UEFI attributes
    except FileNotFoundError:
        return None
    except PermissionError:
        return 'perm'


print('=== 1. Settings stored by the BIOS (UEFI variables) ===')
cache = {}
for label, var, off, size, names in OPTIONS:
    if var not in cache:
        cache[var] = read_var(var)
    data = cache[var]
    if data is None:
        val = 'not visible from the OS'
    elif data == 'perm':
        val = 'permission denied (run with sudo)'
    elif off + size > len(data):
        val = f'outside variable (size {len(data)})'
    else:
        raw = int.from_bytes(data[off:off + size], 'little')
        val = names.get(raw, f'unknown value {raw}') if names else str(raw)
    print(f'  {label:<40} {val}')


def rdmsr(reg):
    try:
        fd = os.open('/dev/cpu/0/msr', os.O_RDONLY)
        try:
            return struct.unpack('<Q', os.pread(fd, 8, reg))[0]
        finally:
            os.close(fd)
    except OSError as e:
        return e


print('\n=== 2. Real state in the CPU (MSRs) ===')
try:
    subprocess.run(['modprobe', 'msr'], check=False)
except OSError:
    pass
v = rdmsr(0xE2)
print('  CFG Lock (MSR 0xE2, bit 15)          ', 'unreadable: ' + str(v) if isinstance(v, Exception) else ('LOCKED' if v >> 15 & 1 else 'unlocked'))
v = rdmsr(0x194)
print('  Overclocking Lock (MSR 0x194, bit 20)', 'unreadable: ' + str(v) if isinstance(v, Exception) else ('LOCKED' if v >> 20 & 1 else 'unlocked'))

print('\n=== 3. BIOS flash write protection (SPI controller, 00:1f.5) ===')
try:
    with open('/sys/bus/pci/devices/0000:00:1f.5/config', 'rb') as f:
        f.seek(0xDC)
        bc = f.read(1)[0]
    print(f'  BIOS_CNTL = 0x{bc:02x}')
    print(f'  BIOSWE  (write enable)            : {bc & 1}')
    print(f'  BLE     (BIOS lock enable)        : {bc >> 1 & 1}')
    print(f'  SMM_BWP (SMM-only BIOS write)     : {bc >> 5 & 1}')
    print(f'  BILD    (BIOS interface lockdown) : {bc >> 7 & 1}')
except (OSError, IndexError) as e:
    print('  unreadable:', e)

print('\n=== 4. CPU microcode ===')
with open('/proc/cpuinfo') as f:
    info = f.read().splitlines()
for key in ('model name', 'microcode'):
    line = next((l for l in info if l.startswith(key)), None)
    if line:
        print('  ' + line.split(':', 1)[0].strip() + ' : ' + line.split(':', 1)[1].strip())
