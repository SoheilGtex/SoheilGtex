from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
readme = (root / "README.md").read_text(encoding="utf-8")
refs = re.findall(r'(?:src|srcset)="([^"]+)"', readme)
missing = [r for r in refs if not r.startswith(('http://','https://')) and not (root/r).exists()]
if missing:
    print("Missing local assets:")
    for m in missing: print(" -", m)
    sys.exit(1)
if len(readme.encode()) > 500_000:
    print("README exceeds GitHub's 500 KiB display limit")
    sys.exit(1)
print(f"Profile check passed: {len(refs)} image refs, {len(readme.encode())} bytes")
