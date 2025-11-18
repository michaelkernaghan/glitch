# NFT Ranker - Side-by-Side Comparison Tool

Rank your NFT collection by comparing two random NFTs at a time!

## 🎯 What It Does

1. **Shows 2 random NFTs** side by side
2. **You pick which is better**
3. **Builds ELO rankings** over time
4. **View ranked list** of all your NFTs

## 🚀 Quick Start

```bash
# From the glitch root directory
cd /home/michael-kernaghan/glitch
source venv/bin/activate
python nft_ranker/app.py
```

Then open in browser: **http://localhost:5000**

## ⌨️ Keyboard Shortcuts

- **Left Arrow** or **A** or **1** = Left NFT wins
- **Right Arrow** or **D** or **2** = Right NFT wins  
- **Space** or **S** = Skip this pair
- Click cards directly to select winner

## 🎨 How It Works

### ELO Rating System
- All NFTs start at **1500 ELO**
- Winner gains points, loser loses points
- More comparisons = more accurate ranking
- Upset wins gain more points

### Rankings
- Click "View Rankings" to see your top NFTs
- Shows: Rank, Name, ELO score, Win-Loss record
- Updates in real-time

## 📊 What NFTs Are Included

The ranker includes all images from:
- `my_nft_collection/tezos/` (99 NFTs)
- `my_nft_collection/evm/` (9 NFTs)
- `imported_images/` (your source images)

**Total:** ~110+ items to rank

## 💡 Strategy

### Quick Ranking (30-50 comparisons)
- Get rough idea of top tier
- 30-40 comparisons gives good initial ranking

### Accurate Ranking (100+ comparisons)
- More comparisons = more accuracy
- ~100 comparisons for solid ranking
- ~200+ for very accurate

### What to Consider When Picking

**Artistic Merit:**
- Composition
- Color palette
- Emotional impact
- Technical execution

**NFT Value:**
- Rarity
- Collection significance
- Personal meaning
- Glitch effectiveness (for your glitched pieces)

## 📁 Data Storage

Rankings saved in: `nft_ranker/rankings.json`
- Automatically saves after each comparison
- Persists between sessions
- Can be backed up/shared

## 🎯 Use Cases

### 1. **Curate Your Collection**
Find your best NFTs to feature

### 2. **Choose Pieces for Competitions**
Identify top pieces for RED competition, Lumen Prize, etc.

### 3. **Build Your Portfolio**
Know which 10-15 pieces to showcase

### 4. **Decide What to Mint**
Rank your glitched variations before minting

### 5. **Social Media**
Know which pieces to promote first

## 🔧 Troubleshooting

**"Images not loading"**
- Make sure you're running from glitch root directory
- Check file paths are correct

**"No NFTs found"**
- Ensure NFTs are in `my_nft_collection/` folders
- Check images have .png, .jpg, .gif extensions

**"Port already in use"**
- Change port in app.py: `app.run(port=5001)`

## 💾 Backup Your Rankings

```bash
# Backup rankings
cp nft_ranker/rankings.json nft_ranker/rankings_backup.json

# Restore from backup
cp nft_ranker/rankings_backup.json nft_ranker/rankings.json
```

## 🎨 Dark Theme

The interface matches your C0RRUPTED VISIONS aesthetic:
- Black background
- Magenta/pink accents (#ff0066)
- Green highlights for winners
- Glitch-inspired typography
- Cyberpunk underground vibe

---

**Start ranking and discover your best NFTs!** 🏆💀✨

