# Quick Start Guide - Glitch Art for NFTs

Get started creating glitch art in 5 minutes!

## Installation

```bash
pip install -r requirements.txt
```

## Your First Glitch Art (3 lines of code!)

```python
from glitch_effects import GlitchArtist
from generative_glitch import GenerativeGlitchArt

# Generate base → Apply glitch → Save
base = GenerativeGlitchArt(1000, 1000).create_vaporwave_aesthetic()
GlitchArtist(image=base).random_glitch_combo('high').save('my_glitch.png')
```

Run it:
```bash
python -c "from glitch_effects import GlitchArtist; from generative_glitch import GenerativeGlitchArt; base = GenerativeGlitchArt(1000, 1000).create_vaporwave_aesthetic(); GlitchArtist(image=base).random_glitch_combo('high').save('my_glitch.png')"
```

## See All Examples

```bash
# Basic examples (7 different techniques)
python example_basic.py

# Advanced examples (professional NFT collections)
python example_advanced.py
```

## Generate an NFT Collection

```python
from generative_glitch import generate_nft_collection

generate_nft_collection(
    num_pieces=100,
    output_dir='./my_nft_collection'
)
```

## Popular Styles

### Vaporwave
```python
base = GenerativeGlitchArt(1000, 1000).create_vaporwave_aesthetic()
GlitchArtist(image=base).pixel_sort().scan_lines().save('vaporwave.png')
```

### Cyberpunk
```python
base = GenerativeGlitchArt(1000, 1000).create_cyberpunk_aesthetic()
GlitchArtist(image=base).rgb_shift(r_shift=(20,0), b_shift=(-20,0)).save('cyber.png')
```

### Chaotic
```python
base = GenerativeGlitchArt(1000, 1000).create_geometric_base(num_shapes=100)
GlitchArtist(image=base).data_mosh().slice_and_shift().save('chaos.png')
```

## Glitch Your Own Images

```python
GlitchArtist(image_path='my_photo.jpg').random_glitch_combo('medium').save('glitched.png')
```

## Next Steps

Read the full [README.md](README.md) for:
- Detailed effect explanations
- NFT collection strategies
- Rarity tier creation
- Color palette tips
- Pro techniques

## Common Effects

| Effect | Code | Best For |
|--------|------|----------|
| RGB Shift | `.rgb_shift(r_shift=(20,0))` | Chromatic aberration |
| Pixel Sort | `.pixel_sort(threshold=128)` | Flowing distortions |
| Data Mosh | `.data_mosh(corruption_rate=0.02)` | Chaotic glitches |
| Scan Lines | `.scan_lines(intensity=0.3)` | Retro CRT look |
| Slice & Shift | `.slice_and_shift(num_slices=10)` | Broken fragments |

## Tips

1. **Start simple**: Use `random_glitch_combo()` to experiment
2. **Chain effects**: Combine 2-4 effects for unique results
3. **Use seeds**: Same seed = reproducible results
4. **Save often**: Try different parameters and compare
5. **High quality**: Use `quality=95` when saving

Happy glitching! 🎨

