# MSI GP76 Leopard : les options cachées du BIOS

*[English version](README.md)*

La carte complète des options du Setup BIOS des **MSI GP76 Leopard 10UE / 10UG / 10UH** (carte mère **MS-17K2**), y compris les **2 847 options que MSI masque** dans le menu d'origine.

Le BIOS analysé est le **E17K2IMS.30F**, publié le 01/10/2021. C'est le dernier BIOS publié par MSI pour ce portable.

Tout provient d'une analyse en lecture seule du fichier BIOS officiel. Aucun firmware n'est modifié ni redistribué dans ce dépôt.

## Les chiffres

| Catégorie | Options |
|---|---:|
| Visibles dans le menu d'origine | 18 |
| Conditionnelles (selon le matériel détecté ou un autre réglage) | 68 |
| **Cachées : menu avancé MSI** | **2 847** |
| Cachées en permanence | 344 |
| **Total** | **3 277** |

Les résultats :

- [`results/HIGHLIGHTS.md`](results/HIGHLIGHTS.md) : 44 options cachées notables (limites de puissance, décalages de tension, verrous, thermique, graphismes)
- [`results/HIDDEN_OPTIONS.md`](results/HIDDEN_OPTIONS.md) : toutes les options cachées, une page par menu
- [`results/options.csv`](results/options.csv) et [`results/options.xlsx`](results/options.xlsx) : les 3 277 options avec valeurs, défauts, texte d'aide, variable et position

## Comment MSI cache les options

Presque tout le menu *Advanced* dépend d'une seule variable, **`MSIHiddenFun`**. Chaque lien vers un sous-menu est entouré d'un `SuppressIf MSIHiddenFun == 1`, et la valeur d'usine est 1.

Quand la variable vaut 0, ces menus apparaissent :

- CPU Information, Power & Performance (PL1/PL2/PL4, Turbo, états C, CFG Lock)
- **OverClocking Performance Menu** (décalages de tension cœur / GT / uncore avec signe +/-, ratios)
- System Agent (graphismes, écran principal, DVMT, Above 4G)
- PCH-IO, PCH-FW (état du ME), Thermal (TCC offset, seuils, ventilateur)
- AMT, Intel ICC, Debug Settings, ACPI, Connectivity

MSI bascule cette variable avec une combinaison de touches dans le BIOS, souvent citée comme **Ctrl droit + Maj droit + Alt gauche + F2**. Cette combinaison est gérée dans du code compilé, pas dans les formulaires : cette analyse ne la confirme donc pas.

L'onglet **Chipset** est masqué par `SuppressIf TRUE` et n'apparaît jamais. Cinq autres formulaires contenant des options (liens PCIe, control logic, caméra MIPI, écran GPU externe, demo board) ne sont reliés à aucun menu.

## Valeurs par défaut notables

Ce sont les défauts écrits dans les formulaires. Les valeurs actives sur un portable donné sont stockées en NVRAM et peuvent différer.

