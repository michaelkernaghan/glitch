# Scripts Guide

All glitch art generation scripts in one place!

## 🚀 Quick Reference

Always activate venv first:
```bash
source venv/bin/activate
```

## 📜 Available Scripts

### **Basic Glitching**

#### `glitch_my_image.py` - Simple glitching
```bash
python scripts/glitch_my_image.py imported_images/image.jpg [low|medium|high]
```
- Easiest way to glitch any image
- Choose intensity: low, medium (default), high
- Output: `examples_output/glitched_*.png`

#### `advanced_glitch.py` - Choose specific effects
```bash
python scripts/advanced_glitch.py imported_images/image.jpg [interactive|presets]
```
- Interactive: Choose which effect to apply
- Presets: Vaporwave, Cyberpunk, Minimal, Chaotic, Retro

---

### **Animations**

#### `glitch_animated.py` - Animated glitch effects
```bash
python scripts/glitch_animated.py <image> flash <pattern>
python scripts/glitch_animated.py <image> multi
python scripts/glitch_animated.py <image.gif> glitch-gif
```
**Flash patterns:** alternate, random, progressive, strobe
- Output: `examples_output/animated_*.gif` or `multi_effect_*.gif`

#### `glitch_advanced_animated.py` - Selective glitching
```bash
python scripts/glitch_advanced_animated.py <image> selective <region>
python scripts/glitch_advanced_animated.py <image> colorflash <region>
python scripts/glitch_advanced_animated.py <image> colorshift <region>
python scripts/glitch_advanced_animated.py <image> overlay <overlay_image>
```
**Regions:** center, circle, left, right, top, bottom, edges

#### `glitch_random_overlay.py` - Multi-overlay animations
```bash
python scripts/glitch_random_overlay.py <base> <overlay> [glitch|static]
```
- Overlay flashes in random positions
- Base can glitch or stay static
- Output: `examples_output/random_overlay_*.gif`

#### `color_flash_overlay.py` - Color pulsing effects
```bash
python scripts/color_flash_overlay.py <image> [pulse|flash|wave|random|glitch]
```
- **pulse**: Like reaper.gif! Purple/magenta pulsing
- **flash**: Fast on/off flashing
- **wave**: Smooth color transitions
- **glitch**: Combined glitch + color pulse
- Output: `examples_output/color_flash_*.gif`

---

### **Special Effects**

#### `scraperboard_effect.py` - Gothic etched style
```bash
python scripts/scraperboard_effect.py <image> [dark|light|gothic|crosshatch] [low|medium|high]
```
- Creates Victorian engraving/etched look
- Perfect for dark art themes
- Output: `examples_output/scraperboard_*.png`

---

### **Utilities**

#### `download_my_nfts.py` - Download your NFT collection
```bash
python scripts/download_my_nfts.py
```
- Downloads NFTs from your Tezos & EVM wallets
- Your addresses pre-configured
- Output: `my_nft_collection/tezos/` and `my_nft_collection/evm/`

---

### **Examples**

#### `example_basic.py` - Basic tutorial examples
```bash
python scripts/example_basic.py
```
- Creates 7 basic effect examples
- Good for learning

#### `example_advanced.py` - Advanced collections
```bash
python scripts/example_advanced.py
```
- Creates themed collections
- Rarity tiers demonstration
- Professional NFT techniques

---

## 🎯 Common Workflows

### Quick Single Glitch
```bash
source venv/bin/activate
python scripts/glitch_my_image.py imported_images/photo.jpg high
```

### Animated Strobe Effect
```bash
source venv/bin/activate
python scripts/glitch_animated.py imported_images/photo.jpg flash strobe
```

### Color Pulse (Reaper.gif Style)
```bash
source venv/bin/activate
python scripts/color_flash_overlay.py imported_images/photo.jpg pulse
```

### Scraperboard + Glitch
```bash
source venv/bin/activate
python scripts/scraperboard_effect.py imported_images/photo.jpg gothic
python scripts/glitch_animated.py examples_output/scraperboard_gothic_photo.png flash strobe
```

### Multi-Overlay with Color Shift
```bash
source venv/bin/activate
python scripts/glitch_random_overlay.py imported_images/base.jpg imported_images/overlay.png glitch
```

### Download Your NFTs
```bash
source venv/bin/activate
python scripts/download_my_nfts.py
```

---

## 💡 Tips

- **Always activate venv first:** `source venv/bin/activate`
- **File paths matter:** Use `imported_images/` for sources
- **Check output:** Files go to `examples_output/`
- **Experiment:** Try different parameters!

---

See individual guides in `../docs/` for detailed documentation on each effect!

