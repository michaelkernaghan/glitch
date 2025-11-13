# Glitch Art for NFTs - Complete Guide

Welcome to your glitch art creation toolkit! This guide will teach you how to create stunning computer-generated glitch art perfect for NFT collections.

## 🎨 What is Glitch Art?

Glitch art is a visual art style that embraces digital errors, artifacts, and distortions as aesthetic elements. It originated from corrupted digital files, compression artifacts, and hardware malfunctions. In the NFT space, glitch art has become incredibly popular due to its unique, digital-native aesthetic.

## 📦 Installation

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

### Run All Examples

The fastest way to see what's possible:

```bash
python example_basic.py
```

This will generate 10+ example images showing different glitch techniques.

### Create Your First Glitch Art

```python
from glitch_effects import GlitchArtist
from generative_glitch import GenerativeGlitchArt

# Generate a base image
generator = GenerativeGlitchArt(800, 600)
base = generator.create_vaporwave_aesthetic()

# Apply glitch effects
glitcher = GlitchArtist(image=base)
glitcher.rgb_shift(r_shift=(20, 0), b_shift=(-20, 0))
glitcher.pixel_sort(threshold=128)
glitcher.save('my_first_glitch.png')
```

## 🎭 Glitch Effects Explained

### 1. **Pixel Sorting**

Sorts pixels by brightness, creating distinctive streaking effects.

```python
glitcher.pixel_sort(
    threshold=128,      # Brightness threshold (0-255)
    direction='horizontal',  # or 'vertical'
    reverse=False       # Reverse sort order
)
```

**Best for:** Creating flowing, organic distortions
**NFT tip:** Works great with gradients and portraits

### 2. **RGB Channel Shift** (Chromatic Aberration)

Separates and shifts color channels to create a "3D glasses" effect.

```python
glitcher.rgb_shift(
    r_shift=(20, 0),    # Shift red channel right 20px
    g_shift=(0, 0),     # Keep green in place
    b_shift=(-20, 0)    # Shift blue channel left 20px
)
```

**Best for:** Adding depth and retro-futuristic vibes
**NFT tip:** Subtle shifts (5-15px) look professional

### 3. **Data Moshing**

Simulates data corruption by randomly corrupting image blocks.

```python
glitcher.data_mosh(
    corruption_rate=0.01,  # 1% of blocks corrupted
    block_size=10          # Size of corruption blocks
)
```

**Best for:** Chaotic, unpredictable effects
**NFT tip:** Lower corruption rates (0.005-0.02) maintain recognizability

### 4. **Scan Lines**

Adds CRT monitor-style horizontal lines.

```python
glitcher.scan_lines(
    line_height=2,      # Height of each scan line
    intensity=0.3       # Darkness (0-1)
)
```

**Best for:** Retro, nostalgic aesthetics
**NFT tip:** Combine with vaporwave colors

### 5. **Wave Distortion**

Creates sine wave distortions across the image.

```python
glitcher.wave_distortion(
    amplitude=10,       # Wave height in pixels
    frequency=0.05,     # Wave frequency
    direction='horizontal'
)
```

**Best for:** Liquid, flowing effects
**NFT tip:** Low frequency (0.01-0.1) looks more natural

### 6. **Slice and Shift**

Cuts the image into horizontal slices and shifts them randomly.

```python
glitcher.slice_and_shift(
    num_slices=10,      # Number of slices
    max_shift=50        # Maximum shift in pixels
)
```

**Best for:** Broken, fragmented aesthetics
**NFT tip:** Great for creating "glitched out" text

### 7. **JPEG Compression Artifacts**

Creates compression artifacts by repeatedly compressing the image.

```python
glitcher.jpeg_compression_artifacts(
    quality=5,          # JPEG quality (1-100, lower = more artifacts)
    iterations=3        # Number of compression cycles
)
```

**Best for:** Degraded, lo-fi aesthetics
**NFT tip:** Subtle effect, best combined with others

### 8. **Color Channel Swap**

Swaps RGB color channels for surreal color effects.

```python
glitcher.color_channel_swap(
    swap_type='random'  # or 'rgb_to_bgr', 'rgb_to_gbr', etc.
)
```

**Best for:** Psychedelic, unexpected colors
**NFT tip:** Creates instant visual impact

## 🎨 Generative Art Styles

### Vaporwave Aesthetic

```python
generator = GenerativeGlitchArt(1000, 1000)
base = generator.create_vaporwave_aesthetic()
```

**Characteristics:**
- Pink, cyan, and magenta color palette
- Grid overlays
- Retro 80s/90s vibes
- Perfect for nostalgic NFT collections

### Cyberpunk Aesthetic

```python
base = generator.create_cyberpunk_aesthetic()
```

**Characteristics:**
- Dark backgrounds with neon accents
- Cyan, magenta, yellow neon colors
- Tech-noir atmosphere
- Great for futuristic NFT themes

### Geometric Abstract

```python
base = generator.create_geometric_base(num_shapes=50)
```

