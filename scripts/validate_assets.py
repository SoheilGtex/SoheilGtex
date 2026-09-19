#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import os
import sys

def validate_svg(filepath):
    try:
        ET.parse(filepath)
        print(f"✅ {filepath} is valid XML/SVG.")
        return True
    except Exception as e:
        print(f"❌ {filepath} failed validation: {e}")
        return False

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets = [
        os.path.join(root_dir, 'assets', 'trajectory-dark.svg'),
        os.path.join(root_dir, 'assets', 'trajectory-light.svg')
    ]
    
    all_valid = True
    for asset in assets:
        if not os.path.exists(asset):
            print(f"❌ Missing file: {os.path.relpath(asset, root_dir)}")
            all_valid = False
        elif not validate_svg(asset):
            all_valid = False

    if not all_valid:
        sys.exit(1)
        
    print("All profile assets validated successfully.")

if __name__ == "__main__":
    main()