# MSI GP76 Leopard: hidden BIOS options

*[Version française](README.fr.md)*

A full map of the BIOS Setup options of the **MSI GP76 Leopard 10UE / 10UG / 10UH** (board **MS-17K2**), including the **2,847 options MSI hides** from the stock menu.

The BIOS analysed is **E17K2IMS.30F**, released on 2021-10-01. It is the last BIOS MSI published for this laptop.

Everything here comes from read-only analysis of the official BIOS file. No firmware is modified or redistributed in this repository.

## Results at a glance

| Category | Options |
|---|---:|
| Visible in the stock menu | 18 |
| Conditional (depends on detected hardware or another setting) | 68 |
| **Hidden: MSI advanced menu** | **2,847** |
| Hidden permanently | 344 |
| **Total** | **3,277** |

Browse the results:

- [`results/HIGHLIGHTS.md`](results/HIGHLIGHTS.md): 44 notable hidden options (power limits, voltage offsets, locks, thermal, graphics)
- [`results/HIDDEN_OPTIONS.md`](results/HIDDEN_OPTIONS.md): every hidden option, one page per menu
- [`results/options.csv`](results/options.csv) and [`results/options.xlsx`](results/options.xlsx): all 3,277 options with values, defaults, help text, variable and offset

## How MSI hides the options

Almost the whole *Advanced* menu sits behind one variable, **`MSIHiddenFun`**. Each submenu link is wrapped in `SuppressIf MSIHiddenFun == 1`, and the factory value is 1.

When the variable is 0, the following menus appear:

- CPU Information, Power & Performance (PL1/PL2/PL4, Turbo, C-states, CFG Lock)
- **OverClocking Performance Menu** (core / GT / uncore voltage offsets with +/- prefix, ratios)
- System Agent (graphics, primary display, DVMT, Above 4G)
- PCH-IO, PCH-FW (ME state), Thermal (TCC offset, trip points, fan speed)
- AMT, Intel ICC, Debug Settings, ACPI, Connectivity

MSI toggles this variable with a key combination in the BIOS. It is commonly reported as **Right Ctrl + Right Shift + Left Alt + F2**. This combination is handled in compiled code, not in the forms, so this analysis does not confirm it.

The **Chipset** tab is hidden with `SuppressIf TRUE` and never appears. Five other forms that hold options (PCIe link options, control logic, MIPI camera, external GPU display, demo board) are not linked from any menu.

## Notable defaults

These are the defaults written in the forms. The values active on a given laptop live in NVRAM and may differ.

| Option | Form default | Why it matters |
|---|---|---|
| Overclocking Lock | Enabled | On Comet Lake this usually blocks undervolting, even with the menu unlocked (Plundervolt mitigation) |
| CFG Lock | Enabled | Locks MSR 0xE2 (relevant for hackintosh and some power tools) |
| BIOS Lock | Disabled | If disabled on your machine, the OS can write to the BIOS flash |
| Flash Protection Range Registers | Disabled | Same: no write protection of flash ranges |
| Tcc Activation Offset | 5 | Thermal throttling starts 5 °C below TjMax |

## Checked on a real machine

The form defaults above are not the whole story. [`tools/check_live.py`](tools/check_live.py) reads the live state under Linux, read-only:

```bash
sudo python3 -I tools/check_live.py
```

Results on a GP76 Leopard with an i7-10870H, BIOS E17K2IMS.30F, Fedora:

| Check | Result | Meaning |
|---|---|---|
| `MSIHiddenFun` variable | 1 | Advanced menu hidden; the offset from the analysis is correct |
| CFG Lock (MSR 0xE2, bit 15) | Locked | Set by the BIOS, cannot be changed from the OS |
| Overclocking Lock (MSR 0x194, bit 20) | Locked | Undervolting is impossible from the OS (ThrottleStop, intel-undervolt) |
| BIOS_CNTL (SPI controller 00:1f.5) | `0xaa`: BIOSWE=0, BLE=1, SMM_BWP=1, BILD=1 | The BIOS flash is write-protected: only SMM firmware can write to it, not the OS, even as root |
| Microcode | `0x100` | Latest Intel revision for CML-H (`06-a5-02`) as of the May 2025 release, loaded by Linux at boot |

So although the form default for "BIOS Lock" is Disabled, the flash is protected in practice. The other setup variables (`Setup`, `CpuSetup`, `PchSetup`…) are boot-service only on this BIOS, so Linux cannot read them; the MSR and BIOS_CNTL checks show the real state anyway.

Each option in the results lists its **VarStore, offset and size**: the exact location of the value inside its UEFI variable. Tools such as `setup_var` use this information. Changing BIOS variables can make a laptop unbootable, so see the disclaimer below.

## Run it yourself

Requires Python 3.9+.

```bash
pip install -r requirements.txt

# 1. Download the BIOS from MSI's official support page for the GP76 Leopard 10UX
#    and unzip it (file E17K2IMS.30F).

# 2. Extract the "Setup" module (AMI forms driver)
python3 tools/extract_setup.py E17K2IMS.30F Setup.efi

# 3. Decode its IFR forms and classify every option
python3 tools/ifr_analyze.py Setup.efi options.json

# 4. Export to CSV / Markdown / XLSX
python3 tools/export.py options.json results "MSI GP76 Leopard (MS-17K2) BIOS E17K2IMS.30F"
```

The tools are written for AMI Aptio V images. They should work on other MSI laptops of the same generation, but they have only been tested on this BIOS.

## How it works

1. **`extract_setup.py`** scans the image for firmware volumes (`_FVH`), decompresses them with [`uefi_firmware`](https://github.com/theopolis/uefi-firmware-parser), and saves the PE32 of the file named `Setup`.
2. **`ifr_analyze.py`** finds the HII form package and the en-US string package inside `Setup.efi`. It then decodes the IFR opcodes from the UEFI specification: forms, gotos, questions, options, defaults, `SuppressIf` / `GrayOutIf`. Visibility is evaluated twice, with `MSIHiddenFun = 1` (stock) and `0` (unlocked), by walking the menu tree from the root form. Conditions on other settings or on hardware use three-valued logic: unknown means "conditional".
3. **`export.py`** writes the tables.

## Limitations

- This is a custom IFR decoder, not a complete one. Unsupported expression opcodes are treated as "unknown", which can move an option between "Visible" and "Conditional".
- When a list shows a raw number as its default (for example `90` for Primary Display), the real default is defined elsewhere, in AMI's default variables.
- Options named `N/A` are placeholders, for example USB ports, whose label is filled in at boot.

## Disclaimer

This project is for educational and documentation purposes. It does not include MSI firmware. Unlocking hidden menus or changing UEFI variables can damage or brick your laptop and may void your warranty. You do this at your own risk. MSI is a trademark of Micro-Star International. This project is not affiliated with or endorsed by MSI.

## License

[MIT](LICENSE) for the tools and generated documentation. The option names and help texts come from MSI's BIOS.