**Characteristics:**
- Random shapes and patterns
- Abstract compositions
- Highly varied outputs
- Excellent for generative collections

### Gradient Base

```python
base = generator.create_base_gradient(
    colors=[(255, 0, 0), (0, 0, 255)]  # Red to blue
)
```

**Characteristics:**
- Smooth color transitions
- Clean, minimal base
- Works well with pixel sorting

### Noise Base

```python
base = generator.create_noise_base(noise_type='perlin')
```

**Characteristics:**
- Textured, organic patterns
- Good for abstract art
- Types: 'color', 'grayscale', 'perlin'

## 🖼️ Creating NFT Collections

### Generate a Complete Collection

```python
from generative_glitch import generate_nft_collection

generate_nft_collection(
    num_pieces=100,              # Number of NFTs
    output_dir='./my_collection',
    width=1000,                  # Standard NFT size
    height=1000
)
```

### Generate Unique, Reproducible Pieces

```python
# Using seeds ensures you can recreate the same piece
generator = GenerativeGlitchArt(1000, 1000)
base = generator.generate_unique_nft(
    seed=42,            # Same seed = same output
    style='vaporwave'   # or 'cyberpunk', 'geometric', etc.
)
```

## 💡 Pro Tips for NFT Artists

### 1. **Maintain Uniqueness**

```python
# Use different seeds for each piece
for i in range(100):
    generator = GenerativeGlitchArt(1000, 1000)
    base = generator.generate_unique_nft(seed=i)
    # Each piece will be unique but reproducible
```

### 2. **Create Rarity Tiers**

```python
# Common: Low intensity glitches
glitcher.random_glitch_combo(intensity='low')

# Rare: Medium intensity
glitcher.random_glitch_combo(intensity='medium')

# Legendary: High intensity
glitcher.random_glitch_combo(intensity='high')
```

### 3. **Combine Effects Strategically**

```python
# Good combination: Subtle and professional
glitcher.rgb_shift(r_shift=(5, 0), b_shift=(-5, 0))
glitcher.scan_lines(intensity=0.2)
glitcher.wave_distortion(amplitude=5, frequency=0.03)

# Bold combination: High impact
glitcher.slice_and_shift(num_slices=20, max_shift=100)
glitcher.data_mosh(corruption_rate=0.03)
glitcher.color_channel_swap(swap_type='random')
```

### 4. **Optimize for NFT Marketplaces**

```python
# Standard NFT dimensions
sizes = [
    (1000, 1000),  # Square (most common)
    (1080, 1080),  # Instagram-friendly
    (2048, 2048),  # High resolution
]

# Save with high quality
glitcher.save('nft.png', quality=95)
```

### 5. **Create Themed Collections**

```python
# Example: "Cyber Dreams" collection
themes = ['cyberpunk'] * 50 + ['vaporwave'] * 30 + ['geometric'] * 20

for i, theme in enumerate(themes):
    generator = GenerativeGlitchArt(1000, 1000)
    base = generator.generate_unique_nft(seed=i, style=theme)
    
    glitcher = GlitchArtist(image=base)
    glitcher.random_glitch_combo(intensity='medium')
    glitcher.save(f'cyber_dreams_{i:04d}.png')
```

## 🎓 Advanced Techniques

### Method Chaining

The `GlitchArtist` class supports method chaining for clean, readable code:

```python
(GlitchArtist(image=base)
    .rgb_shift(r_shift=(10, 0))
    .pixel_sort(threshold=150)
    .scan_lines(intensity=0.3)
    .data_mosh(corruption_rate=0.01)
    .save('advanced_glitch.png'))
```

### Custom Color Palettes

```python
# Create your own color scheme
custom_colors = [
    (255, 0, 128),    # Hot pink
    (0, 255, 255),    # Cyan
    (128, 0, 255),    # Purple
]

generator = GenerativeGlitchArt(1000, 1000)
base = generator.create_base_gradient(colors=custom_colors)
```

### Conditional Glitching

```python
import random

# Apply different effects based on conditions
if random.random() > 0.5:
    glitcher.pixel_sort(direction='horizontal')
else:
    glitcher.pixel_sort(direction='vertical')

# Create rarity through probability
if random.random() > 0.9:  # 10% chance
    glitcher.color_channel_swap(swap_type='random')  # Rare effect
```

### Glitching Existing Images

```python
# Glitch your own photos or artwork
glitcher = GlitchArtist(image_path='my_photo.jpg')
glitcher.random_glitch_combo(intensity='medium')
glitcher.save('glitched_photo.png')
```

## 📊 Recommended Settings by Style

### Minimal Glitch
```python
glitcher.rgb_shift(r_shift=(3, 0), b_shift=(-3, 0))
glitcher.scan_lines(line_height=2, intensity=0.2)
```

### Vaporwave
```python
generator.create_vaporwave_aesthetic()
glitcher.pixel_sort(threshold=120, direction='horizontal')
glitcher.scan_lines(line_height=3, intensity=0.3)
```

