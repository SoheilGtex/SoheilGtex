from pathlib import Path
import re, sys, xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
readme = root / "README.md"
text = readme.read_text(encoding="utf-8")
errors = []

# Keep the profile small and self-contained.
if len(text.encode("utf-8")) > 100_000:
    errors.append("README is unexpectedly large")

# Validate all local image references.
refs = re.findall(r'(?:src|srcset)="([^"#?]+)"', text)
for ref in refs:
    if ref.startswith(("http://", "https://")):
        errors.append(f"External image dependency found: {ref}")
        continue
    target = root / ref
    if not target.exists():
        errors.append(f"Missing image asset: {ref}")

# SVGs should remain parseable and self-hosted.
for svg in (root / "assets").glob("*.svg"):
    try:
        ET.parse(svg)
    except Exception as exc:
        errors.append(f"Invalid SVG {svg.name}: {exc}")

# Deliberately avoid common template widgets in this profile.
banned = ["github-readme-stats", "streak-stats", "typing-svg", "contribution-snake", "github-profile-trophy"]
for token in banned:
    if token in text.lower():
        errors.append(f"Template widget dependency found: {token}")

if errors:
    for err in errors:
        print(f"ERROR: {err}")
    sys.exit(1)
print(f"Profile check passed: {len(refs)} local image refs, {len(text.encode('utf-8'))} README bytes")
