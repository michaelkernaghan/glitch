#!/usr/bin/env python3
"""
Advanced Image Glitching
More control over individual effects
"""

import sys; sys.path.append(".."); from src.glitch_effects import GlitchArtist
import sys
import os


def show_effects_menu():
    """Show all available effects"""
    print("\n" + "="*70)
    print("🎨 ADVANCED GLITCH EFFECTS")
    print("="*70)
    print("\nAvailable Effects:\n")
    
    effects = [
        ("1", "RGB Shift", "Chromatic aberration (color separation)"),
        ("2", "Pixel Sort", "Sort pixels by brightness"),
        ("3", "Data Mosh", "Digital corruption artifacts"),
        ("4", "Scan Lines", "CRT monitor effect"),
        ("5", "Wave Distortion", "Liquid wave effect"),
        ("6", "Slice & Shift", "Horizontal slice displacement"),
        ("7", "Color Swap", "Swap RGB channels"),
        ("8", "JPEG Artifacts", "Compression degradation"),
        ("9", "All Effects", "Apply multiple effects"),
        ("0", "Custom Combo", "Your custom combination"),
    ]
    
    for num, name, desc in effects:
        print(f"  [{num}] {name:20s} - {desc}")
    
    print("\n" + "="*70)


def apply_effect(glitcher, effect_num):
    """Apply a specific effect"""
    
    if effect_num == '1':
        print("⚡ Applying RGB Shift...")
        glitcher.rgb_shift(r_shift=(20, 0), b_shift=(-20, 0))
    
    elif effect_num == '2':
        print("⚡ Applying Pixel Sort...")
        glitcher.pixel_sort(threshold=130, direction='horizontal')
    
    elif effect_num == '3':
        print("⚡ Applying Data Mosh...")
        glitcher.data_mosh(corruption_rate=0.015, block_size=15)
    
    elif effect_num == '4':
        print("⚡ Applying Scan Lines...")
        glitcher.scan_lines(line_height=3, intensity=0.3)
    
    elif effect_num == '5':
        print("⚡ Applying Wave Distortion...")
        glitcher.wave_distortion(amplitude=15, frequency=0.05, direction='horizontal')
    
    elif effect_num == '6':
        print("⚡ Applying Slice & Shift...")
        glitcher.slice_and_shift(num_slices=12, max_shift=50)
    
    elif effect_num == '7':
        print("⚡ Applying Color Swap...")
        glitcher.color_channel_swap(swap_type='random')
    
    elif effect_num == '8':
        print("⚡ Applying JPEG Artifacts...")
        glitcher.jpeg_compression_artifacts(quality=10, iterations=3)
    
    elif effect_num == '9':
        print("⚡ Applying Multiple Effects...")
        glitcher.random_glitch_combo(intensity='medium')
    
    elif effect_num == '0':
        print("⚡ Applying Custom Combo...")
        # Customize this!
        glitcher.rgb_shift(r_shift=(10, 0), b_shift=(-10, 0))
        glitcher.pixel_sort(threshold=140)
        glitcher.scan_lines(intensity=0.25)
    
    else:
        print(f"❌ Unknown effect: {effect_num}")
        return False
    
    return True


def glitch_interactive(input_path):
    """Interactive glitching with effect selection"""
    
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    show_effects_menu()
    
    print("\nEnter effect number (or press Enter for all effects): ", end='')
    choice = input().strip() or '9'
    
    # Load image
    print(f"\n🎨 Loading image: {input_path}")
    glitcher = GlitchArtist(image_path=input_path)
    
    # Apply effect
    if apply_effect(glitcher, choice):
        # Generate output filename
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/effect_{choice}_{name}.png'
        
        os.makedirs('examples_output', exist_ok=True)
        glitcher.save(output_path)
        
        print(f"✅ Saved to: {output_path}\n")


def glitch_preset_styles(input_path):
    """Apply preset glitch styles"""
    
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    print("\n" + "="*60)
    print("🎨 PRESET GLITCH STYLES")
    print("="*60)
    
    styles = {
        'vaporwave': {
            'name': 'Vaporwave',
            'effects': lambda g: g.pixel_sort(threshold=120).scan_lines(intensity=0.3)
        },
        'cyberpunk': {
            'name': 'Cyberpunk',
            'effects': lambda g: g.rgb_shift(r_shift=(25, 0), b_shift=(-25, 0)).data_mosh(corruption_rate=0.015)
        },
        'minimal': {
            'name': 'Minimal',
            'effects': lambda g: g.rgb_shift(r_shift=(5, 0), b_shift=(-5, 0)).scan_lines(intensity=0.2)
        },
        'chaotic': {
            'name': 'Chaotic',
            'effects': lambda g: g.slice_and_shift(num_slices=20, max_shift=80).data_mosh(corruption_rate=0.025).color_channel_swap()
        },
        'retro': {
            'name': 'Retro',
            'effects': lambda g: g.jpeg_compression_artifacts(quality=15, iterations=3).scan_lines(intensity=0.4)
        }
    }
    
    print("\nAvailable Presets:\n")
    for i, (key, style) in enumerate(styles.items(), 1):
        print(f"  [{i}] {style['name']}")
    
    print(f"\n  [0] Apply ALL presets")
    print("\n" + "="*60)
    
    print("\nEnter preset number: ", end='')
    choice = input().strip()
    
    if choice == '0':
        # Apply all presets
        print(f"\n🎨 Loading image: {input_path}")
        for key, style in styles.items():
            print(f"\n⚡ Applying {style['name']} style...")
            glitcher = GlitchArtist(image_path=input_path)
            style['effects'](glitcher)
            
            filename = os.path.basename(input_path)
            name, ext = os.path.splitext(filename)
            output_path = f'examples_output/{key}_{name}.png'
            
            os.makedirs('examples_output', exist_ok=True)
            glitcher.save(output_path)
            print(f"✅ Saved to: {output_path}")
    else:
        try:
            idx = int(choice) - 1
            key = list(styles.keys())[idx]
            style = styles[key]
            
            print(f"\n🎨 Loading image: {input_path}")
            print(f"⚡ Applying {style['name']} style...")
            
            glitcher = GlitchArtist(image_path=input_path)
            style['effects'](glitcher)
            
            filename = os.path.basename(input_path)
            name, ext = os.path.splitext(filename)
            output_path = f'examples_output/{key}_{name}.png'
            
            os.makedirs('examples_output', exist_ok=True)
            glitcher.save(output_path)
            print(f"✅ Saved to: {output_path}\n")
        except (ValueError, IndexError):
            print("❌ Invalid choice")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("\n" + "="*60)
        print("🎨 ADVANCED IMAGE GLITCHING")
        print("="*60)
        print("\nUsage:")
        print("  python advanced_glitch.py <image_path> [mode]")
        print("\nModes:")
        print("  interactive - Choose individual effects (default)")
        print("  presets    - Apply preset glitch styles")
        print("\nExamples:")
        print("  python advanced_glitch.py my_photo.jpg")
        print("  python advanced_glitch.py my_photo.jpg presets")
        print("\n" + "="*60 + "\n")
        sys.exit(0)
    
    input_image = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else 'interactive'
    
    if mode == 'presets':
        glitch_preset_styles(input_image)
    else:
        glitch_interactive(input_image)

