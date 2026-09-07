from pathlib import Path
import zipfile

BASE = Path(__file__).resolve().parents[1]
vault = BASE / "evidence/protected/vault.zip"
wordlist = BASE / "scripts/wordlist.txt"
out = BASE / "artefacts/recovered"
passwords = [x.strip() for x in wordlist.read_text().splitlines() if x.strip()]

with zipfile.ZipFile(vault) as z:
    if z.testzip() is None:
        z.extractall(out)
        (BASE / "logs/cracking.log").write_text("Bundled dummy archive opened; synthetic artefacts recovered.\n")
        print("Dummy archive opened.")
