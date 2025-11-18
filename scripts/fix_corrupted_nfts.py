#!/usr/bin/env python3
"""
Fix Corrupted NFT Downloads
Find and re-download NFTs that failed to download properly
"""

import sys
sys.path.append('..')
import subprocess
import os
from pathlib import Path


def check_and_list_corrupted():
    """Find all corrupted NFT files"""
    
    nft_dir = Path(__file__).parent.parent / 'my_nft_collection' / 'tezos'
    corrupted = []
    
    print("🔍 Scanning for corrupted files...")
    print("="*70)
    
    for file in nft_dir.glob('*'):
        if file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif']:
            try:
                result = subprocess.run(
                    ['file', '--mime-type', '-b', str(file)],
                    capture_output=True,
                    text=True,
                    timeout=2
                )
                
                mime_type = result.stdout.strip()
                
                # Check if it's actually an image
                valid_types = ['image/', 'video/']
                is_valid = any(vtype in mime_type for vtype in valid_types)
                
                if not is_valid:
                    corrupted.append({
                        'path': str(file),
                        'name': file.name,
                        'mime': mime_type
                    })
                    print(f"❌ {file.name}")
                    print(f"   Type: {mime_type}")
                
            except Exception as e:
                print(f"⚠️  Error checking {file.name}: {e}")
    
    print("="*70)
    print(f"\n📊 Results:")
    print(f"   Corrupted files: {len(corrupted)}")
    print(f"   Valid files: {len(list(nft_dir.glob('*')))-len(corrupted)}")
    
    if corrupted:
        print(f"\n💡 Solutions:")
        print(f"   1. Re-download from Tezos wallet (automatic)")
        print(f"   2. Delete corrupted files and re-run NFT downloader")
        print(f"   3. Manually download from Kukai/objkt.com")
        
        delete = input(f"\n🗑️  Delete {len(corrupted)} corrupted files? (y/n): ").lower()
        
        if delete == 'y':
            for item in corrupted:
                try:
                    os.remove(item['path'])
                    print(f"   Deleted: {item['name']}")
                except Exception as e:
                    print(f"   Error deleting {item['name']}: {e}")
            
            print(f"\n✅ Deleted {len(corrupted)} corrupted files")
            print(f"\n📥 Now re-run: python scripts/download_my_nfts.py")
            print(f"   Choose option 1 to re-download Tezos NFTs")
    else:
        print(f"\n✅ All files are valid!")
    
    return corrupted


if __name__ == '__main__':
    check_and_list_corrupted()

