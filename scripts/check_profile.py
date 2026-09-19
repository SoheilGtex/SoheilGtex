from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
readme=(root/'README.md').read_text(encoding='utf-8')
refs=re.findall(r'(?:src|srcset)="([^"]+)"',readme)
missing=[r for r in refs if not (root/r).exists()]
if missing:
    print('Missing assets:', *missing, sep='\n- '); sys.exit(1)
if len(readme.encode())>200_000:
    print('README is unexpectedly large'); sys.exit(1)
for banned in ['github-readme-stats','komarev','readme-typing-svg','streak-stats']:
    if banned in readme:
        print('Template-like external widget detected:',banned);sys.exit(1)
print(f'Profile check passed: {len(refs)} image refs, {len(readme.encode())} bytes')
