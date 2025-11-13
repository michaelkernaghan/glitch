# Project Structure

```
glitch/
│
├── 📁 src/                          # Core library files
│   ├── __init__.py                  # Package initialization
│   ├── glitch_effects.py            # Main effects library (GlitchArtist class)
│   └── generative_glitch.py         # Generative art creation
│
├── 📁 docs/                         # Documentation
│   ├── README.md                    # Full comprehensive guide
│   └── QUICK_START.md               # 5-minute quick start
│
├── 📁 imported_images/              # Your source images (put your images here!)
│   └── DALLE2~4.PNG                 # Example: your uploaded images
│
├── 📁 examples_output/              # Generated glitched images
│   ├── nft_sample_*.png             # NFT samples
│   ├── output_*.png                 # Effect examples
│   └── glitched_*.png               # Your glitched images
│
├── 📁 venv/                         # Python virtual environment (gitignored)
│
├── 📄 example_basic.py              # Run basic examples
├── 📄 example_advanced.py           # Advanced NFT collection examples
├── 📄 requirements.txt              # Python dependencies
├── 📄 README.md                     # Main project readme
├── 📄 .gitignore                    # Git ignore rules
└── 📄 PROJECT_STRUCTURE.md          # This file!
```

## What's What?

### 📁 `src/` - Core Library
The heart of your glitch art toolkit:
- **`glitch_effects.py`** - Contains `GlitchArtist` class with all effects
- **`generative_glitch.py`** - Contains `GenerativeGlitchArt` for creating art from scratch
- **`__init__.py`** - Makes src/ a proper Python package

### 📁 `docs/` - Documentation
All your learning resources:
- **`README.md`** - Comprehensive guide with all effects explained
- **`QUICK_START.md`** - Get started in 5 minutes

### 📁 `examples_output/` - Generated Art
All images created by the example scripts go here (gitignored):
- Output files from `example_basic.py`
- Output files from `example_advanced.py`
- Any test images you create

### 📄 Example Scripts
- **`example_basic.py`** - 7 basic examples of different glitch techniques
- **`example_advanced.py`** - Professional NFT collection strategies

## Usage

### Import the library:
```python
from src.glitch_effects import GlitchArtist
from src.generative_glitch import GenerativeGlitchArt
```

### Or use the package-level imports:
```python
from src import GlitchArtist, GenerativeGlitchArt, generate_nft_collection
```

### Run examples:
```bash
python example_basic.py      # Basic examples
python example_advanced.py   # Advanced collections
```

## Clean Structure Benefits

✅ **Organized**: Source code separated from examples and docs  
✅ **Clean Root**: No clutter in main directory  
✅ **Git-friendly**: Output files are ignored  
✅ **Professional**: Standard Python project structure  
✅ **Scalable**: Easy to add more modules in src/  

## Adding Your Own Scripts

Create your own script in the root directory:

```python
# my_glitch_art.py
from src import GlitchArtist, GenerativeGlitchArt

# Your code here
generator = GenerativeGlitchArt(1000, 1000)
base = generator.create_vaporwave_aesthetic()

glitcher = GlitchArtist(image=base)
glitcher.random_glitch_combo('high')
glitcher.save('examples_output/my_art.png')
```

Run it:
```bash
python my_glitch_art.py
```

All generated images will automatically go to `examples_output/` and will be ignored by git!

