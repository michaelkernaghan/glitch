"""
Advanced Glitch Art Examples
More sophisticated techniques for creating professional NFT collections
"""

import sys; sys.path.append(".."); from src.glitch_effects import GlitchArtist
import sys; sys.path.append(".."); from src.generative_glitch import GenerativeGlitchArt
import random
import os


def create_themed_collection(theme: str, num_pieces: int = 5):
    """Create a themed collection of glitch art"""
    print(f"\n{'='*60}")
    print(f"Creating {theme.upper()} themed collection ({num_pieces} pieces)")
    print('='*60)
    
    output_dir = f'collection_{theme}'
    os.makedirs(output_dir, exist_ok=True)
    
    for i in range(num_pieces):
        print(f"Generating piece {i+1}/{num_pieces}...")
        
        generator = GenerativeGlitchArt(1000, 1000)
        
        if theme == 'vaporwave':
            base = generator.create_vaporwave_aesthetic()
            glitcher = GlitchArtist(image=base)
            glitcher.pixel_sort(
                threshold=random.randint(100, 150),
                direction='horizontal'
            )
            glitcher.scan_lines(line_height=3, intensity=0.3)
            if random.random() > 0.5:
                glitcher.rgb_shift(r_shift=(5, 0), b_shift=(-5, 0))
        
        elif theme == 'cyberpunk':
            base = generator.create_cyberpunk_aesthetic()
            glitcher = GlitchArtist(image=base)
            glitcher.rgb_shift(
                r_shift=(random.randint(10, 20), 0),
                b_shift=(-random.randint(10, 20), 0)
            )
            glitcher.data_mosh(
                corruption_rate=random.uniform(0.01, 0.02),
                block_size=random.randint(10, 15)
            )
            if random.random() > 0.7:
                glitcher.slice_and_shift(num_slices=8, max_shift=30)
        
        elif theme == 'minimal':
            colors = [
                (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255)),
                (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
            ]
            base = generator.create_base_gradient(colors=colors)
            glitcher = GlitchArtist(image=base)
            glitcher.rgb_shift(r_shift=(3, 0), b_shift=(-3, 0))
            glitcher.scan_lines(line_height=2, intensity=0.2)
        
        elif theme == 'chaotic':
            base = generator.create_geometric_base(num_shapes=random.randint(50, 100))
            glitcher = GlitchArtist(image=base)
            glitcher.random_glitch_combo(intensity='high')
        
        output_path = os.path.join(output_dir, f'{theme}_{i+1:03d}.png')
        glitcher.save(output_path)
        print(f"  ✓ Saved: {output_path}")
    
    print(f"\n✓ {theme.upper()} collection complete!")


def create_rarity_tiers():
    """Demonstrate creating NFTs with different rarity levels"""
    print("\n" + "="*60)
    print("Creating NFT Collection with Rarity Tiers")
    print("="*60)
    
    output_dir = 'rarity_collection'
    os.makedirs(output_dir, exist_ok=True)
    
    # Define rarity distribution
    rarities = (
        ['common'] * 7 +      # 70% common
        ['rare'] * 2 +        # 20% rare
        ['legendary'] * 1     # 10% legendary
    )
    
    for i, rarity in enumerate(rarities):
        print(f"\nGenerating {rarity.upper()} piece {i+1}/10...")
        
        generator = GenerativeGlitchArt(1000, 1000)
        
        # Different base styles for different rarities
        if rarity == 'common':
            base = generator.create_base_gradient()
            glitcher = GlitchArtist(image=base)
            glitcher.random_glitch_combo(intensity='low')
            print("  - Applied: Low intensity glitches")
        
        elif rarity == 'rare':
            base = generator.create_vaporwave_aesthetic()
            glitcher = GlitchArtist(image=base)
            glitcher.random_glitch_combo(intensity='medium')
            glitcher.rgb_shift(r_shift=(10, 0), b_shift=(-10, 0))
            print("  - Applied: Medium intensity + RGB shift")
        
        elif rarity == 'legendary':
            base = generator.create_cyberpunk_aesthetic()
            glitcher = GlitchArtist(image=base)
            glitcher.random_glitch_combo(intensity='high')
            glitcher.color_channel_swap(swap_type='random')
            print("  - Applied: High intensity + Color swap")
        
        output_path = os.path.join(output_dir, f'{rarity}_{i+1:03d}.png')
        glitcher.save(output_path)
        print(f"  ✓ Saved: {output_path}")
    
    print("\n✓ Rarity collection complete!")
    print(f"  - 7 Common pieces")
    print(f"  - 2 Rare pieces")
    print(f"  - 1 Legendary piece")


