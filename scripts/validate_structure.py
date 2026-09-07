from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
required = [
    "README.md", "AUTHORSHIP.md", "requirements.txt",
    "docs/01_Cybercrime_Taxonomy_and_Legal_Mapping.md",
    "docs/Legal_Technical_Report.pdf", "docs/Chain_of_Custody_Form.pdf",
    "docs/Execution_Guide.md", "artefacts/extracted_artefacts.md",
    "artefacts/evidence_log.csv", "evidence/protected/vault.zip",
    "scripts/generate_evidence.py", "scripts/hash_files.py",
    "scripts/search_media.py", "scripts/crack_zip.py"
]
missing = [x for x in required if not (BASE / x).exists()]
if missing:
    raise SystemExit("Missing: " + ", ".join(missing))
print("Required structure OK.")
