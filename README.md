# Operation Phantom Swipe — Vinay
### Academic Digital Forensics Simulation

**Name:** Vinay  
**Roll No.:** 2301730176  
**Course:** B.Tech CSE  
**Submission:** 2026

This repository is a small, self-contained forensic exercise based on a fictional ATM/card-fraud case. All case identifiers and evidence are fabricated for academic use. No real customer, banking, wallet or device data is included.

## Required work

1. Cybercrime classification and legal mapping — `docs/01_Cybercrime_Taxonomy_and_Legal_Mapping.md`
2. Evidence acquisition, hashing and chain of custody — `hashes/SHA256SUMS.txt`, `logs/hashing.log`, `docs/Chain_of_Custody_Form.pdf`
3. Media search and artefact extraction — `scripts/search_media.py`, `artefacts/`, `logs/search.log`
4. Protected evidence simulation — `evidence/protected/vault.zip`, `scripts/crack_zip.py`, `logs/cracking.log`
5. Legal-technical report — `docs/Legal_Technical_Report.pdf`

## Run

```bash
python3 scripts/generate_evidence.py
python3 scripts/hash_files.py
python3 scripts/search_media.py
python3 scripts/crack_zip.py
python3 scripts/validate_structure.py
```

The protected archive contains only fabricated records. The password test is limited to this bundled dummy archive.
