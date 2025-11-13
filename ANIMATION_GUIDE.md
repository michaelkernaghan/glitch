# Animated Glitch Art Guide 🎬

Create flashing, strobing, and animated glitch effects!

## 🚀 Quick Start

```bash
# Simple flashing effect (original ↔ glitched)
python glitch_animated.py imported_images/your_image.jpg

# Fast strobe effect (like your artifact.gif!)
python glitch_animated.py imported_images/your_image.jpg flash strobe

# Flash through different glitch effects
python glitch_animated.py imported_images/your_image.jpg multi

# Glitch an existing GIF
python glitch_animated.py imported_images/your_animation.gif glitch-gif
```

## 🎨 Animation Modes

### 1. Flash Mode (Default)

Flashing effect with different patterns:

```bash
# Alternate: Original ↔ Same glitched image
python glitch_animated.py image.jpg flash alternate

# Random: Original ↔ Different random glitches each flash
python glitch_animated.py image.jpg flash random

# Progressive: Original → Low → Medium → High intensity
python glitch_animated.py image.jpg flash progressive

# Strobe: Fast flashing with random glitch types
python glitch_animated.py image.jpg flash strobe
```

**Best for**: Creating that rapid flashing/artifact effect

### 2. Multi-Effect Mode

Cycles through different specific glitch effects:
- Original
- RGB Shift
- Original
- Pixel Sort
- Original
- Data Mosh
- Original  
- Slice & Shift

```bash
python glitch_animated.py image.jpg multi
```

**Best for**: Showcasing different glitch styles

### 3. Glitch-GIF Mode

Takes an existing animated GIF and glitches each frame:

```bash
# Low intensity (subtle)
python glitch_animated.py animation.gif glitch-gif low

# Medium intensity
python glitch_animated.py animation.gif glitch-gif medium

# High intensity (extreme)
python glitch_animated.py animation.gif glitch-gif high
```

**Best for**: Adding glitch effects to existing animations

## 🎯 What You Created

### From your DALL-E image:

1. **animated_DALLE2~4.gif** (17MB) - Random flashing effect
   - 20 frames, different glitch each flash
   - 100ms per frame = fast flashing

2. **multi_effect_DALLE2~4.gif** (6.2MB) - Cycling through effects
   - 8 frames showing different glitch types
   - 150ms per frame = smooth cycling

### From your artifact.gif:

3. **glitched_artifact.gif** (50MB) - Each frame glitched
   - All 120 original frames with glitch effects added
   - Maintains original timing

## ⚙️ Customization

Edit `glitch_animated.py` to customize:

### Frame Count & Speed

```python
create_flashing_glitch(
    input_file, 
    frames=20,        # More frames = longer animation
    duration=100,     # Lower = faster (milliseconds per frame)
    flash_intensity='medium',  # 'low', 'medium', 'high'
    flash_pattern='strobe'     # See patterns above
)
```

### Speed Guide

- **50ms** = Very fast strobe (20 FPS)
- **100ms** = Fast flash (10 FPS) ← Default
- **150ms** = Medium speed (6.7 FPS)
- **200ms** = Slower flash (5 FPS)
- **500ms** = Slow transition (2 FPS)

## 💡 Tips for NFTs

### Optimal GIF Settings

```python
# For Twitter/social media (file size limits)
frames=10-15
duration=100
# Result: ~5-10MB

# For OpenSea/NFT platforms
frames=20-30
duration=80-100
# Result: ~10-20MB

# For maximum quality
frames=30-60
duration=50-100
# Result: 20-50MB
```

### Style Recommendations

**Cyberpunk/Tech Art**:
```bash
python glitch_animated.py image.jpg flash strobe
```

**Vaporwave/Retro**:
```bash
python glitch_animated.py image.jpg flash progressive
```

**Experimental/Avant-garde**:
```bash
python glitch_animated.py image.jpg flash random
```

**Clean/Professional**:
```bash
python glitch_animated.py image.jpg multi
```

## 🎬 Advanced: Custom Patterns

Edit `glitch_animated.py` and add your own pattern:

```python
elif flash_pattern == 'my_custom':
    for i in range(frames):
        glitcher = GlitchArtist(image=original.copy())
        
        # Your custom logic here
        if i < 5:
            glitcher.rgb_shift(r_shift=(i*5, 0))
        else:
            glitcher.pixel_sort(threshold=150-i*10)
        
        frame_list.append(glitcher.get_image())
```

Then use it:
```bash
python glitch_animated.py image.jpg flash my_custom
```

## 📊 File Size Considerations

Animated GIFs can get large:
- **10 frames @ 1024x1024**: ~5-10MB
- **20 frames @ 1024x1024**: ~10-20MB  
- **100+ frames**: 30-100MB+

To reduce file size:
1. Reduce frame count
2. Resize images before animating
3. Use fewer colors (add `optimize=True` in save)
4. Consider converting to video (MP4) for very long animations

## 🔧 Troubleshooting

**"GIF is too large"**
- Reduce `frames` parameter
- Resize image before processing
- Use shorter animations

**"Animation is too fast/slow"**
- Adjust `duration` parameter
- 100ms = good default
- Lower = faster, Higher = slower

**"Not enough glitch effect"**
- Change intensity to 'high'
- Use 'strobe' or 'random' patterns
- Edit specific effect parameters in the code

## 🎨 Examples from Your Images

```bash
# Create fast strobing like artifact.gif
python glitch_animated.py imported_images/DALLE2~4.PNG flash strobe

# Smooth cycling through effects
python glitch_animated.py imported_images/DALLE2~4.PNG multi

# Glitch your artifact.gif even more!
python glitch_animated.py imported_images/artifact.gif glitch-gif medium
```

---

**Pro Tip**: Animated glitch GIFs are perfect for:
- NFT profile pictures
- Social media posts
- Digital art collections
- Music visualizers
- VJ loops

Happy animating! 🎬✨

