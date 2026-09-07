#!/usr/bin/env bash
set -e
python3 scripts/generate_evidence.py
python3 scripts/hash_files.py
python3 scripts/search_media.py
python3 scripts/crack_zip.py
python3 scripts/validate_structure.py
