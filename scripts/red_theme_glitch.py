#!/usr/bin/env python3
"""
RED Theme Glitch Art
Create red/blood/crimson themed glitch art for competitions
"""

import sys
sys.path.append('..')
from src.glitch_effects import GlitchArtist
from PIL import Image, ImageEnhance
import numpy as np
import sys
import os


def red_color_pulse(input_path, output_path=None, frames=75, duration=30, 
                    intensity=0.6, style='blood'):
    """
    Create pulsing RED overlay animation
    
    Args:
        style: 'blood', 'crimson', 'fire', 'neon_red', 'dark_red'
    """
    
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/red_competition/red_pulse_{style}_{name}.gif'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    # RED color palettes
    color_palettes = {
        'blood': [
            (139, 0, 0),      # Dark red
            (178, 34, 34),    # Firebrick
            (220, 20, 60),    # Crimson
            (255, 0, 0),      # Pure red
        ],
        'crimson': [
            (220, 20, 60),    # Crimson
            (255, 0, 63),     # Folly
            (220, 0, 0),      # Red
            (178, 34, 34),    # Firebrick
        ],
        'fire': [
            (255, 69, 0),     # Red-orange
            (255, 0, 0),      # Red
            (255, 140, 0),    # Dark orange
            (220, 20, 60),    # Crimson
        ],
        'neon_red': [
            (255, 0, 0),      # Pure red
            (255, 20, 147),   # Deep pink
            (255, 0, 100),    # Hot red
            (255, 51, 0),     # Scarlet
        ],
        'dark_red': [
            (102, 0, 0),      # Very dark red
            (139, 0, 0),      # Dark red
            (165, 0, 0),      # Medium dark
            (128, 0, 0),      # Maroon
        ]
    }
    
    colors = color_palettes.get(style, color_palettes['blood'])
    
    print(f"🎨 Creating RED color pulse animation")
    print(f"   Style: {style}")
    print(f"   Colors: {len(colors)} red variations")
    print(f"   Frames: {frames} @ {duration}ms")
    
    base = Image.open(input_path).convert('RGB')
    width, height = base.size
    
    frame_list = []
    
    for i in range(frames):
        current_frame = base.copy()
        
        # Pulsing - smooth sine wave
        pulse = (np.sin(2 * np.pi * i / 30) + 1) / 2
        opacity = intensity * pulse
        
        # Cycle through red shades
        color_idx = (i // 15) % len(colors)
        color = colors[color_idx]
        
        if opacity > 0:
            color_layer = Image.new('RGB', (width, height), color)
            current_frame = Image.blend(current_frame, color_layer, opacity)
        
        frame_list.append(current_frame)
        
        if (i + 1) % 25 == 0:
            print(f'   Processed {i + 1}/{frames} frames...')
    
    print(f"💾 Saving RED pulse GIF...")
    frame_list[0].save(
        output_path,
        save_all=True,
        append_images=frame_list[1:],
        duration=duration,
        loop=0,
        optimize=False
    )
    
    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✅ Saved: {output_path}")
    print(f"   File size: {file_size:.2f}MB")


def red_glitch_static(input_path, output_path=None, red_intensity=0.5):
    """
    Create static glitch with red color enhancement
    """
    
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/red_competition/red_glitch_{name}.png'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Creating RED glitch static image")
    
    # Apply glitch
    glitcher = GlitchArtist(image_path=input_path)
    glitcher.random_glitch_combo(intensity='high')
    glitched = glitcher.get_image()
    
    # Enhance red channel
    img_array = np.array(glitched)
    
    # Boost red, reduce green and blue
    img_array[:, :, 0] = np.clip(img_array[:, :, 0] * (1 + red_intensity), 0, 255)  # Red
    img_array[:, :, 1] = np.clip(img_array[:, :, 1] * (1 - red_intensity * 0.5), 0, 255)  # Green
    img_array[:, :, 2] = np.clip(img_array[:, :, 2] * (1 - red_intensity * 0.5), 0, 255)  # Blue
    
    result = Image.fromarray(img_array.astype(np.uint8))
    result.save(output_path)
    
    print(f"✅ Saved: {output_path}")


def red_scraperboard_glitch(input_path, output_path=None):
    """
    Create red-tinted scraperboard + glitch combination
    """
    import sys
    sys.path.append('..')
    
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/red_competition/red_scraperboard_{name}.png'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Creating RED scraperboard + glitch")
    
    # First create scraperboard
    from scripts.scraperboard_effect import scraperboard_gothic
    temp_path = '/tmp/temp_scraperboard.png'
    scraperboard_gothic(input_path, temp_path)
    
    # Glitch it
    glitcher = GlitchArtist(image_path=temp_path)
    glitcher.random_glitch_combo(intensity='medium')
    glitched = glitcher.get_image().convert('RGB')
    
    # Add red tint
    img_array = np.array(glitched)
    
    # Create red tint (keep whites, tint grays/blacks red)
    red_tint = np.zeros_like(img_array)
    red_tint[:, :, 0] = 255  # Red channel full
    red_tint[:, :, 1] = img_array[:, :, 1] // 3  # Reduce green
    red_tint[:, :, 2] = img_array[:, :, 2] // 3  # Reduce blue
    
    # Blend based on brightness
    brightness = np.mean(img_array, axis=2, keepdims=True)
    blend_factor = np.clip(1 - brightness / 255, 0, 0.7)
    
    result = img_array * (1 - blend_factor) + red_tint * blend_factor
    
    final = Image.fromarray(result.astype(np.uint8))
    final.save(output_path)
    
    print(f"✅ Saved: {output_path}")
    
    # Cleanup
    if os.path.exists(temp_path):
        os.remove(temp_path)


def show_menu():
    """Show usage"""
    print("\n" + "="*70)
    print("🔴 RED THEME GLITCH ART")
    print("="*70)
    print("\nCreate red-themed glitch art for competitions")
    print("\nUsage:")
    print("  python scripts/red_theme_glitch.py <image> <mode> [style]")
    print("\nModes:")
    print("  pulse  - Pulsing red overlay animation")
    print("  static - Static glitch with red enhancement")
    print("  scraper - Red-tinted scraperboard + glitch")
    print("\nStyles (for pulse mode):")
    print("  blood      - Dark blood reds")
    print("  crimson    - Bright crimson reds")
    print("  fire       - Red-orange fire")
    print("  neon_red   - Neon red/pink")
    print("  dark_red   - Very dark maroon/burgundy")
    print("\nExamples:")
    print("  python scripts/red_theme_glitch.py skull.jpg pulse blood")
    print("  python scripts/red_theme_glitch.py deity.jpg static")
    print("  python scripts/red_theme_glitch.py dark.jpg scraper")
    print("\n" + "="*70 + "\n")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        show_menu()
        sys.exit(0)
    
    input_file = sys.argv[1]
    mode = sys.argv[2]
    style = sys.argv[3] if len(sys.argv) > 3 else 'blood'
    
    if mode == 'pulse':
        red_color_pulse(input_file, style=style)
    elif mode == 'static':
        red_glitch_static(input_file)
    elif mode == 'scraper':
        red_scraperboard_glitch(input_file)
    else:
        print(f"❌ Unknown mode: {mode}")
        show_menu()

