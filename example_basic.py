"""
Basic Glitch Art Examples
Simple examples to get started with glitch art creation
"""

from src.glitch_effects import GlitchArtist
from src.generative_glitch import GenerativeGlitchArt
from PIL import Image
import os


def example_1_pixel_sort():
    """Example 1: Pixel Sorting Effect"""
    print("Example 1: Creating pixel sort effect...")
    
    # Create a base image
    generator = GenerativeGlitchArt(800, 600)
    base = generator.create_base_gradient()
    
    # Apply pixel sort
    glitcher = GlitchArtist(image=base)
    glitcher.pixel_sort(threshold=128, direction='horizontal')
    glitcher.save('output_pixel_sort.png')
    
    print("✓ Saved: output_pixel_sort.png")


def example_2_rgb_shift():
    """Example 2: RGB Channel Shift (Chromatic Aberration)"""
    print("\nExample 2: Creating RGB shift effect...")
    
    # Create a geometric base
    generator = GenerativeGlitchArt(800, 600)
    base = generator.create_geometric_base(num_shapes=30)
    
    # Apply RGB shift
    glitcher = GlitchArtist(image=base)
    glitcher.rgb_shift(r_shift=(20, 0), b_shift=(-20, 0))
    glitcher.save('output_rgb_shift.png')
    
    print("✓ Saved: output_rgb_shift.png")


def example_3_data_mosh():
    """Example 3: Data Moshing"""
    print("\nExample 3: Creating data mosh effect...")
    
    # Create a vaporwave base
    generator = GenerativeGlitchArt(800, 600)
    base = generator.create_vaporwave_aesthetic()
    
    # Apply data mosh
    glitcher = GlitchArtist(image=base)
    glitcher.data_mosh(corruption_rate=0.02, block_size=15)
    glitcher.save('output_data_mosh.png')
    
    print("✓ Saved: output_data_mosh.png")


def example_4_combined_effects():
    """Example 4: Combining Multiple Effects"""
    print("\nExample 4: Creating combined glitch effects...")
    
    # Create a cyberpunk base
    generator = GenerativeGlitchArt(800, 600)
    base = generator.create_cyberpunk_aesthetic()
    
    # Apply multiple effects in sequence
    glitcher = GlitchArtist(image=base)
    (glitcher
        .rgb_shift(r_shift=(10, 0), b_shift=(-10, 0))
        .scan_lines(line_height=3, intensity=0.3)
        .slice_and_shift(num_slices=8, max_shift=30)
        .save('output_combined.png'))
    
    print("✓ Saved: output_combined.png")


def example_5_random_glitch():
    """Example 5: Random Glitch Combination"""
    print("\nExample 5: Creating random glitch art...")
    
    # Create a gradient base
    generator = GenerativeGlitchArt(800, 600)
    base = generator.create_base_gradient()
    
    # Apply random glitch effects
    glitcher = GlitchArtist(image=base)
    glitcher.random_glitch_combo(intensity='high')
    glitcher.save('output_random_glitch.png')
    
    print("✓ Saved: output_random_glitch.png")


def example_6_glitch_existing_image():
    """Example 6: Glitch an Existing Image"""
    print("\nExample 6: Glitching an existing image...")
    
    # First, create a sample image if you don't have one
    generator = GenerativeGlitchArt(800, 600)
    sample = generator.create_geometric_base(num_shapes=50)
    sample.save('sample_image.png')
    
    # Now glitch it
    glitcher = GlitchArtist(image_path='sample_image.png')
    (glitcher
        .pixel_sort(threshold=150, direction='vertical')
        .rgb_shift(g_shift=(0, 15))
        .wave_distortion(amplitude=15, frequency=0.05)
        .save('output_glitched_existing.png'))
    
    print("✓ Saved: output_glitched_existing.png")


def example_7_nft_generation():
    """Example 7: Generate NFT-Ready Artwork"""
    print("\nExample 7: Generating NFT-ready artwork...")
    
    # Generate unique pieces with different seeds
    for i in range(3):
        generator = GenerativeGlitchArt(1000, 1000)
        base = generator.generate_unique_nft(seed=i, style='random')
        
        glitcher = GlitchArtist(image=base)
        glitcher.random_glitch_combo(intensity='medium')
        glitcher.save(f'nft_sample_{i+1}.png')
        
        print(f"✓ Saved: nft_sample_{i+1}.png")


def run_all_examples():
    """Run all examples"""
    print("=" * 60)
    print("GLITCH ART EXAMPLES")
    print("=" * 60)
    
    example_1_pixel_sort()
    example_2_rgb_shift()
    example_3_data_mosh()
    example_4_combined_effects()
    example_5_random_glitch()
    example_6_glitch_existing_image()
    example_7_nft_generation()
    
    print("\n" + "=" * 60)
    print("All examples complete! Check the output files.")
    print("=" * 60)


if __name__ == '__main__':
    run_all_examples()

