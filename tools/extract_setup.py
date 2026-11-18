#!/usr/bin/env python3
"""Extract the AMI "Setup" DXE driver (PE32) from an AMI Aptio V BIOS image.

Usage: python3 extract_setup.py <bios_image> <output Setup.efi>

Works on a full SPI dump or on a BIOS-region-only image: it scans for every
firmware volume (_FVH signature), walks it (including compressed sections)
with uefi_firmware, and writes the PE32 section of the file whose user
interface name is "Setup".
"""
import sys
import uefi_firmware
from uefi_firmware.uefi import FirmwareVolume


def walk(obj):
    yield obj
    for child in getattr(obj, 'objects', None) or []:
        if child is not None:
            yield from walk(child)


def own_sections(ffs):
    """Sections of one FFS file, without descending into nested volumes/files."""
    stack = list(getattr(ffs, 'objects', None) or [])
    while stack:
        o = stack.pop()
        if o is None or o.__class__.__name__ in ('FirmwareVolume', 'FirmwareFile', 'FirmwareFileSystem'):
            continue
        yield o
        stack.extend(getattr(o, 'objects', None) or [])


def find_setup(image):
    """Return the largest PE32 named "Setup" (the HII forms driver)."""
    found = []
    seen = set()
    pos = 0
    while True:
        i = image.find(b'_FVH', pos)
        if i == -1:
            return max(found, key=len) if found else None
        pos = i + 4
        start = i - 0x28
        if start < 0 or start in seen:
            continue
        seen.add(start)
        fv = FirmwareVolume(image[start:])
        if not fv.valid_header or not fv.process():
            continue
        for o in walk(fv):
            if o.__class__.__name__ != 'FirmwareFile':
                continue
            secs = [x for x in own_sections(o) if x.__class__.__name__ == 'FirmwareFileSystemSection']
            names = [s for s in secs if s.type == 0x15]
            if not any(n.data.decode('utf-16-le', 'ignore').rstrip('\0') == 'Setup' for n in names):
                continue
            for s in secs:
                if s.type == 0x10:  # PE32
                    found.append(s.data)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    data = find_setup(open(sys.argv[1], 'rb').read())
    if data is None:
        sys.exit('Setup module not found')
    open(sys.argv[2], 'wb').write(data)
    print(f'Setup PE32 written: {len(data):,} bytes')
