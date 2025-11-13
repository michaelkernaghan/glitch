#!/usr/bin/env python3
"""
Animated Glitch Art Generator
Create animated GIFs with flashing glitch effects
"""

from src.glitch_effects import GlitchArtist
from PIL import Image
import sys
import os


def create_flashing_glitch(input_path, output_path=None, frames=10, duration=100, 
                          flash_intensity='medium', flash_pattern='alternate'):
    """
    Create an animated GIF with flashing glitch effects
    
    Args:
        input_path: Path to your image
        output_path: Where to save the GIF
        frames: Number of frames in the animation
        duration: Duration per frame in milliseconds (lower = faster)
        flash_intensity: 'low', 'medium', or 'high'
        flash_pattern: 'alternate' (original/glitch), 'random' (different glitches), 
                      'progressive' (increasing intensity)
    """
    
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/animated_{name}.gif'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Loading image: {input_path}")
    print(f"⚡ Creating {frames} frames with {flash_pattern} pattern...")
    print(f"   Flash intensity: {flash_intensity}")
    print(f"   Frame duration: {duration}ms")
    
    # Load original image
    original = Image.open(input_path).convert('RGB')
    
    # Generate frames
    frame_list = []
    
    if flash_pattern == 'alternate':
        # Alternate between original and glitched
        glitcher = GlitchArtist(image=original.copy())
        glitcher.random_glitch_combo(intensity=flash_intensity)
        glitched = glitcher.get_image()
        
        for i in range(frames):
            if i % 2 == 0:
                frame_list.append(original.copy())
            else:
                frame_list.append(glitched.copy())
    
    elif flash_pattern == 'random':
        # Each frame has different random glitches
        for i in range(frames):
            if i % 2 == 0:
                # Original frame
                frame_list.append(original.copy())
            else:
                # New random glitch each time
                glitcher = GlitchArtist(image=original.copy())
                glitcher.random_glitch_combo(intensity=flash_intensity)
                frame_list.append(glitcher.get_image())
    
    elif flash_pattern == 'progressive':
        # Progressive intensity increase
        intensities = ['low', 'medium', 'high']
        for i in range(frames):
            if i % 4 == 0:
                frame_list.append(original.copy())
            else:
                intensity_idx = min((i % 4) - 1, len(intensities) - 1)
                glitcher = GlitchArtist(image=original.copy())
                glitcher.random_glitch_combo(intensity=intensities[intensity_idx])
                frame_list.append(glitcher.get_image())
    
    elif flash_pattern == 'strobe':
        # Fast alternating strobe effect
        for i in range(frames):
            if i % 2 == 0:
                frame_list.append(original.copy())
            else:
                glitcher = GlitchArtist(image=original.copy())
                # Quick, different glitches
                import random
                choice = random.choice(['rgb', 'datamosh', 'slice'])
                if choice == 'rgb':
                    glitcher.rgb_shift(r_shift=(20, 0), b_shift=(-20, 0))
                elif choice == 'datamosh':
                    glitcher.data_mosh(corruption_rate=0.02, block_size=15)
                else:
                    glitcher.slice_and_shift(num_slices=10, max_shift=50)
                frame_list.append(glitcher.get_image())
    
    # Save as animated GIF
    print(f"💾 Saving animated GIF...")
    frame_list[0].save(
        output_path,
        save_all=True,
        append_images=frame_list[1:],
        duration=duration,
        loop=0,  # Loop forever
        optimize=False
    )
    
    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✅ Saved: {output_path}")
    print(f"   {frames} frames @ {duration}ms/frame")
    print(f"   File size: {file_size:.2f}MB")
    print(f"   Total duration: {frames * duration / 1000:.1f}s per loop")