def create_signature_style():
    """Create a consistent signature style across multiple pieces"""
    print("\n" + "="*60)
    print("Creating Signature Style Collection")
    print("="*60)
    print("Applying consistent effects for brand recognition\n")
    
    output_dir = 'signature_collection'
    os.makedirs(output_dir, exist_ok=True)
    
    # Define your signature style
    def apply_signature_style(glitcher: GlitchArtist):
        """Your unique glitch style"""
        glitcher.rgb_shift(r_shift=(8, 0), b_shift=(-8, 0))
        glitcher.pixel_sort(threshold=130, direction='horizontal')
        glitcher.scan_lines(line_height=3, intensity=0.25)
        return glitcher
    
    styles = ['vaporwave', 'cyberpunk', 'geometric', 'gradient', 'noise']
    
    for i, style in enumerate(styles):
        print(f"Generating piece {i+1}/5 with {style} base...")
        
        generator = GenerativeGlitchArt(1000, 1000)
        base = generator.generate_unique_nft(seed=i, style=style)
        
        glitcher = GlitchArtist(image=base)
        apply_signature_style(glitcher)
        
        output_path = os.path.join(output_dir, f'signature_{i+1:03d}.png')
        glitcher.save(output_path)
        print(f"  ✓ Saved: {output_path}")
    
    print("\n✓ Signature collection complete!")
    print("  All pieces share the same glitch style for consistency")


def create_evolution_series():
    """Create a series showing progressive glitch intensity"""
    print("\n" + "="*60)
    print("Creating Evolution Series")
    print("="*60)
    print("Showing progressive glitch intensity\n")
    
    output_dir = 'evolution_series'
    os.makedirs(output_dir, exist_ok=True)
    
    # Create one base image
    generator = GenerativeGlitchArt(1000, 1000)
    base = generator.create_vaporwave_aesthetic()
    
    intensities = [
        ('original', 0),
        ('subtle', 1),
        ('light', 2),
        ('medium', 3),
        ('heavy', 4),
        ('extreme', 5)
    ]
    
    for name, level in intensities:
        print(f"Creating {name} version (level {level})...")
        
        glitcher = GlitchArtist(image=base.copy())
        
        if level == 0:
            # Original, no effects
            pass
        elif level == 1:
            glitcher.rgb_shift(r_shift=(3, 0), b_shift=(-3, 0))
        elif level == 2:
            glitcher.rgb_shift(r_shift=(8, 0), b_shift=(-8, 0))
            glitcher.scan_lines(intensity=0.2)
        elif level == 3:
            glitcher.rgb_shift(r_shift=(15, 0), b_shift=(-15, 0))
            glitcher.pixel_sort(threshold=140)
            glitcher.scan_lines(intensity=0.3)
        elif level == 4:
            glitcher.rgb_shift(r_shift=(25, 0), b_shift=(-25, 0))
            glitcher.pixel_sort(threshold=120)
            glitcher.data_mosh(corruption_rate=0.015)
            glitcher.scan_lines(intensity=0.4)
        elif level == 5:
            glitcher.slice_and_shift(num_slices=15, max_shift=80)
            glitcher.rgb_shift(r_shift=(40, 0), b_shift=(-40, 0))
            glitcher.data_mosh(corruption_rate=0.03)
            glitcher.color_channel_swap(swap_type='random')
        
        output_path = os.path.join(output_dir, f'{level}_{name}.png')
        glitcher.save(output_path)
        print(f"  ✓ Saved: {output_path}")
    
    print("\n✓ Evolution series complete!")
    print("  View the images in order to see the progression")


