#!/usr/bin/env python3
"""
RED Competition Entry Creator
Create 5 red-themed glitch art pieces for Fusion Art RED 2025
"""

from src.glitch_effects import GlitchArtist
from PIL import Image
import numpy as np
import os


def create_red_pieces():
    """Create all 5 pieces for RED competition"""
    
    os.makedirs('examples_output/red_competition', exist_ok=True)
    
    print("🔴" * 35)
    print("   CREATING RED COMPETITION ENTRIES")
    print("🔴" * 35)
    print(f"\n✨ Creating 5 pieces for Fusion Art RED 2025")
    print(f"⏰ Deadline: December 1, 2025\n")
    
    # Piece 1: Blood Red Pluto Pulse
    print("="*70)
    print("[1/5] 'Blood Moon Pluto' - Pulsing blood red animation")
    print("="*70)
    
    base1 = Image.open('imported_images/pluto.jpg').convert('RGB')
    width1, height1 = base1.size
    
    blood_reds = [(139, 0, 0), (178, 34, 34), (220, 20, 60), (255, 0, 0)]
    frames1 = []
    
    for i in range(75):
        frame = base1.copy()
        pulse = (np.sin(2 * np.pi * i / 30) + 1) / 2
        opacity = 0.6 * pulse
        
        color_idx = (i // 15) % len(blood_reds)
        color = blood_reds[color_idx]
        
        if opacity > 0:
            color_layer = Image.new('RGB', (width1, height1), color)
            frame = Image.blend(frame, color_layer, opacity)
        
        frames1.append(frame)
    
    frames1[0].save(
        'examples_output/red_competition/01_blood_moon_pluto.gif',
        save_all=True, append_images=frames1[1:], duration=30, loop=0
    )
    print("✅ Saved: 01_blood_moon_pluto.gif (Blood red pulsing deity)\n")
    
    
    # Piece 2: Crimson Glitch Static
    print("="*70)
    print("[2/5] 'Crimson Corruption' - Static glitch with red enhancement")
    print("="*70)
    
    glitcher2 = GlitchArtist(image_path='imported_images/6.jpg')
    glitcher2.random_glitch_combo(intensity='high')
    glitched2 = glitcher2.get_image()
    
    # Red enhancement
    img_array2 = np.array(glitched2)
    img_array2[:, :, 0] = np.clip(img_array2[:, :, 0] * 1.5, 0, 255)
    img_array2[:, :, 1] = np.clip(img_array2[:, :, 1] * 0.5, 0, 255)
    img_array2[:, :, 2] = np.clip(img_array2[:, :, 2] * 0.5, 0, 255)
    
    Image.fromarray(img_array2.astype(np.uint8)).save(
        'examples_output/red_competition/02_crimson_corruption.png'
    )
    print("✅ Saved: 02_crimson_corruption.png (Red glitch static)\n")
    
    
    # Piece 3: Fire Red DALLE
    print("="*70)
    print("[3/5] 'Infernal Transmission' - Fire red skull animation")
    print("="*70)
    
    base3 = Image.open('imported_images/DALLE2~4.PNG').convert('RGB')
    width3, height3 = base3.size
    
    fire_reds = [(255, 69, 0), (255, 0, 0), (255, 140, 0), (220, 20, 60)]
    frames3 = []
    
    for i in range(60):
        # Glitch every 8 frames
        if i % 8 == 0:
            glitcher = GlitchArtist(image=base3.copy())
            glitcher.random_glitch_combo(intensity='low')
            frame = glitcher.get_image()
        else:
            frame = frames3[-1].copy() if frames3 else base3.copy()
        
        # Fire red pulse
        pulse = (np.sin(2 * np.pi * i / 20) + 1) / 2
        opacity = 0.5 * pulse
        
        color = fire_reds[(i // 15) % len(fire_reds)]
        color_layer = Image.new('RGB', (width3, height3), color)
        frame = Image.blend(frame, color_layer, opacity)
        
        frames3.append(frame)
    
    frames3[0].save(
        'examples_output/red_competition/03_infernal_transmission.gif',
        save_all=True, append_images=frames3[1:], duration=40, loop=0
    )
    print("✅ Saved: 03_infernal_transmission.gif (Fire red skull)\n")
    
    
    # Piece 4: Deep Red ChatGPT
    print("="*70)
    print("[4/5] 'Scarlet Decay' - Dark red glitch with selective circle")
    print("="*70)
    
    base4 = Image.open('imported_images/ChatGPT Image Nov 14, 2025, 11_54_06 AM.png').convert('RGB')
    
    # Apply glitch
    glitcher4 = GlitchArtist(image=base4)
    glitcher4.rgb_shift(r_shift=(20, 0), b_shift=(-20, 0))
    glitcher4.pixel_sort(threshold=130, direction='horizontal')
    glitched4 = glitcher4.get_image()
    
    # Deep red tint
    img_array4 = np.array(glitched4)
    img_array4[:, :, 0] = np.clip(img_array4[:, :, 0] * 1.4, 0, 255)
    img_array4[:, :, 1] = np.clip(img_array4[:, :, 1] * 0.3, 0, 255)
    img_array4[:, :, 2] = np.clip(img_array4[:, :, 2] * 0.3, 0, 255)
    
    Image.fromarray(img_array4.astype(np.uint8)).save(
        'examples_output/red_competition/04_scarlet_decay.png'
    )
    print("✅ Saved: 04_scarlet_decay.png (Dark red glitch)\n")
    
    
    # Piece 5: Neon Red with Overlay
    print("="*70)
    print("[5/5] 'Neon Blood Oracle' - Red overlay + glitching")
    print("="*70)
    
    base5 = Image.open('imported_images/17.jpg').convert('RGB')
    width5, height5 = base5.size
    
    overlay5 = Image.open('imported_images/PfEFRlBu.jpg').convert('RGBA')
    overlay5 = overlay5.resize((int(width5 * 0.2), int(height5 * 0.2)), Image.LANCZOS)
    
    neon_reds = [(255, 0, 0), (255, 20, 147), (255, 0, 100), (255, 51, 0)]
    frames5 = []
    
    import random
    for i in range(40):
        # Moderate glitching
        if i % 6 == 0:
            glitcher = GlitchArtist(image=base5.copy())
            glitcher.random_glitch_combo(intensity='medium')
            frame = glitcher.get_image().convert('RGBA')
        else:
            frame = frames5[-1].convert('RGBA') if frames5 else base5.copy().convert('RGBA')
        
        # Red color overlay
        color = neon_reds[(i // 10) % len(neon_reds)]
        color_layer = Image.new('RGB', (width5, height5), color)
        frame_rgb = frame.convert('RGB')
        pulse = (np.sin(2 * np.pi * i / 25) + 1) / 2
        frame_rgb = Image.blend(frame_rgb, color_layer, 0.4 * pulse)
        frame = frame_rgb.convert('RGBA')
        
        # Random overlay
        if random.random() < 0.7:
            pos_x = random.randint(0, width5 - overlay5.width)
            pos_y = random.randint(0, height5 - overlay5.height)
            frame.paste(overlay5, (pos_x, pos_y), overlay5)
        
        frames5.append(frame.convert('RGB'))
    
    frames5[0].save(
        'examples_output/red_competition/05_neon_blood_oracle.gif',
        save_all=True, append_images=frames5[1:], duration=80, loop=0
    )
    print("✅ Saved: 05_neon_blood_oracle.gif (Neon red with overlays)\n")
    
    
    # Summary
    print("\n" + "🔴" * 35)
    print("   COMPETITION ENTRIES COMPLETE!")
    print("🔴" * 35)
    print("\n📁 All files in: examples_output/red_competition/")
    print("\n5 Pieces Created:")
    print("  1. Blood Moon Pluto - Blood red pulsing animation")
    print("  2. Crimson Corruption - Red-enhanced glitch static")
    print("  3. Infernal Transmission - Fire red skull animation")
    print("  4. Scarlet Decay - Dark red glitch")
    print("  5. Neon Blood Oracle - Neon red with overlays")
    print("\n📋 Next Steps:")
    print("  1. Review all 5 pieces")
    print("  2. Select your best 3-5 for submission")
    print("  3. Write titles and descriptions")
    print("  4. Submit to Fusion Art before December 1!")
    print(f"\n🔗 Competition: https://artisttrust.org/opportunities/red-2025-art-competition-calls-submissions/")
    print()


if __name__ == '__main__':
    create_red_pieces()

