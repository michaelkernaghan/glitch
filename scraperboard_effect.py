#!/usr/bin/env python3
"""
Digital Scraperboard Effect
Convert images to scraperboard/scratchboard style - high contrast etched look
Perfect for dark/gothic art before glitching
"""

from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageDraw
import numpy as np
import cv2
import sys
import os


def scraperboard_effect(input_path, output_path=None, style='dark', 
                       detail='high', threshold=128):
    """
    Create scraperboard/scratchboard effect
    
    Args:
        input_path: Path to input image
        output_path: Path to save output
        style: 'dark' (white lines on black) or 'light' (black lines on white)
        detail: 'low', 'medium', 'high' - amount of line detail
        threshold: Brightness threshold for conversion (0-255)
    """
    
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/scraperboard_{style}_{name}.png'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Loading image: {input_path}")
    print(f"⚡ Creating scraperboard effect")
    print(f"   Style: {style}")
    print(f"   Detail level: {detail}")
    
    # Load and convert to grayscale
    img = Image.open(input_path).convert('L')
    width, height = img.size
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)
    
    # Edge detection for scratch lines
    img_array = np.array(img)
    
    # Apply different edge detection based on detail level
    if detail == 'low':
        edges = cv2.Canny(img_array, 50, 150)
        kernel_size = 3
    elif detail == 'medium':
        edges = cv2.Canny(img_array, 30, 100)
        kernel_size = 2
    else:  # high
        edges = cv2.Canny(img_array, 20, 80)
        kernel_size = 1
    
    # Threshold to create high contrast
    _, thresh = cv2.threshold(img_array, threshold, 255, cv2.THRESH_BINARY)
    
    # Combine edges with threshold
    combined = cv2.bitwise_or(edges, thresh)
    
    # Invert for dark style (white lines on black)
    if style == 'dark':
        combined = cv2.bitwise_not(combined)
    
    # Convert back to PIL
    result = Image.fromarray(combined)
    
    # Add slight texture/grain for authenticity
    result = add_scratch_texture(result, detail)
    
    result.save(output_path)
    
    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✅ Saved: {output_path}")
    print(f"   File size: {file_size:.2f}MB")
    
    return result


def add_scratch_texture(img, detail='high'):
    """Add subtle scratch texture to simulate scraperboard"""
    img_array = np.array(img)
    
    # Add random scratch lines
    if detail == 'high':
        num_scratches = 500
    elif detail == 'medium':
        num_scratches = 200
    else:
        num_scratches = 50
    
    pil_img = Image.fromarray(img_array)
    draw = ImageDraw.Draw(pil_img)
    
    height, width = img_array.shape
    
    for _ in range(num_scratches):
        # Random scratch parameters
        x1 = np.random.randint(0, width)
        y1 = np.random.randint(0, height)
        length = np.random.randint(2, 10)
        angle = np.random.random() * 2 * np.pi
        
        x2 = int(x1 + length * np.cos(angle))
        y2 = int(y1 + length * np.sin(angle))
        
        # Only draw on appropriate areas
        if 0 <= x2 < width and 0 <= y2 < height:
            # Draw scratch
            color = 255 if img_array[y1, x1] > 128 else 0
            draw.line([(x1, y1), (x2, y2)], fill=color, width=1)
    
    return pil_img


def scraperboard_crosshatch(input_path, output_path=None, style='dark'):
    """
    Create scraperboard with crosshatch shading pattern
    """
    
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/scraperboard_crosshatch_{name}.png'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Creating crosshatch scraperboard effect...")
    
    # Load and convert
    img = Image.open(input_path).convert('L')
    width, height = img.size
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.5)
    
    img_array = np.array(img)
    
    # Edge detection
    edges = cv2.Canny(img_array, 30, 100)
    
    # Create crosshatch pattern based on brightness
    result = np.zeros_like(img_array)
    
    # Add crosshatch lines in darker areas
    line_spacing = 4
    for y in range(0, height, line_spacing):
        for x in range(width):
            if img_array[y, x] < 128:  # Dark areas
                if y < height:
                    result[y, x] = 255
    
    # Add perpendicular lines
    for x in range(0, width, line_spacing):
        for y in range(height):
            if img_array[y, x] < 100:  # Very dark areas
                if x < width:
                    result[y, x] = 255
    
    # Combine with edges
    result = cv2.bitwise_or(result, edges)
    
    # Invert for dark style
    if style == 'dark':
        result = cv2.bitwise_not(result)
    
    result_img = Image.fromarray(result)
    result_img.save(output_path)
    
    print(f"✅ Saved: {output_path}")
    
    return result_img


def scraperboard_gothic(input_path, output_path=None):
    """
    Create dramatic gothic scraperboard effect
    High contrast, heavy blacks, fine white lines
    """
    
    if not os.path.exists(input_path):
        print(f"❌ Error: Image not found at {input_path}")
        return
    
    if output_path is None:
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = f'examples_output/scraperboard_gothic_{name}.png'
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    print(f"🎨 Creating GOTHIC scraperboard effect...")
    
    img = Image.open(input_path).convert('L')
    
    # Heavy contrast enhancement
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(3.0)
    
    # Darken overall
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(0.7)
    
    img_array = np.array(img)
    
    # Very fine edge detection
    edges = cv2.Canny(img_array, 15, 60)
    
    # Very high threshold - mostly black
    _, thresh = cv2.threshold(img_array, 100, 255, cv2.THRESH_BINARY)
    
    # Combine
    combined = cv2.bitwise_or(edges, thresh)
    
    # Invert - white lines on black
    combined = cv2.bitwise_not(combined)
    
    result = Image.fromarray(combined)
    result.save(output_path)
    
    print(f"✅ Saved: {output_path}")
    
    return result


def show_menu():
    """Show usage"""
    print("\n" + "="*70)
    print("🎨 DIGITAL SCRAPERBOARD EFFECT")
    print("="*70)
    print("\nUsage:")
    print("  python scraperboard_effect.py <image> [mode] [detail]")
    print("\nModes:")
    print("  dark       - White lines on black (default, gothic)")
    print("  light      - Black lines on white")
    print("  crosshatch - Crosshatch shading pattern")
    print("  gothic     - Heavy blacks, dramatic contrast")
    print("\nDetail levels (for dark/light modes):")
    print("  low    - Bold, simple lines")
    print("  medium - Balanced detail")
    print("  high   - Maximum line detail (default)")
    print("\nExamples:")
    print("  python scraperboard_effect.py skull.jpg")
    print("  python scraperboard_effect.py skull.jpg dark high")
    print("  python scraperboard_effect.py skull.jpg gothic")
    print("  python scraperboard_effect.py skull.jpg crosshatch")
    print("\nPerfect for dark/gothic/occult imagery!")
    print("Then glitch the scraperboard result for underground art!")
    print("\n" + "="*70 + "\n")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        show_menu()
        sys.exit(0)
    
    input_file = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else 'dark'
    detail = sys.argv[3] if len(sys.argv) > 3 else 'high'
    
    if mode == 'gothic':
        scraperboard_gothic(input_file)
    elif mode == 'crosshatch':
        scraperboard_crosshatch(input_file, style='dark')
    else:  # dark or light
        scraperboard_effect(input_file, style=mode, detail=detail)

