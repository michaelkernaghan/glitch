#!/usr/bin/env python3
"""
NFT Downloader - Download your owned NFTs from Tezos (Objkt) and EVM chains
"""

import requests
import json
import os
from pathlib import Path
import time
import sys


class NFTDownloader:
    def __init__(self, output_dir='downloaded_nfts'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Load API keys from config if available
        self.config = self.load_config()
        
        # IPFS gateways (fallbacks if one fails)
        self.ipfs_gateways = [
            'https://ipfs.io/ipfs/',
            'https://cloudflare-ipfs.com/ipfs/',
            'https://gateway.pinata.cloud/ipfs/',
            'https://dweb.link/ipfs/',
        ]
    
    def load_config(self):
        """Load API keys from config.json"""
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')
        
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    return json.load(f)
            except:
                pass
        
        return {}
    
    def download_tezos_nfts(self, wallet_address):
        """Download NFTs owned on Tezos (via Objkt API)"""
        
        print(f"🔍 Fetching Tezos NFTs for: {wallet_address}")
        print("="*70)
        
        # Objkt GraphQL API
        url = "https://data.objkt.com/v3/graphql"
        
        query = """
        query GetUserTokens($address: String!) {
          token_holder(
            where: {
              holder_address: {_eq: $address}
              quantity: {_gt: "0"}
            }
            limit: 100
          ) {
            token {
              token_id
              name
              description
              artifact_uri
              display_uri
              thumbnail_uri
              fa_contract
            }
            quantity
          }
        }
        """
        
        variables = {"address": wallet_address}
        
        try:
            response = requests.post(
                url,
                json={'query': query, 'variables': variables},
                headers={'Content-Type': 'application/json'},
                timeout=30
            )
            
            if response.status_code != 200:
                print(f"❌ Error: API returned status {response.status_code}")
                return
            
            data = response.json()
            
            if 'errors' in data:
                print(f"❌ API Error: {data['errors']}")
                return
            
            holdings = data.get('data', {}).get('token_holder', [])
            
            if not holdings:
                print("📭 No NFTs found for this address")
                return
            
            print(f"✅ Found {len(holdings)} NFTs!\n")
            
            # Create Tezos folder
            tezos_dir = os.path.join(self.output_dir, 'tezos')
            os.makedirs(tezos_dir, exist_ok=True)
            
            for idx, holding in enumerate(holdings, 1):
                token = holding['token']
                quantity = holding['quantity']
                
                token_id = token.get('token_id', 'unknown')
                name = token.get('name', f'Token_{token_id}')
                contract = token.get('fa_contract', 'unknown')
                
                print(f"\n[{idx}/{len(holdings)}] {name}")
                print(f"   Token ID: {token_id}")
                print(f"   Contract: {contract}")
                print(f"   Owned: {quantity}")
                
                # Try different URI fields (artifact_uri is usually the full quality)
                uri = (token.get('artifact_uri') or 
                       token.get('display_uri') or 
                       token.get('thumbnail_uri'))
                
                if uri:
                    print(f"   URI: {uri[:60]}...")
                    
                    # Download the NFT
                    filename = self.sanitize_filename(f"{name}_{token_id}")
                    self.download_from_uri(uri, tezos_dir, filename)
                else:
                    print("   ⚠️  No media URI found")
                
                # Small delay to be nice to servers
                time.sleep(0.5)
            
            print(f"\n✅ Tezos NFTs downloaded to: {tezos_dir}")
            
        except Exception as e:
            print(f"❌ Error fetching Tezos NFTs: {e}")
    
    def download_evm_nfts(self, wallet_address):
        """Download NFTs owned on EVM chains (Ethereum, Polygon, etc.)"""
        
        print(f"\n🔍 Fetching EVM NFTs for: {wallet_address}")
        print("="*70)
        
        # Check if we have Alchemy API key
        alchemy_key = self.config.get('alchemy_api_key', '')
        
        if alchemy_key and alchemy_key != 'PASTE_YOUR_ALCHEMY_KEY_HERE':
            print("✅ Using Alchemy API key from config.json")
            return self.download_with_alchemy(wallet_address, alchemy_key)
        else:
            print("⚠️  No Alchemy API key found in config.json")
            print("   See ALCHEMY_SETUP.md for instructions")
        
        print("\n📝 Trying OpenSea public API (limited)...")
        
        # Try OpenSea API (no key needed but rate limited)
        url = f"https://api.opensea.io/api/v2/chain/ethereum/account/{wallet_address}/nfts"
        
        headers = {
            'Accept': 'application/json',
            'X-API-KEY': self.config.get('opensea_api_key', '')
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=30)
            
            if response.status_code == 429:
                print("⚠️  Rate limited. Try again in a few minutes or add API key.")
                return
            
            if response.status_code != 200:
                print(f"⚠️  API returned status {response.status_code}")
                print("   Trying alternative method...")
                self.download_evm_simple(wallet_address)
                return
            
            data = response.json()
            nfts = data.get('nfts', [])
            
            if not nfts:
                print("📭 No NFTs found (or rate limited)")
                return
            
            print(f"✅ Found {len(nfts)} NFTs!\n")
            
            # Create EVM folder
            evm_dir = os.path.join(self.output_dir, 'evm')
            os.makedirs(evm_dir, exist_ok=True)
            
            for idx, nft in enumerate(nfts[:50], 1):  # Limit to 50 for free tier
                name = nft.get('name', 'Unnamed')
                token_id = nft.get('identifier', 'unknown')
                collection = nft.get('collection', 'Unknown')
                
                print(f"\n[{idx}/{len(nfts)}] {name}")
                print(f"   Collection: {collection}")
                print(f"   Token ID: {token_id}")
                
                # Get image URL
                image_url = nft.get('image_url') or nft.get('display_image_url')
                
                if image_url:
                    filename = self.sanitize_filename(f"{collection}_{name}_{token_id}")
                    self.download_from_uri(image_url, evm_dir, filename)
                else:
                    print("   ⚠️  No image URL found")
                
                time.sleep(0.5)
            
            print(f"\n✅ EVM NFTs downloaded to: {evm_dir}")
            
        except Exception as e:
            print(f"❌ Error fetching EVM NFTs: {e}")
    
    def download_evm_simple(self, wallet_address):
        """Simpler EVM method using public APIs"""
        print("📝 Using public NFT API...")
        
        # Try SimpleHash API (free tier, no key needed for basic queries)
        try:
            url = f"https://api.simplehash.com/api/v0/nfts/owners?chains=ethereum,polygon&wallet_addresses={wallet_address}"
            
            headers = {
                'Accept': 'application/json',
                'X-API-KEY': ''  # Works without key for limited requests
            }
            
            response = requests.get(url, headers=headers, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                nfts = data.get('nfts', [])
                
                if nfts:
                    print(f"✅ Found {len(nfts)} EVM NFTs!\n")
                    
                    evm_dir = os.path.join(self.output_dir, 'evm')
                    os.makedirs(evm_dir, exist_ok=True)
                    
                    for idx, nft in enumerate(nfts[:50], 1):
                        name = nft.get('name', 'Unnamed')
                        token_id = nft.get('token_id', 'unknown')
                        collection = nft.get('collection', {}).get('name', 'Unknown')
                        
                        print(f"\n[{idx}/{len(nfts[:50])}] {name}")
                        print(f"   Collection: {collection}")
                        
                        image_url = nft.get('image_url') or nft.get('previews', {}).get('image_large_url')
                        
                        if image_url:
                            filename = self.sanitize_filename(f"{collection}_{name}_{token_id}")
                            self.download_from_uri(image_url, evm_dir, filename)
                        
                        time.sleep(0.5)
                    
                    print(f"\n✅ EVM NFTs downloaded to: {evm_dir}")
                    return
            
            print("⚠️  Public API rate limited or wallet has no EVM NFTs")
            print("\n💡 To download EVM NFTs, you can:")
            print("   1. Get free Alchemy API key: https://www.alchemy.com/")
            print("   2. Or manually export from OpenSea/marketplace")
            print("   3. Or provide IPFS hashes directly (option 4 in menu)")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("\n💡 For EVM NFTs, consider:")
            print("   - Getting free Alchemy API key: https://www.alchemy.com/")
            print("   - Or use OpenSea's export feature")
    
    def download_with_alchemy(self, wallet_address, api_key):
        """Download using Alchemy API"""
        
        print("🔑 Using Alchemy API...")
        
        # Alchemy getNFTs endpoint
        url = f"https://eth-mainnet.g.alchemy.com/nft/v3/{api_key}/getNFTsForOwner"
        
        params = {
            'owner': wallet_address,
            'withMetadata': 'true',
            'pageSize': 100
        }
        
        try:
            response = requests.get(url, params=params, timeout=30)
            
            if response.status_code != 200:
                print(f"❌ Alchemy API error: {response.status_code}")
                return
            
            data = response.json()
            nfts = data.get('ownedNfts', [])
            
            if not nfts:
                print("📭 No NFTs found")
                return
            
            print(f"✅ Found {len(nfts)} Ethereum NFTs!\n")
            
            evm_dir = os.path.join(self.output_dir, 'evm')
            os.makedirs(evm_dir, exist_ok=True)
            
            for idx, nft in enumerate(nfts, 1):
                title = nft.get('name') or nft.get('title', 'Unnamed')
                token_id = nft.get('tokenId', 'unknown')
                contract = nft.get('contract', {}).get('name', 'Unknown')
                
                print(f"\n[{idx}/{len(nfts)}] {title}")
                print(f"   Collection: {contract}")
                print(f"   Token ID: {token_id}")
                
                # Get image URL (try multiple sources)
                media = nft.get('image', {})
                image_url = (
                    media.get('originalUrl') or 
                    media.get('cachedUrl') or
                    nft.get('gateway', '')
                )
                
                if image_url:
                    filename = self.sanitize_filename(f"{contract}_{title}_{token_id}")
                    self.download_from_uri(image_url, evm_dir, filename)
                else:
                    print("   ⚠️  No image URL found")
                
                time.sleep(0.3)
            
            print(f"\n✅ Ethereum NFTs downloaded to: {evm_dir}")
            
        except Exception as e:
            print(f"❌ Error with Alchemy: {e}")
    
    def download_from_uri(self, uri, output_dir, filename):
        """Download file from URI (supports IPFS, HTTP, etc.)"""
        
        try:
            # Handle IPFS URIs
            if uri.startswith('ipfs://'):
                ipfs_hash = uri.replace('ipfs://', '')
                download_url = self.ipfs_gateways[0] + ipfs_hash
            elif uri.startswith('ar://'):
                # Arweave
                arweave_hash = uri.replace('ar://', '')
                download_url = f'https://arweave.net/{arweave_hash}'
            else:
                download_url = uri
            
            # Determine file extension
            ext = self.get_extension_from_url(download_url)
            if not filename.endswith(ext):
                filename = f"{filename}{ext}"
            
            output_path = os.path.join(output_dir, filename)
            
            # Skip if already downloaded
            if os.path.exists(output_path):
                print(f"   ⏭️  Already exists: {filename}")
                return
            
            # Download
            print(f"   ⬇️  Downloading: {filename}")
            
            response = requests.get(download_url, timeout=60, stream=True)
            
            if response.status_code == 200:
                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                file_size = os.path.getsize(output_path) / (1024 * 1024)
                print(f"   ✅ Downloaded: {file_size:.2f}MB")
            else:
                print(f"   ❌ Failed: HTTP {response.status_code}")
                
                # Try alternative IPFS gateway
                if uri.startswith('ipfs://'):
                    print("   🔄 Trying alternative IPFS gateway...")
                    self.try_alternative_gateways(uri, output_path, filename)
        
        except Exception as e:
            print(f"   ❌ Download error: {e}")
    
    def try_alternative_gateways(self, ipfs_uri, output_path, filename):
        """Try alternative IPFS gateways if first one fails"""
        ipfs_hash = ipfs_uri.replace('ipfs://', '')
        
        for gateway in self.ipfs_gateways[1:]:  # Skip first one (already tried)
            try:
                url = gateway + ipfs_hash
                response = requests.get(url, timeout=60)
                
                if response.status_code == 200:
                    with open(output_path, 'wb') as f:
                        f.write(response.content)
                    print(f"   ✅ Success with alternative gateway")
                    return
            except:
                continue
        
        print(f"   ❌ All gateways failed")
    
    def get_extension_from_url(self, url):
        """Get file extension from URL"""
        # Common image/video extensions
        if '.png' in url.lower():
            return '.png'
        elif '.jpg' in url.lower() or '.jpeg' in url.lower():
            return '.jpg'
        elif '.gif' in url.lower():
            return '.gif'
        elif '.mp4' in url.lower():
            return '.mp4'
        elif '.webp' in url.lower():
            return '.webp'
        elif '.svg' in url.lower():
            return '.svg'
        else:
            return '.png'  # Default
    
    def sanitize_filename(self, filename):
        """Make filename safe for filesystem"""
        # Remove invalid characters
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        
        # Limit length
        if len(filename) > 200:
            filename = filename[:200]
        
        return filename


def main():
    print("\n" + "="*70)
    print("🎨 NFT COLLECTION DOWNLOADER")
    print("="*70)
    
    # Your wallet addresses
    TEZOS_WALLET = "tz1bkhCGUuA5bveCsMqXe9tEkopkZX3hiB9i"
    EVM_WALLET = "0x96a564fcf259101df654622fa796b50a31c77e2d"
    
    downloader = NFTDownloader(output_dir='my_nft_collection')
    
    print("\n📥 What would you like to download?")
    print("  1. Tezos NFTs only")
    print("  2. EVM NFTs only")
    print("  3. Both (recommended)")
    print("  4. Specific IPFS hash")
    
    choice = input("\nEnter choice (1-4) or press Enter for [3]: ").strip() or "3"
    
    if choice == "1":
        downloader.download_tezos_nfts(TEZOS_WALLET)
    elif choice == "2":
        downloader.download_evm_nfts(EVM_WALLET)
    elif choice == "3":
        downloader.download_tezos_nfts(TEZOS_WALLET)
        downloader.download_evm_nfts(EVM_WALLET)
    elif choice == "4":
        ipfs_hash = input("Enter IPFS hash (ipfs://QmXXX or just QmXXX): ").strip()
        if ipfs_hash:
            downloader.download_from_uri(ipfs_hash, 'my_nft_collection', 'downloaded_nft')
    
    print("\n" + "="*70)
    print("✅ DOWNLOAD COMPLETE!")
    print(f"📁 Files saved to: my_nft_collection/")
    print("="*70 + "\n")


if __name__ == '__main__':
    main()