### Cyberpunk
```python
generator.create_cyberpunk_aesthetic()
glitcher.rgb_shift(r_shift=(15, 0), b_shift=(-15, 0))
glitcher.data_mosh(corruption_rate=0.015, block_size=12)
```

### Abstract/Chaotic
```python
glitcher.slice_and_shift(num_slices=25, max_shift=150)
glitcher.data_mosh(corruption_rate=0.03, block_size=20)
glitcher.color_channel_swap(swap_type='random')
```

### Retro/Nostalgic
```python
glitcher.jpeg_compression_artifacts(quality=10, iterations=5)
glitcher.scan_lines(line_height=2, intensity=0.4)
glitcher.wave_distortion(amplitude=8, frequency=0.04)
```

## 🛠️ Workflow Examples

### Workflow 1: Quick Single Piece

```python
from glitch_effects import GlitchArtist
from generative_glitch import GenerativeGlitchArt

# Generate and glitch in one go
generator = GenerativeGlitchArt(1000, 1000)
base = generator.create_vaporwave_aesthetic()

GlitchArtist(image=base).random_glitch_combo('high').save('quick_glitch.png')
```

### Workflow 2: Iterative Experimentation

```python
# Create base once
generator = GenerativeGlitchArt(1000, 1000)
base = generator.create_cyberpunk_aesthetic()

# Try different effects
glitcher = GlitchArtist(image=base)

# Version 1
glitcher.pixel_sort(threshold=100).save('version_1.png')

# Version 2 (reset first)
glitcher.reset().rgb_shift(r_shift=(20, 0)).save('version_2.png')

# Version 3
glitcher.reset().data_mosh(corruption_rate=0.02).save('version_3.png')
```

### Workflow 3: Batch Processing

```python
import os

# Process multiple base images
base_images = ['base1.png', 'base2.png', 'base3.png']

for img_path in base_images:
    glitcher = GlitchArtist(image_path=img_path)
    glitcher.random_glitch_combo(intensity='medium')
    
    filename = os.path.basename(img_path)
    glitcher.save(f'glitched_{filename}')
```

## 🎯 NFT Marketplace Considerations

### File Formats
- **PNG**: Best for glitch art (lossless, supports transparency)
- **JPEG**: Smaller file size but adds compression artifacts
- **GIF**: For animated glitch art (not covered in this toolkit)

### File Sizes
- Most marketplaces accept up to 50-100MB
- Aim for 1000x1000 to 2048x2048 pixels
- Use `quality=95` for PNG to balance quality and size

### Metadata
When minting NFTs, include:
- **Title**: Descriptive and unique
- **Description**: Explain the glitch techniques used
- **Attributes**: Style, intensity, color palette, effects used
- **Seed**: For provenance and reproducibility

## 🐛 Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### Images look too corrupted
- Reduce `corruption_rate` in `data_mosh()`
- Use `intensity='low'` or `'medium'` in `random_glitch_combo()`
- Reduce shift amounts in `rgb_shift()` and `slice_and_shift()`

### Not enough glitch effect
- Increase intensity parameters
- Combine multiple effects
- Use `random_glitch_combo(intensity='high')`

### Colors look wrong
- Check if image is in RGB mode: `image.convert('RGB')`
- Verify color values are in 0-255 range
- Try different color palettes

## 📚 Further Learning

### Glitch Art Concepts
- **Databending**: Manipulating file data directly
- **Circuit bending**: Hardware manipulation (not covered here)
- **Compression artifacts**: JPEG, video codec artifacts
- **Pixel sorting**: Kim Asendorf's technique

### NFT Resources
- Research successful glitch art NFT collections
- Study color theory for better palettes
- Learn about generative art algorithms
- Understand NFT marketplace requirements

## 🎨 Example Gallery

Run the examples to see:
- `output_pixel_sort.png` - Pixel sorting effect
- `output_rgb_shift.png` - Chromatic aberration
- `output_data_mosh.png` - Data corruption
- `output_combined.png` - Multiple effects
- `output_random_glitch.png` - Random combination
- `nft_sample_*.png` - NFT-ready pieces

## 🚀 Next Steps

1. **Experiment**: Run `python example_basic.py` and study the outputs
2. **Customize**: Modify parameters to create your own style
3. **Generate**: Create a small collection (10-20 pieces)
4. **Refine**: Iterate on your favorite pieces
5. **Mint**: Prepare your best work for NFT marketplaces

## 📝 License & Usage

This toolkit is for educational and commercial use. Feel free to:
- Create and sell NFTs using this code
- Modify and extend the effects
- Use in your own projects

**Note**: When selling NFTs, ensure you have rights to any base images you use. The generative bases created by this toolkit are yours to use freely.

## 🤝 Contributing

Ideas for extending this toolkit:
- Add animated glitch effects (GIF/video)
- Implement more advanced noise algorithms
- Add text/typography glitch effects
- Create preset collections (80s, Y2K, etc.)
- Add batch processing GUI

---

**Happy Glitching! 🎨✨**

For questions or issues, experiment with different parameters and combinations. The beauty of glitch art is in the unexpected results!

