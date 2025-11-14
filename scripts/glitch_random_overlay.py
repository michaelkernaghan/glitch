#!/usr/bin/env python3
"""
Random Overlay + Glitching Base Animation
Flash an overlay image in random locations over a glitching base image
"""

import sys; sys.path.append(".."); from src.glitch_effects import GlitchArtist
from PIL import Image
import random
import sys
import os


def random_overlay_with_glitch(base_path, overlay_path, output_path=None, 
                               frames=30, duration=80, overlay_scale=0.3,
                               glitch_intensity='medium'):
    """
    Create animation with:
    - Base image glitching with random effects each frame
    - Overlay image flashing in random positions
    
    Args:
        base_path: Path to base image (will be glitched)
        overlay_path: Path to overlay image (will flash around)
        output_path: Output GIF path
        frames: Number of frames
        duration: Duration per frame in ms
        overlay_scale: Size of overlay relative to base (0.1-1.0)
        glitch_intensity: 'low', 'medium', 'high'
    """
    
    if not os.path.exists(base_path):
        print(f"❌ Error: Base image not found at {base_path}")
        return
    
    if not os.path.exists(overlay_path):
        print(f"❌ Error: Overlay image not found at {overlay_path}")
        return
    
    if output_path is None:
        base_name = os.path.splitext(os.path.basename(base_path))[0]
        overlay_name = os.path.splitext(os.path.basename(overlay_path))[0]
        output_path = f'examples_output/random_overlay_{base_name}_{overlay_name}.gif'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Loading images...")
    print(f"   Base: {base_path}")
    print(f"   Overlay: {overlay_path}")
    print(f"⚡ Creating random overlay + glitch animation")
    print(f"   Frames: {frames}")
    print(f"   Glitch intensity: {glitch_intensity}")
    
    # Load base image
    base_original = Image.open(base_path).convert('RGB')
    width, height = base_original.size
    
    # Load and scale overlay
    overlay = Image.open(overlay_path).convert('RGBA')
    overlay_size = (int(width * overlay_scale), int(height * overlay_scale))
    overlay = overlay.resize(overlay_size, Image.LANCZOS)
    overlay_width, overlay_height = overlay.size
    
    frame_list = []
    
    for i in range(frames):
        # Create glitched version of base for this frame
        glitcher = GlitchArtist(image=base_original.copy())
        glitcher.random_glitch_combo(intensity=glitch_intensity)
        glitched_base = glitcher.get_image().convert('RGBA')
        
        # Randomly decide if overlay appears this frame (70% chance)
        if random.random() < 0.7:
            # Random position for overlay
            max_x = width - overlay_width
            max_y = height - overlay_height
            pos_x = random.randint(0, max_x) if max_x > 0 else 0
            pos_y = random.randint(0, max_y) if max_y > 0 else 0
            
            # Paste overlay at random position
            glitched_base.paste(overlay, (pos_x, pos_y), overlay)
        
        # Convert to RGB for GIF
        frame = glitched_base.convert('RGB')
        frame_list.append(frame)
        
        if (i + 1) % 10 == 0:
            print(f"   Processed {i + 1}/{frames} frames...")
    
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
    print(f"   {frames} frames with random overlay placement")
    print(f"   File size: {file_size:.2f}MB")


def random_overlay_static_base(base_path, overlay_path, output_path=None,
                               frames=20, duration=100, overlay_scale=0.3):
    """
    Static base image with overlay flashing in random locations
    (base doesn't glitch, only overlay moves)
    """
    
    if not os.path.exists(base_path):
        print(f"❌ Error: Base image not found at {base_path}")
        return
    
    if not os.path.exists(overlay_path):
        print(f"❌ Error: Overlay image not found at {overlay_path}")
        return
    
    if output_path is None:
        base_name = os.path.splitext(os.path.basename(base_path))[0]
        overlay_name = os.path.splitext(os.path.basename(overlay_path))[0]
        output_path = f'examples_output/static_overlay_{base_name}_{overlay_name}.gif'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Creating static base + random overlay animation")
    
    # Load base image (stays same)
    base = Image.open(base_path).convert('RGBA')
    width, height = base.size
    
    # Load and scale overlay
    overlay = Image.open(overlay_path).convert('RGBA')
    overlay_size = (int(width * overlay_scale), int(height * overlay_scale))
    overlay = overlay.resize(overlay_size, Image.LANCZOS)
    overlay_width, overlay_height = overlay.size
    
    frame_list = []
    
    for i in range(frames):
        current_frame = base.copy()
        
        # Alternate: show overlay or not
        if i % 2 == 1:
            # Random position
            max_x = width - overlay_width
            max_y = height - overlay_height
            pos_x = random.randint(0, max_x) if max_x > 0 else 0
            pos_y = random.randint(0, max_y) if max_y > 0 else 0
            
            current_frame.paste(overlay, (pos_x, pos_y), overlay)
        
        frame = current_frame.convert('RGB')
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


def show_menu():
    """Show usage"""
    print("\n" + "="*70)
    print("🎨 RANDOM OVERLAY + GLITCH ANIMATION")
    print("="*70)
    print("\nUsage:")
    print("  python glitch_random_overlay.py <base> <overlay> [mode]")
    print("\nModes:")
    print("  glitch - Base glitches + overlay in random positions (default)")
    print("  static - Base static + overlay in random positions")
    print("\nExamples:")
    print("  python glitch_random_overlay.py 17.jpg skull.png")
    print("  python glitch_random_overlay.py 17.jpg skull.png glitch")
    print("  python glitch_random_overlay.py 17.jpg skull.png static")
    print("\n" + "="*70 + "\n")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        show_menu()
        sys.exit(0)
    
    base_image = sys.argv[1]
    overlay_image = sys.argv[2]
    mode = sys.argv[3] if len(sys.argv) > 3 else 'glitch'
    
    if mode == 'glitch':
        random_overlay_with_glitch(
            base_image, 
            overlay_image,
            frames=30,
            duration=80,
            overlay_scale=0.25,
            glitch_intensity='medium'
        )
    elif mode == 'static':
        random_overlay_static_base(
            base_image,
            overlay_image,
            frames=20,
            duration=100,
            overlay_scale=0.3
        )
    else:
        print(f"❌ Unknown mode: {mode}")
        show_menu()

