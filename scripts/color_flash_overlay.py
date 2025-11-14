#!/usr/bin/env python3
"""
Color Flash Overlay Effect
Create fast flashing color overlays like the reaper.gif effect
"""

from PIL import Image, ImageEnhance
import numpy as np
import sys
import os


def pulsing_color_overlay(input_path, output_path=None, frames=75, duration=30,
                         colors=None, intensity=0.5, pattern='pulse'):
    """
    Create animation with pulsing/flashing color overlays
    
    Args:
        input_path: Base image
        output_path: Output GIF path
        frames: Number of frames (default 75 like reaper.gif)
        duration: Milliseconds per frame (30 = very fast)
        colors: List of RGB tuples for flashing colors
        intensity: Overlay intensity (0.0-1.0)
        pattern: 'pulse', 'flash', 'wave', 'random'
    """
    
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/color_flash_{name}.gif'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    # Default purple/magenta palette like reaper.gif
    if colors is None:
        colors = [
            (150, 0, 200),    # Purple
            (200, 0, 150),    # Magenta
            (100, 0, 255),    # Deep purple
            (255, 0, 200),    # Hot magenta
        ]
    
    print(f"🎨 Creating color flash overlay animation")
    print(f"   Pattern: {pattern}")
    print(f"   Frames: {frames} @ {duration}ms")
    print(f"   Colors: {len(colors)} color palette")
    
    # Load base image
    base = Image.open(input_path).convert('RGB')
    width, height = base.size
    
    frame_list = []
    
    for i in range(frames):
        current_frame = base.copy()
        
        if pattern == 'pulse':
            # Pulsing - smooth sine wave
            pulse = (np.sin(2 * np.pi * i / 30) + 1) / 2  # 0 to 1
            opacity = intensity * pulse
            
            # Cycle through colors
            color_idx = (i // 15) % len(colors)
            color = colors[color_idx]
        
        elif pattern == 'flash':
            # Fast flashing - on/off
            if i % 3 == 0:
                opacity = intensity
            else:
                opacity = 0
            
            color_idx = (i // 10) % len(colors)
            color = colors[color_idx]
        
        elif pattern == 'wave':
            # Wave pattern - smooth color transitions
            progress = i / frames
            opacity = intensity * (0.5 + 0.5 * np.sin(progress * 4 * np.pi))
            
            # Smooth color transitions
            color_progress = (i % 30) / 30
            color_idx = int((i / 30) % len(colors))
            next_idx = (color_idx + 1) % len(colors)
            
            # Blend between two colors
            color = tuple(
                int(colors[color_idx][j] * (1 - color_progress) + 
                    colors[next_idx][j] * color_progress)
                for j in range(3)
            )
        
        elif pattern == 'random':
            # Random flashing
            import random
            opacity = intensity if random.random() > 0.4 else 0
            color = random.choice(colors)
        
        # Create color overlay
        if opacity > 0:
            color_layer = Image.new('RGB', (width, height), color)
            current_frame = Image.blend(current_frame, color_layer, opacity)
        
        frame_list.append(current_frame)
        
        if (i + 1) % 25 == 0:
            print(f'   Processed {i + 1}/{frames} frames...')
    
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
    print(f"   {frames} frames @ {duration}ms/frame")
    print(f"   Total duration: {frames * duration / 1000:.1f}s")
    print(f"   File size: {file_size:.2f}MB")


def color_flash_with_glitch(input_path, output_path=None, frames=60, duration=40):
    """
    Combine color flashing with glitch effects
    """
    import sys; sys.path.append(".."); from src.glitch_effects import GlitchArtist
    
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/glitch_colorflash_{name}.gif'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Creating glitch + color flash animation")
    
    base_original = Image.open(input_path).convert('RGB')
    width, height = base_original.size
    
    colors = [
        (150, 0, 200),    # Purple
        (200, 0, 150),    # Magenta
        (0, 200, 255),    # Cyan
        (255, 0, 100),    # Hot pink
    ]
    
    frame_list = []
    
    for i in range(frames):
        # Glitch every few frames
        if i % 8 == 0:
            glitcher = GlitchArtist(image=base_original.copy())
            glitcher.random_glitch_combo(intensity='low')
            current_frame = glitcher.get_image()
        else:
            if frame_list:
                current_frame = frame_list[-1].copy()
            else:
                current_frame = base_original.copy()
        
        # Add pulsing color overlay
        pulse = (np.sin(2 * np.pi * i / 20) + 1) / 2
        opacity = 0.4 * pulse
        
        color_idx = (i // 15) % len(colors)
        color = colors[color_idx]
        
        if opacity > 0.1:
            color_layer = Image.new('RGB', (width, height), color)
            current_frame = Image.blend(current_frame, color_layer, opacity)
        
        frame_list.append(current_frame)
    
    print(f"💾 Saving...")
    frame_list[0].save(
        output_path,
        save_all=True,
        append_images=frame_list[1:],
        duration=duration,
        loop=0,
        optimize=False
    )
    
    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✅ Saved: {output_path} ({file_size:.2f}MB)")


def show_menu():
    """Show usage"""
    print("\n" + "="*70)
    print("🎨 COLOR FLASH OVERLAY EFFECT")
    print("="*70)
    print("\nCreate fast flashing color overlays like reaper.gif")
    print("\nUsage:")
    print("  python color_flash_overlay.py <image> [pattern]")
    print("\nPatterns:")
    print("  pulse   - Smooth pulsing colors (default, like reaper.gif)")
    print("  flash   - Fast on/off flashing")
    print("  wave    - Smooth color wave transitions")
    print("  random  - Random color flashing")
    print("  glitch  - Color flash + glitch effects combined")
    print("\nExamples:")
    print("  python color_flash_overlay.py skull.jpg pulse")
    print("  python color_flash_overlay.py deity.jpg flash")
    print("  python color_flash_overlay.py dark.jpg glitch")
    print("\n" + "="*70 + "\n")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        show_menu()
        sys.exit(0)
    
    input_file = sys.argv[1]
    pattern = sys.argv[2] if len(sys.argv) > 2 else 'pulse'
    
    if pattern == 'glitch':
        color_flash_with_glitch(input_file, frames=60, duration=40)
    else:
        pulsing_color_overlay(input_file, pattern=pattern, frames=75, duration=30)

