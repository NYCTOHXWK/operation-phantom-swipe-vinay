from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
terms = ["skimmer", "OTP", "Bluetooth"]
matches = []
for p in (BASE / "evidence").rglob("*"):
    if p.is_file():
        text = p.read_text(errors="ignore")
        for term in terms:
            if term.lower() in text.lower():
                matches.append((str(p.relative_to(BASE)), term))
                break
log = BASE / "logs/search.log"
log.write_text("Search terms: " + ", ".join(terms) + "\n" + "\n".join(f"{p} -> {t}" for p,t in matches) + "\n")
print("\n".join(f"{p} -> {t}" for p,t in matches))