def create_color_palette_variations():
    """Create variations using different color palettes"""
    print("\n" + "="*60)
    print("Creating Color Palette Variations")
    print("="*60)
    
    output_dir = 'palette_variations'
    os.makedirs(output_dir, exist_ok=True)
    
    palettes = {
        'sunset': [(255, 94, 77), (255, 175, 64), (255, 224, 102)],
        'ocean': [(0, 119, 182), (0, 180, 216), (144, 224, 239)],
        'forest': [(34, 139, 34), (107, 142, 35), (154, 205, 50)],
        'neon': [(255, 0, 255), (0, 255, 255), (255, 255, 0)],
        'monochrome': [(50, 50, 50), (150, 150, 150), (250, 250, 250)],
    }
    
    for i, (name, colors) in enumerate(palettes.items()):
        print(f"\nCreating {name} palette variation...")
        
        generator = GenerativeGlitchArt(1000, 1000)
        base = generator.create_base_gradient(colors=colors)
        
        glitcher = GlitchArtist(image=base)
        glitcher.pixel_sort(threshold=130, direction='horizontal')
        glitcher.rgb_shift(r_shift=(10, 0), b_shift=(-10, 0))
        glitcher.scan_lines(intensity=0.3)
        
        output_path = os.path.join(output_dir, f'palette_{name}.png')
        glitcher.save(output_path)
        print(f"  ✓ Saved: {output_path}")
    
    print("\n✓ Palette variations complete!")


def batch_process_custom_images():
    """Example of batch processing your own images"""
    print("\n" + "="*60)
    print("Batch Processing Example")
    print("="*60)
    print("This example shows how to glitch your own images\n")
    
    # First, create some sample images to process
    print("Creating sample images...")
    sample_dir = 'samples_to_glitch'
    os.makedirs(sample_dir, exist_ok=True)
    
    generator = GenerativeGlitchArt(800, 600)
    for i in range(3):
        base = generator.generate_unique_nft(seed=i, style='random')
        base.save(os.path.join(sample_dir, f'sample_{i+1}.png'))
    
    print(f"  ✓ Created 3 sample images in {sample_dir}/\n")
    
    # Now batch process them
    output_dir = 'batch_processed'
    os.makedirs(output_dir, exist_ok=True)
    
    sample_files = [f for f in os.listdir(sample_dir) if f.endswith('.png')]
    
    for filename in sample_files:
        print(f"Processing {filename}...")
        
        input_path = os.path.join(sample_dir, filename)
        glitcher = GlitchArtist(image_path=input_path)
        
        # Apply random effects
        glitcher.random_glitch_combo(intensity='medium')
        
        output_path = os.path.join(output_dir, f'glitched_{filename}')
        glitcher.save(output_path)
        print(f"  ✓ Saved: {output_path}")
    
    print("\n✓ Batch processing complete!")


def run_all_advanced_examples():
    """Run all advanced examples"""
    print("\n" + "="*60)
    print("ADVANCED GLITCH ART EXAMPLES")
    print("="*60)
    print("\nThis will create multiple collections demonstrating")
    print("professional NFT creation techniques.\n")
    
    # Run each example
    create_themed_collection('vaporwave', num_pieces=3)
    create_themed_collection('cyberpunk', num_pieces=3)
    create_themed_collection('minimal', num_pieces=3)
    
    create_rarity_tiers()
    create_signature_style()
    create_evolution_series()
    create_color_palette_variations()
    batch_process_custom_images()
    
    print("\n" + "="*60)
    print("ALL ADVANCED EXAMPLES COMPLETE!")
    print("="*60)
    print("\nCollections created:")
    print("  - collection_vaporwave/")
    print("  - collection_cyberpunk/")
    print("  - collection_minimal/")
    print("  - rarity_collection/")
    print("  - signature_collection/")
    print("  - evolution_series/")
    print("  - palette_variations/")
    print("  - batch_processed/")
    print("\nExplore these folders to see different approaches!")


if __name__ == '__main__':
    run_all_advanced_examples()

