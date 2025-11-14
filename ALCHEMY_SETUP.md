# Setting Up Alchemy API Key for Ethereum NFTs

## 🔑 Quick Setup

### Step 1: Get Your Free Alchemy API Key

1. Go to: **https://www.alchemy.com/**
2. Click "Sign Up" (free account)
3. After login, click "Create App"
4. Settings:
   - **Chain**: Ethereum
   - **Network**: Mainnet
   - **Name**: NFT Downloader
5. Click "Create App"
6. Click "View Key" and copy your **API KEY**

### Step 2: Add Key to Config File

```bash
# Copy the example config
cp config.json.example config.json

# Edit it (use nano, vim, or any text editor)
nano config.json
```

Paste your key:
```json
{
  "alchemy_api_key": "YOUR_ACTUAL_KEY_HERE",
  "moralis_api_key": "",
  "opensea_api_key": ""
}
```

Save and exit (Ctrl+X, then Y, then Enter in nano)

### Step 3: Download Your Ethereum NFTs

```bash
source venv/bin/activate
python scripts/download_my_nfts.py
# Choose option 2 (EVM NFTs only) or 3 (Both)
```

---

## 🔐 Security

- ✅ `config.json` is in `.gitignore` (won't be committed to git)
- ✅ Your API key stays on your local machine
- ✅ Free tier is sufficient for personal use

---

## 💡 Alternative: No API Key Needed

If you don't want to get an API key, you can:

1. **Manually download from OpenSea:**
   - Visit: https://opensea.io/0x96a564fcf259101df654622fa796b50a31c77e2d
   - Right-click and save NFT images
   - Put them in `imported_images/`

2. **Use specific IPFS hashes:**
   ```bash
   python scripts/download_my_nfts.py
   # Choose option 4, paste IPFS hash
   ```

---

## ✅ What You Already Have

**Tezos NFTs:** 99 NFTs downloaded (487MB)
- All ready to glitch in `my_nft_collection/tezos/`

**Ethereum NFTs:** Waiting for API key
- Will download to `my_nft_collection/evm/`

---

Once you add your Alchemy key to `config.json`, the downloader will automatically use it!

