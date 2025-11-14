# Digital Scraperboard Effect Guide 🖤

Transform your images into high-contrast scraperboard/scratchboard art - perfect for gothic, dark, and occult themes!

## 🎨 What is Scraperboard?

Traditional scraperboard is black ink over white clay that artists scratch away to reveal white lines underneath. The result is:
- High contrast black and white
- Etched/engraved appearance
- Detailed line work
- Gothic/Victorian aesthetic
- Perfect for dark/underground art

## 🚀 Quick Start

```bash
# Gothic style (heavy blacks, dramatic)
python scraperboard_effect.py imported_images/your_image.jpg gothic

# Dark style (white lines on black) - customizable detail
python scraperboard_effect.py imported_images/your_image.jpg dark high

# Crosshatch style (shading with lines)
python scraperboard_effect.py imported_images/your_image.jpg crosshatch

# Light style (black lines on white)
python scraperboard_effect.py imported_images/your_image.jpg light
```

## 🎭 Available Styles

### 1. Gothic (Recommended for Dark Art)
```bash
python scraperboard_effect.py image.jpg gothic
```
- **Heavy blacks** with fine white details
- Maximum contrast (3x enhancement)
- Darkened overall
- Perfect for: Skulls, occult imagery, death gods
- Output: Dramatic, underground aesthetic

### 2. Dark (Customizable Detail)
```bash
python scraperboard_effect.py image.jpg dark high
python scraperboard_effect.py image.jpg dark medium
python scraperboard_effect.py image.jpg dark low
```
- White lines on black background
- Three detail levels:
  - **high**: Maximum line detail, intricate
  - **medium**: Balanced
  - **low**: Bold, simple lines
- Perfect for: All dark art, customizable intensity

### 3. Crosshatch
```bash
python scraperboard_effect.py image.jpg crosshatch
```
- Traditional crosshatch shading
- Perpendicular lines for depth
- Classic engraving look
- Perfect for: Portrait-style work, classic art

### 4. Light (Inverse)
```bash
python scraperboard_effect.py image.jpg light high
```
- Black lines on white background
- Traditional scraperboard look
- Perfect for: Printing, lighter themes

## 🔥 Combining with Glitch Effects

### Workflow 1: Scraperboard → Glitch (Static)
```bash
# 1. Create scraperboard
python scraperboard_effect.py imported_images/skull.jpg gothic

# 2. Glitch it
python glitch_my_image.py examples_output/scraperboard_gothic_skull.png high
```

### Workflow 2: Scraperboard → Animated Glitch
```bash
# 1. Create scraperboard
python scraperboard_effect.py imported_images/deity.jpg gothic

# 2. Animate with glitches
python glitch_animated.py examples_output/scraperboard_gothic_deity.png flash strobe

# Or multi-effect
python glitch_animated.py examples_output/scraperboard_gothic_deity.png multi
```

### Workflow 3: Scraperboard → Selective Glitch
```bash
# 1. Create scraperboard
python scraperboard_effect.py imported_images/occult.jpg dark high

# 2. Selective glitch animation
python glitch_advanced_animated.py examples_output/scraperboard_dark_occult.png selective circle
```

### Workflow 4: Scraperboard → Overlay Effects
```bash
# 1. Create scraperboard base
python scraperboard_effect.py imported_images/base.jpg gothic

# 2. Add color-shifting overlays
python glitch_random_overlay.py examples_output/scraperboard_gothic_base.png imported_images/overlay.png
```

## 💀 Perfect For Dark Art NFTs

### Why Scraperboard + Glitch Works:

1. **High Contrast Base**
   - Pure blacks and whites = dramatic glitches
   - RGB shifts are more visible
   - Data corruption stands out

2. **Gothic Aesthetic**
   - Already looks hand-carved/underground
   - Victorian engraving + digital corruption = unique
   - Perfect for occult/death themes

3. **Line Detail**
   - Fine lines break beautifully when glitched
   - Pixel sorting creates interesting patterns
   - Slice effects fragment the etched lines

4. **Underground Vibe**
   - Scraperboard = DIY/punk aesthetic
   - Combined with glitch = cyberpunk meets Victorian
   - Unique in NFT space

## 🎯 Recommended Combinations

