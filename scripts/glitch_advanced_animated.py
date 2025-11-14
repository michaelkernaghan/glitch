#!/usr/bin/env python3
"""
Advanced Animated Glitch Effects
- Selective region glitching
- Color flashing on specific areas
- Image overlays with transparency
- Masking and targeted effects
"""

import sys; sys.path.append(".."); from src.glitch_effects import GlitchArtist
from PIL import Image, ImageDraw, ImageEnhance
import numpy as np
import sys
import os


def create_mask_region(width, height, region='center', size=0.5):
    """
    Create a mask for selective glitching
    
    Args:
        width, height: Image dimensions
        region: 'center', 'left', 'right', 'top', 'bottom', 'edges', 'circle'
        size: Size factor (0.0-1.0)
    """
    mask = np.zeros((height, width), dtype=np.uint8)
    
    if region == 'center':
        # Center rectangle
        x1 = int(width * (1 - size) / 2)
        y1 = int(height * (1 - size) / 2)
        x2 = int(width * (1 + size) / 2)
        y2 = int(height * (1 + size) / 2)
        mask[y1:y2, x1:x2] = 255
    
    elif region == 'circle':
        # Circular mask
        center_x, center_y = width // 2, height // 2
        radius = int(min(width, height) * size / 2)
        y, x = np.ogrid[:height, :width]
        mask_circle = (x - center_x)**2 + (y - center_y)**2 <= radius**2
        mask[mask_circle] = 255
    
    elif region == 'left':
        mask[:, :int(width * size)] = 255
    
    elif region == 'right':
        mask[:, int(width * (1 - size)):] = 255
    
    elif region == 'top':
        mask[:int(height * size), :] = 255
    
    elif region == 'bottom':
        mask[int(height * (1 - size)):, :] = 255
    
    elif region == 'edges':
        # Edge frame
        thickness = int(min(width, height) * size * 0.1)
        mask[:thickness, :] = 255  # Top
        mask[-thickness:, :] = 255  # Bottom
        mask[:, :thickness] = 255  # Left
        mask[:, -thickness:] = 255  # Right
    
    return Image.fromarray(mask)


def selective_glitch_animation(input_path, output_path=None, region='center', 
                               frames=20, duration=100):
    """
    Glitch only a specific region of the image while keeping rest intact
    """
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/selective_{region}_{name}.gif'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Loading image: {input_path}")
    print(f"⚡ Creating selective glitch animation")
    print(f"   Region: {region}")
    print(f"   Frames: {frames}")
    
    original = Image.open(input_path).convert('RGB')
    width, height = original.size
    
    # Create mask for the region
    mask = create_mask_region(width, height, region=region, size=0.6)
    
    frame_list = []
    
    for i in range(frames):
        if i % 2 == 0:
            # Original frame
            frame_list.append(original.copy())
        else:
            # Glitch only the masked region
            glitcher = GlitchArtist(image=original.copy())
            glitcher.random_glitch_combo(intensity='high')
            glitched = glitcher.get_image()
            
            # Composite: original background + glitched region
            result = Image.composite(glitched, original, mask)
            frame_list.append(result)
    
    print(f"💾 Saving animated GIF...")
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
    print(f"   {frames} frames with selective glitching")
    print(f"   File size: {file_size:.2f}MB")


def color_flash_region(input_path, output_path=None, region='center', 
                       flash_color=(255, 0, 255), frames=20, duration=80):
    """
    Flash a specific region with color while keeping image intact
    """
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/colorflash_{region}_{name}.gif'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Loading image: {input_path}")
    print(f"⚡ Creating color flash animation")
    print(f"   Region: {region}")
    print(f"   Flash color: RGB{flash_color}")
    
    original = Image.open(input_path).convert('RGB')
    width, height = original.size
    
    # Create mask for the region
    mask = create_mask_region(width, height, region=region, size=0.7)
    
    # Create colored overlay
    color_overlay = Image.new('RGB', (width, height), flash_color)
    
    frame_list = []
    
    for i in range(frames):
        if i % 2 == 0:
            # Original frame
            frame_list.append(original.copy())
        else:
            # Flash the region with color (semi-transparent)
            # Blend original with color overlay using mask
            flashed = Image.composite(color_overlay, original, mask)
            # Make it semi-transparent
            blended = Image.blend(original, flashed, 0.6)
            frame_list.append(blended)
    
    print(f"💾 Saving animated GIF...")
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


