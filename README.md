# Glitch Art Toolkit for NFTs

A comprehensive Python toolkit for creating computer-generated glitch art, perfect for NFT collections.

## 📁 Project Structure

```
glitch/
├── imported_images/            # 📸 Put your source images here
├── examples_output/            # 🎨 Generated glitched images appear here
├── src/                        # 📚 Core library files
│   ├── glitch_effects.py      # Effect functions
│   └── generative_glitch.py   # Generative art creation
├── docs/                       # 📖 Documentation
│   ├── README.md              # Full documentation
│   └── QUICK_START.md         # Quick start guide
├── glitch_my_image.py          # 🚀 Simple: Glitch any image
├── advanced_glitch.py          # 🎯 Advanced: Choose effects/presets
├── example_basic.py            # Basic examples
├── example_advanced.py         # Advanced NFT techniques
└── requirements.txt            # Python dependencies
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### 2. Glitch Your Own Images! 🎨

**Simple Method:**
```bash
# Put your image in imported_images/ folder, then:
python glitch_my_image.py imported_images/your_photo.jpg

# Or specify intensity
python glitch_my_image.py imported_images/your_photo.jpg high
```

**Advanced Method (Choose Effects):**
```bash
# Interactive - pick which effect to apply
python advanced_glitch.py imported_images/your_photo.jpg

# Preset styles (vaporwave, cyberpunk, retro, etc.)
python advanced_glitch.py imported_images/your_photo.jpg presets
```

### 3. Run Examples

```bash
# Basic examples (7 different techniques)
python example_basic.py

# Advanced examples (professional NFT collections)
python example_advanced.py
```

### 4. Create Your First Glitch Art (from scratch)

```python
from src.glitch_effects import GlitchArtist
from src.generative_glitch import GenerativeGlitchArt

# Generate base → Apply glitch → Save
base = GenerativeGlitchArt(1000, 1000).create_vaporwave_aesthetic()
GlitchArtist(image=base).random_glitch_combo('high').save('my_glitch.png')
```

## 🎨 What You Can Create

- **Glitch Your Photos**: Turn any image into glitch art
- **Vaporwave Art**: Retro 80s/90s aesthetic with pink and cyan
- **Cyberpunk**: Dark backgrounds with neon accents
- **Data Mosh**: Corrupted, chaotic digital artifacts
- **Pixel Sort**: Flowing, organic distortions
- **RGB Shift**: Chromatic aberration effects
- **Generative Collections**: 100s of unique NFT pieces

## 📚 Full Documentation

See [docs/README.md](docs/README.md) for comprehensive documentation including:
- Detailed effect explanations
- NFT collection strategies
- Rarity tier creation
- Pro tips and techniques

See [docs/QUICK_START.md](docs/QUICK_START.md) for a 5-minute quick start guide.

## 🎯 Example Effects

```python
from src import GlitchArtist, GenerativeGlitchArt

# Create base
generator = GenerativeGlitchArt(1000, 1000)
base = generator.create_vaporwave_aesthetic()

# Apply effects (method chaining)
glitcher = GlitchArtist(image=base)
(glitcher
    .rgb_shift(r_shift=(20, 0), b_shift=(-20, 0))
    .pixel_sort(threshold=128)
    .scan_lines(intensity=0.3)
    .save('vaporwave_glitch.png'))
```

## 🖼️ Generate NFT Collections

```python
from src.generative_glitch import generate_nft_collection

generate_nft_collection(
    num_pieces=100,
    output_dir='./my_nft_collection',
    width=1000,
    height=1000
)
```

## 📦 Available Effects

| Effect | Description | Best For |
|--------|-------------|----------|
| `pixel_sort()` | Sort pixels by brightness | Flowing distortions |
| `rgb_shift()` | Shift color channels | Chromatic aberration |
| `data_mosh()` | Simulate data corruption | Chaotic glitches |
| `scan_lines()` | Add CRT monitor lines | Retro aesthetic |
| `wave_distortion()` | Sine wave distortions | Liquid effects |
| `slice_and_shift()` | Cut and shift slices | Broken fragments |
| `jpeg_compression_artifacts()` | Compression artifacts | Lo-fi degraded look |
| `color_channel_swap()` | Swap RGB channels | Psychedelic colors |
| `random_glitch_combo()` | Random combination | Quick experimentation |

## 🎭 Preset Styles

The `advanced_glitch.py` script includes these presets:
- **Vaporwave**: Pixel sort + scan lines
- **Cyberpunk**: Heavy RGB shift + data corruption
- **Minimal**: Subtle RGB shift + light scan lines
- **Chaotic**: Slice & shift + data mosh + color swap
- **Retro**: JPEG artifacts + heavy scan lines

## 🎓 Learning Resources

1. **Run the examples**: See different techniques in action
2. **Read the docs**: Understand each effect and parameter
3. **Experiment**: Modify parameters and combine effects
4. **Create collections**: Apply what you learned to NFT generation

## 💡 Tips for NFT Creators

- **Use seeds** for reproducible, unique pieces
- **Create rarity tiers** with different glitch intensities
- **Develop a signature style** for brand recognition
- **High quality output**: 1000x1000+ resolution
- **Save with quality=95** for PNG exports
- **Keep source images** in `imported_images/` folder

## 📂 Workflow

1. **Put source images** in `imported_images/`
2. **Glitch them** with `glitch_my_image.py` or `advanced_glitch.py`
3. **Find results** in `examples_output/`
4. **Iterate and refine** until you get the perfect look!

## 🛠️ Requirements

- Python 3.12+
- Pillow (image processing)
- NumPy (array operations)
- OpenCV (computer vision)
- SciPy (scientific computing)
- Matplotlib (visualization)

## 📄 License

Free to use for personal and commercial projects, including NFT creation.

---

**Happy Glitching! 🎨✨**

Created with ❤️ for the NFT art community
