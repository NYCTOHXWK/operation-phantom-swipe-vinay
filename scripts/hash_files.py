from pathlib import Path
import hashlib

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "hashes/SHA256SUMS.txt"
lines = []
for path in sorted(BASE.rglob("*")):
    if not path.is_file() or "hashes" in path.parts or path.name == "SHA256SUMS.txt":
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    lines.append(f"{digest}  {path.relative_to(BASE)}")
OUT.write_text("\n".join(lines) + "\n")
print(f"Hashed {len(lines)} files.")