| Option | Défaut | Pourquoi c'est intéressant |
|---|---|---|
| Overclocking Lock | Enabled | Sur Comet Lake, bloque en général l'undervolt, même menu débloqué (parade à Plundervolt) |
| CFG Lock | Enabled | Verrouille le MSR 0xE2 (utile pour hackintosh et certains outils d'énergie) |
| BIOS Lock | Disabled | S'il est désactivé sur ta machine, l'OS peut écrire dans la flash du BIOS |
| Flash Protection Range Registers | Disabled | Idem : pas de protection en écriture de zones de la flash |
| Tcc Activation Offset | 5 | Le bridage thermique commence 5 °C sous la TjMax |

## Vérifié sur une vraie machine

Les défauts des formulaires ne disent pas tout. [`tools/check_live.py`](tools/check_live.py) lit l'état réel sous Linux, en lecture seule :

```bash
sudo python3 -I tools/check_live.py
```

Résultats sur un GP76 Leopard avec un i7-10870H, BIOS E17K2IMS.30F, sous Fedora :

| Vérification | Résultat | Signification |
|---|---|---|
| Variable `MSIHiddenFun` | 1 | Menu avancé masqué ; la position trouvée par l'analyse est la bonne |
| CFG Lock (MSR 0xE2, bit 15) | Verrouillé | Fixé par le BIOS, impossible à changer depuis l'OS |
| Overclocking Lock (MSR 0x194, bit 20) | Verrouillé | Undervolt impossible depuis l'OS (ThrottleStop, intel-undervolt) |
| BIOS_CNTL (contrôleur SPI 00:1f.5) | `0xaa` : BIOSWE=0, BLE=1, SMM_BWP=1, BILD=1 | La flash du BIOS est protégée en écriture : seul le firmware SMM peut y écrire, pas l'OS, même en root |
| Microcode | `0x100` | Dernière révision Intel pour CML-H (`06-a5-02`) à la publication de mai 2025, chargée par Linux au démarrage |

Même si le défaut du formulaire pour « BIOS Lock » est Disabled, la flash est donc protégée en pratique. Les autres variables du Setup (`Setup`, `CpuSetup`, `PchSetup`…) ne sont accessibles qu'au démarrage sur ce BIOS : Linux ne peut pas les lire. Les vérifications MSR et BIOS_CNTL montrent malgré tout l'état réel.

Chaque option indique son **VarStore, sa position (offset) et sa taille** : l'emplacement exact de sa valeur dans la variable UEFI. Des outils comme `setup_var` s'en servent. Modifier des variables BIOS peut rendre un portable inutilisable : voir l'avertissement plus bas.

## Le refaire soi-même

Nécessite Python 3.9 ou plus récent.

```bash
pip install -r requirements.txt

# 1. Télécharger le BIOS sur la page support officielle MSI du GP76 Leopard 10UX
#    et le dézipper (fichier E17K2IMS.30F).

# 2. Extraire le module « Setup » (pilote des formulaires AMI)
python3 tools/extract_setup.py E17K2IMS.30F Setup.efi

# 3. Décoder ses formulaires IFR et classer chaque option
python3 tools/ifr_analyze.py Setup.efi options.json

# 4. Exporter en CSV / Markdown / XLSX
python3 tools/export.py options.json results "MSI GP76 Leopard (MS-17K2) BIOS E17K2IMS.30F"
```

Les outils visent les images AMI Aptio V. Ils devraient fonctionner sur d'autres portables MSI de la même génération, mais n'ont été testés que sur ce BIOS.

## Fonctionnement

1. **`extract_setup.py`** cherche les volumes firmware (`_FVH`) dans l'image, les décompresse avec [`uefi_firmware`](https://github.com/theopolis/uefi-firmware-parser) et enregistre le PE32 du fichier nommé `Setup`.
2. **`ifr_analyze.py`** trouve dans `Setup.efi` le paquet de formulaires HII et le paquet de chaînes en-US. Il décode ensuite les opcodes IFR de la spécification UEFI : formulaires, liens, questions, choix, défauts, `SuppressIf` / `GrayOutIf`. La visibilité est évaluée deux fois, avec `MSIHiddenFun = 1` (usine) et `0` (débloqué), en parcourant l'arbre des menus depuis la racine. Les conditions qui dépendent d'autres réglages ou du matériel sont évaluées en logique à trois valeurs : inconnu signifie « conditionnelle ».
3. **`export.py`** produit les tableaux.

## Limites

- C'est un décodeur IFR maison, pas complet. Les opcodes d'expression non gérés sont traités comme « inconnus », ce qui peut faire passer une option de « Visible » à « Conditionnelle ».
- Quand une liste affiche un nombre brut comme défaut (par exemple `90` pour Primary Display), le vrai défaut est défini ailleurs, dans les variables de défauts AMI.
- Les options nommées `N/A` sont des emplacements génériques, par exemple des ports USB, dont le libellé est rempli au démarrage.

## Avertissement

Projet à but pédagogique et documentaire. Il ne contient aucun firmware MSI. Débloquer les menus cachés ou modifier des variables UEFI peut endommager ou bloquer définitivement ton portable, et peut annuler la garantie. C'est à tes risques. MSI est une marque de Micro-Star International. Ce projet n'est ni affilié à MSI ni approuvé par MSI.

## Licence

[MIT](LICENSE) pour les outils et la documentation générée. Les noms d'options et textes d'aide proviennent du BIOS MSI.
