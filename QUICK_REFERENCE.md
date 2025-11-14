# Quick Reference Card

## 🚀 Essential Commands

### Setup (One Time)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Activate Venv (Every Session)
```bash
source venv/bin/activate
```

---

## 🎨 Quick Glitch Commands

### Simple Glitching
```bash
# Static glitch
python scripts/glitch_my_image.py imported_images/photo.jpg high

# Animated strobe
python scripts/glitch_animated.py imported_images/photo.jpg flash strobe

# Color pulse (reaper.gif style!)
python scripts/color_flash_overlay.py imported_images/photo.jpg pulse
```

### Advanced Effects
```bash
# Scraperboard + glitch
python scripts/scraperboard_effect.py imported_images/photo.jpg gothic
python scripts/glitch_animated.py examples_output/scraperboard_gothic_photo.png flash strobe

# Multi-overlay with colors
python scripts/glitch_random_overlay.py imported_images/base.jpg imported_images/overlay.png glitch

# Selective circular glitch
python scripts/glitch_advanced_animated.py imported_images/photo.jpg selective circle
```

---

## 📁 Project Structure

```
glitch/
├── src/                    # Core library
├── scripts/                # All glitch scripts ⭐
├── docs/                   # Documentation
├── imported_images/        # PUT SOURCE IMAGES HERE
├── examples_output/        # GENERATED ART APPEARS HERE
├── my_nft_collection/      # Downloaded NFTs
└── README.md              # Main guide
```

---

## 🎯 Effect Types

| Command | Effect |
|---------|--------|
| `glitch_my_image.py` | Simple static glitch |
| `glitch_animated.py` | Animated strobe/multi-effect |
| `color_flash_overlay.py` | Color pulsing overlay |
| `glitch_random_overlay.py` | Multi-overlay flashing |
| `glitch_advanced_animated.py` | Selective region effects |
| `scraperboard_effect.py` | Gothic etched style |
| `download_my_nfts.py` | Download your NFTs |

---

## 🏷️ Your Collection

**Name:** C0RRUPTED VISIONS & Digital Decay
**Collection:** https://objkt.com/collections/KT1DA5FSmsNmanEkE3qTPc8FzkoKC5vEb9MM

**Minted:**
- ✅ Genesis: multi_effect_DALLE2~4.gif
- ✅ #002: random_pluto.gif (Pluto underworld deity)
- ✅ #003: very_slow_overlay (Haunted Transmission)
- ✅ #004: slow_multi_overlay_6_colored (Pluto + Tezcatlipoca)

---

**For full documentation, see `docs/README.md`**