def create_multi_effect_flash(input_path, output_path=None, duration=150):
    """
    Create a GIF that flashes through different specific effects
    """
    
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/multi_effect_{name}.gif'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Loading image: {input_path}")
    print(f"⚡ Creating multi-effect animation...")
    
    original = Image.open(input_path).convert('RGB')
    frames = []
    
    # Original
    frames.append(original.copy())
    
    # RGB Shift
    print("   - RGB Shift frame")
    glitcher = GlitchArtist(image=original.copy())
    glitcher.rgb_shift(r_shift=(20, 0), b_shift=(-20, 0))
    frames.append(glitcher.get_image())
    
    # Original
    frames.append(original.copy())
    
    # Pixel Sort
    print("   - Pixel Sort frame")
    glitcher = GlitchArtist(image=original.copy())
    glitcher.pixel_sort(threshold=130, direction='horizontal')
    frames.append(glitcher.get_image())
    
    # Original
    frames.append(original.copy())
    
    # Data Mosh
    print("   - Data Mosh frame")
    glitcher = GlitchArtist(image=original.copy())
    glitcher.data_mosh(corruption_rate=0.02, block_size=15)
    frames.append(glitcher.get_image())
    
    # Original
    frames.append(original.copy())
    
    # Slice & Shift
    print("   - Slice & Shift frame")
    glitcher = GlitchArtist(image=original.copy())
    glitcher.slice_and_shift(num_slices=12, max_shift=50)
    frames.append(glitcher.get_image())
    
    # Save
    print(f"💾 Saving animated GIF...")
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        optimize=False
    )
    
    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✅ Saved: {output_path}")
    print(f"   {len(frames)} frames @ {duration}ms/frame")
    print(f"   File size: {file_size:.2f}MB")


def glitch_existing_gif(input_path, output_path=None, glitch_intensity='medium'):
    """
    Take an existing GIF and glitch each frame
    """
    
    if not os.path.exists(input_path):
        print(f"❌ Error: GIF not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/glitched_{name}.gif'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Loading GIF: {input_path}")
    
    # Open GIF
    gif = Image.open(input_path)
    
    # Get frame info
    try:
        frame_count = gif.n_frames
        duration = gif.info.get('duration', 100)
    except AttributeError:
        print("❌ Error: Not a valid animated GIF")
        return
    
    print(f"   Found {frame_count} frames")
    print(f"⚡ Applying {glitch_intensity} intensity glitches to each frame...")
    
    glitched_frames = []
    
    for i in range(frame_count):
        gif.seek(i)
        frame = gif.convert('RGB')
        
        # Glitch this frame
        glitcher = GlitchArtist(image=frame)
        glitcher.random_glitch_combo(intensity=glitch_intensity)
        glitched_frames.append(glitcher.get_image())
        
        if (i + 1) % 10 == 0:
            print(f"   Processed {i + 1}/{frame_count} frames...")
    
    print(f"💾 Saving glitched GIF...")
    glitched_frames[0].save(
        output_path,
        save_all=True,
        append_images=glitched_frames[1:],
        duration=duration,
        loop=0,
        optimize=False
    )
    
    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✅ Saved: {output_path}")
    print(f"   {frame_count} glitched frames")
    print(f"   File size: {file_size:.2f}MB")


def show_menu():
    """Show available animation modes"""
    print("\n" + "="*70)
    print("🎬 ANIMATED GLITCH ART GENERATOR")
    print("="*70)
    print("\nUsage:")
    print("  python glitch_animated.py <image> [mode] [options]")
    print("\nModes:")
    print("  flash          - Flashing glitch effect (default)")
    print("  multi          - Flash through different effects")
    print("  glitch-gif     - Glitch an existing GIF")
    print("\nFlash Patterns (for 'flash' mode):")
    print("  alternate      - Original ↔ Glitched (default)")
    print("  random         - Original ↔ Random glitches")
    print("  progressive    - Low → Medium → High intensity")
    print("  strobe         - Fast random strobe effect")
    print("\nExamples:")
    print("  python glitch_animated.py my_photo.jpg")
    print("  python glitch_animated.py my_photo.jpg flash random")
    print("  python glitch_animated.py my_photo.jpg flash strobe")
    print("  python glitch_animated.py my_photo.jpg multi")
    print("  python glitch_animated.py animation.gif glitch-gif")
    print("\n" + "="*70 + "\n")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        show_menu()
        sys.exit(0)
    
    input_file = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else 'flash'
    
    if mode == 'flash':
        pattern = sys.argv[3] if len(sys.argv) > 3 else 'alternate'
        create_flashing_glitch(
            input_file, 
            frames=20, 
            duration=100,
            flash_intensity='medium',
            flash_pattern=pattern
        )
    
    elif mode == 'multi':
        create_multi_effect_flash(input_file, duration=150)
    
    elif mode == 'glitch-gif':
        intensity = sys.argv[3] if len(sys.argv) > 3 else 'medium'
        glitch_existing_gif(input_file, glitch_intensity=intensity)
    
    else:
        print(f"❌ Unknown mode: {mode}")
        print("   Valid modes: flash, multi, glitch-gif")
        show_menu()