def overlay_flashing_images(input_path, overlay_path, output_path=None, 
                           position='center', scale=0.3, frames=20, duration=100):
    """
    Overlay another image that flashes on top of the main image
    """
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if not os.path.exists(overlay_path):
        print(f"❌ Error: Overlay image not found at {overlay_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/overlay_{name}.gif'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Loading images...")
    print(f"   Base: {input_path}")
    print(f"   Overlay: {overlay_path}")
    
    base = Image.open(input_path).convert('RGBA')
    overlay = Image.open(overlay_path).convert('RGBA')
    
    # Scale overlay
    width, height = base.size
    overlay_size = (int(width * scale), int(height * scale))
    overlay = overlay.resize(overlay_size, Image.LANCZOS)
    
    # Calculate position
    if position == 'center':
        pos = ((width - overlay.width) // 2, (height - overlay.height) // 2)
    elif position == 'top-left':
        pos = (0, 0)
    elif position == 'top-right':
        pos = (width - overlay.width, 0)
    elif position == 'bottom-left':
        pos = (0, height - overlay.height)
    elif position == 'bottom-right':
        pos = (width - overlay.width, height - overlay.height)
    else:
        pos = (0, 0)
    
    frame_list = []
    
    for i in range(frames):
        if i % 2 == 0:
            # Base image only
            frame = base.copy().convert('RGB')
            frame_list.append(frame)
        else:
            # Base + overlay
            combined = base.copy()
            combined.paste(overlay, pos, overlay)
            frame = combined.convert('RGB')
            frame_list.append(frame)
    
    print(f"💾 Saving animated GIF...")
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


def color_shift_region(input_path, output_path=None, region='center', frames=30, duration=50):
    """
    Cycle through colors in a specific region (psychedelic effect)
    """
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/colorshift_{region}_{name}.gif'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Loading image: {input_path}")
    print(f"⚡ Creating color shift animation")
    print(f"   Region: {region}")
    
    original = Image.open(input_path).convert('RGB')
    width, height = original.size
    
    mask = create_mask_region(width, height, region=region, size=0.7)
    
    # Color cycle
    colors = [
        (255, 0, 255),   # Magenta
        (0, 255, 255),   # Cyan
        (255, 255, 0),   # Yellow
        (255, 0, 0),     # Red
        (0, 255, 0),     # Green
        (0, 0, 255),     # Blue
    ]
    
    frame_list = []
    
    for i in range(frames):
        color_idx = i % len(colors)
        color = colors[color_idx]
        
        # Create colored overlay
        color_overlay = Image.new('RGB', (width, height), color)
        
        # Composite with varying opacity
        opacity = 0.4 + 0.2 * np.sin(2 * np.pi * i / frames)
        
        colored = Image.composite(color_overlay, original, mask)
        blended = Image.blend(original, colored, opacity)
        
        frame_list.append(blended)
    
    print(f"💾 Saving animated GIF...")
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


def show_menu():
    """Show available advanced animation modes"""
    print("\n" + "="*70)
    print("🎨 ADVANCED ANIMATED GLITCH EFFECTS")
    print("="*70)
    print("\nUsage:")
    print("  python glitch_advanced_animated.py <image> <mode> [options]")
    print("\nModes:")
    print("  selective <region>  - Glitch only specific region")
    print("  colorflash <region> - Flash color in specific region")
    print("  colorshift <region> - Cycle colors in region")
    print("  overlay <overlay_image> - Flash overlay image on top")
    print("\nRegions:")
    print("  center, circle, left, right, top, bottom, edges")
    print("\nExamples:")
    print("  python glitch_advanced_animated.py pluto.jpg selective center")
    print("  python glitch_advanced_animated.py pluto.jpg colorflash circle")
    print("  python glitch_advanced_animated.py pluto.jpg colorshift edges")
    print("  python glitch_advanced_animated.py pluto.jpg overlay skull.png")
    print("\n" + "="*70 + "\n")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        show_menu()
        sys.exit(0)
    
    input_file = sys.argv[1]
    mode = sys.argv[2]
    
    if mode == 'selective':
        region = sys.argv[3] if len(sys.argv) > 3 else 'center'
        selective_glitch_animation(input_file, region=region)
    
    elif mode == 'colorflash':
        region = sys.argv[3] if len(sys.argv) > 3 else 'center'
        color_flash_region(input_file, region=region)
    
    elif mode == 'colorshift':
        region = sys.argv[3] if len(sys.argv) > 3 else 'center'
        color_shift_region(input_file, region=region)
    
    elif mode == 'overlay':
        if len(sys.argv) < 4:
            print("❌ Error: overlay mode requires an overlay image path")
            print("   Usage: python glitch_advanced_animated.py <base> overlay <overlay_image>")
            sys.exit(1)
        overlay_image = sys.argv[3]
        overlay_flashing_images(input_file, overlay_image)
    
    else:
        print(f"❌ Unknown mode: {mode}")
        show_menu()