### For Skulls/Death Imagery:
```bash
python scraperboard_effect.py skull.jpg gothic
python glitch_animated.py examples_output/scraperboard_gothic_skull.png flash strobe
```

### For Deities/Occult:
```bash
python scraperboard_effect.py deity.jpg dark high
python glitch_advanced_animated.py examples_output/scraperboard_dark_deity.png selective center
```

### For Complex Imagery:
```bash
python scraperboard_effect.py image.jpg crosshatch
python glitch_animated.py examples_output/scraperboard_crosshatch_image.png multi
```

## 🎨 Examples Created

From your pluto.jpg, we created:
- `scraperboard_gothic_pluto.png` - Heavy blacks, dramatic
- `scraperboard_dark_pluto.png` - High detail white lines
- `scraperboard_crosshatch_pluto.png` - Traditional crosshatch

All ready to be glitched!

## ⚙️ Technical Details

### What the Script Does:

1. **Converts to grayscale**
2. **Enhances contrast** (2-3x)
3. **Edge detection** (Canny algorithm)
4. **Threshold conversion** (high contrast black/white)
5. **Combines edges + threshold**
6. **Adds scratch texture** for authenticity
7. **Inverts if needed** (dark vs light style)

### Parameters You Can Adjust:

Edit `scraperboard_effect.py` to customize:
- **Contrast enhancement**: Line 47 `enhance(2.0)` - higher = more contrast
- **Edge sensitivity**: Lines 53-60 Canny values - lower = more lines
- **Threshold**: Line 65 `threshold=128` - adjust split point
- **Scratch density**: Lines 100-104 `num_scratches` - more = grainier

## 💡 Pro Tips

### Best Source Images:
- ✅ High contrast photos
- ✅ Clear subjects (portraits, skulls, symbols)
- ✅ Dark/gothic themes
- ✅ Detailed imagery
- ❌ Avoid: Very busy/noisy images

### Detail Level Guide:
- **High detail**: Complex imagery, fine features
- **Medium detail**: Balanced, most images
- **Low detail**: Bold graphics, logos, simple shapes

### Glitch Recommendations:
- **RGB Shift**: Creates color separation on white lines
- **Pixel Sort**: Streams the etched lines beautifully
- **Data Mosh**: Breaks the carved pattern dramatically
- **Slice & Shift**: Fragments like broken engravings

## 🖤 NFT Collection Ideas

### "Etched Corruption" Series:
1. Convert dark images to scraperboard (gothic style)
2. Apply different glitch patterns to each
3. Maintain scraperboard aesthetic with digital corruption
4. Underground Victorian cyberpunk vibe

### "Carved Chaos" Series:
1. Use crosshatch style for classic look
2. Animate with multi-effect glitches
3. Traditional engraving meets modern glitch

### "Dark Engravings" Series:
1. Dark style with high detail
2. Selective glitching (keep some areas clean)
3. Emphasizes hand-carved + digital hybrid

## 🔧 Troubleshooting

**"Too much black/not enough detail"**
- Use `dark high` instead of `gothic`
- Lower the threshold value in code
- Try crosshatch mode

**"Not enough contrast"**
- Gothic mode has maximum contrast
- Increase contrast enhancement in code
- Use higher quality source images

**"Lines too thick/thin"**
- Adjust detail level (`low`, `medium`, `high`)
- Modify Canny edge detection values
- Change kernel size in code

## 🎬 Complete Workflow Example

```bash
# 1. Start with dark art image
# imported_images/death_god.jpg

# 2. Convert to scraperboard
python scraperboard_effect.py imported_images/death_god.jpg gothic

# 3. Create static glitched version
python glitch_my_image.py examples_output/scraperboard_gothic_death_god.png high

# 4. Create animated version
python glitch_animated.py examples_output/scraperboard_gothic_death_god.png flash strobe

# 5. Create selective glitch version
python glitch_advanced_animated.py examples_output/scraperboard_gothic_death_god.png selective circle

# Result: 3 unique pieces from one image!
```

---

**The combination of scraperboard + glitch is PERFECT for underground dark art NFTs!** 🖤💀⚡

Traditional Victorian engraving aesthetic + modern digital corruption = unique, underground, cyberpunk gothic art.

Try it with your occult/death deity images! 🔥

