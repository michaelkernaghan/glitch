#!/usr/bin/env python3
"""
Glitch Your Own Image
Simple script to apply glitch effects to any image you provide
"""

import sys; sys.path.append(".."); from src.glitch_effects import GlitchArtist
import sys
import os


def glitch_image(input_path, output_path=None, intensity='medium'):
    """
    Apply glitch effects to an image
    
    Args:
        input_path: Path to your image
        output_path: Where to save (optional, auto-generates if not provided)
        intensity: 'low', 'medium', or 'high'
    """
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    # Auto-generate output path if not provided
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/glitched_{name}.png'
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Loading image: {input_path}")
    print(f"⚡ Applying {intensity} intensity glitch effects...")
    
    # Load and glitch the image
    glitcher = GlitchArtist(image_path=input_path)
    glitcher.random_glitch_combo(intensity=intensity)
    glitcher.save(output_path)
    
    print(f"✅ Saved glitched image to: {output_path}")
    print(f"📁 Original size: {glitcher.width}x{glitcher.height}")


def glitch_with_specific_effects(input_path, output_path=None):
    """
    Apply specific effects with more control
    """
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/custom_glitched_{name}.png'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Loading image: {input_path}")
    print("⚡ Applying custom glitch effects...")
    
    # Load image and apply specific effects
    glitcher = GlitchArtist(image_path=input_path)
    
    # Customize these effects as you like!
    (glitcher
        .rgb_shift(r_shift=(15, 0), b_shift=(-15, 0))  # Chromatic aberration
        .pixel_sort(threshold=130, direction='horizontal')  # Pixel sorting
        .scan_lines(line_height=3, intensity=0.3)  # CRT lines
        .save(output_path))
    
    print(f"✅ Saved glitched image to: {output_path}")


def show_menu():
    """Show available glitch styles"""
    print("\n" + "="*60)
    print("🎨 GLITCH YOUR IMAGE")
    print("="*60)
    print("\nUsage:")
    print("  python glitch_my_image.py <image_path> [intensity]")
    print("\nExamples:")
    print("  python glitch_my_image.py my_photo.jpg")
    print("  python glitch_my_image.py my_photo.jpg high")
    print("  python glitch_my_image.py portrait.png low")
    print("\nIntensity levels:")
    print("  • low    - Subtle glitches (1-2 effects)")
    print("  • medium - Moderate glitches (2-4 effects) [default]")
    print("  • high   - Heavy glitches (4-6 effects)")
    print("\n" + "="*60 + "\n")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        show_menu()
        print("💡 Tip: Drag and drop your image file path as the argument!\n")
        sys.exit(0)
    
    input_image = sys.argv[1]
    intensity = sys.argv[2] if len(sys.argv) > 2 else 'medium'
    
    # Validate intensity
    if intensity not in ['low', 'medium', 'high']:
        print(f"⚠️  Warning: Invalid intensity '{intensity}', using 'medium'")
        intensity = 'medium'
    
    # Glitch it!
    glitch_image(input_image, intensity=intensity)
    
    print("\n💡 To apply specific effects, edit the glitch_with_specific_effects() function")
    print("   in this script and customize the effects you want!\n")

