"""Verify public repository file bytes without fetching data or running experiments."""
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "PUBLICATION_MANIFEST.json").read_text())
errors = []
for row in manifest["files"]:
    path = (ROOT / row["path"]).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        errors.append(row["path"] + " missing")
        continue
    with path.open("rb") as stream:
        digest = sha256(stream.read()).hexdigest()
    if path.stat().st_size != row["bytes"] or digest != row["sha256"]:
        errors.append(row["path"] + " differs from the publication manifest")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS. {len(manifest['files'])} public files match the publication manifest.")
