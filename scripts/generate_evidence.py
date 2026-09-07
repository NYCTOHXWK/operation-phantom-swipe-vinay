from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
items = {
    "evidence/device01_skimmer/device_config.ini": "[device]\nexhibit=EXH-11\ndevice_type=ATM-skimmer\noperator_alias=Delta-7\n",
    "evidence/device02_phone/notes.txt": "Fictional forensic note. No real personal data.\n",
}
for rel, text in items.items():
    path = BASE / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
print("Synthetic evidence refreshed.")
