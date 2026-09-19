import os
import sys
from pathlib import Path
import re

def validate_profile():
    root = Path(__file__).resolve().parents[1]
    readme_path = root / 'README.md'
    
    if not readme_path.exists():
        print("Error: README.md is missing.")
        sys.exit(1)

    readme_content = readme_path.read_text(encoding='utf-8')
    
    # Check for presence of required assets
    refs = re.findall(r'(?:src|srcset)="([^"]+)"', readme_content)
    missing = [r for r in refs if not (root / r).exists()]
    
    if missing:
        print('Error: Missing referenced assets:')
        for m in missing:
            print(f'  - {m}')
        sys.exit(1)

    # Check for legacy template widgets
    banned_widgets = ['github-readme-stats', 'komarev', 'readme-typing-svg', 'streak-stats', 'wakatime']
    for banned in banned_widgets:
        if banned in readme_content.lower():
            print(f'Error: Template-like external widget detected: {banned}')
            sys.exit(1)
            
    # Validate Size (ensure it remains lightweight)
    if len(readme_content.encode()) > 50_000:
        print('Error: README is unexpectedly large. Keep it concise.')
        sys.exit(1)

    print(f'Profile check passed successfully. ({len(refs)} local image references verified)')

if __name__ == '__main__':
    validate_profile()