# Execution Guide

This lab uses controlled evidence files to demonstrate acquisition, string searching, recovery and integrity verification.

## Realistic test dataset
Examples are written in an Indian investigation context: Connaught Place and Karol Bagh in New Delhi, Sector 18 in Noida and Banjara Hills in Hyderabad. Device models include Samsung Galaxy S24, OnePlus 12, iPhone 15 and Google Pixel 8. Names and usernames are fictional; payment references are deliberately non-usable.

## Run

```bash
python scripts/generate_evidence.py
python scripts/search_media.py
python scripts/crack_zip.py
python scripts/hash_files.py
python scripts/validate_structure.py
```

The protected archive uses a lab-only test password.
