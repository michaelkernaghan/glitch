"""
Glitch Art Effects Library
A collection of functions to create various glitch art effects for NFT generation
"""

import numpy as np
from PIL import Image
import random
from typing import Tuple, List
import io


class GlitchArtist:
    """Main class for applying glitch effects to images"""
    
    def __init__(self, image_path: str = None, image: Image.Image = None):
        """Initialize with either a path or PIL Image object"""
        if image_path:
            self.image = Image.open(image_path)
        elif image:
            self.image = image
        else:
            raise ValueError("Must provide either image_path or image")
        
        self.width, self.height = self.image.size
        self.original = self.image.copy()
    
    def reset(self):
        """Reset to original image"""
        self.image = self.original.copy()
        return self
    
    def pixel_sort(self, threshold: int = 128, direction: str = 'horizontal', 
                   reverse: bool = False) -> 'GlitchArtist':
        """
        Pixel sorting effect - sorts pixels by brightness
        
        Args:
            threshold: Brightness threshold (0-255) to determine sorting boundaries
            direction: 'horizontal' or 'vertical'
            reverse: Reverse sort order
        """
        img_array = np.array(self.image)
        
        if direction == 'horizontal':
            for i in range(self.height):
                row = img_array[i]
                # Calculate brightness
                brightness = np.mean(row, axis=1)
                # Find segments to sort
                mask = brightness < threshold
                
                # Sort pixels in segments
                start = None
                for j in range(len(mask)):
                    if mask[j] and start is None:
                        start = j
                    elif not mask[j] and start is not None:
                        segment = row[start:j]
                        segment_brightness = brightness[start:j]
                        sorted_indices = np.argsort(segment_brightness)
                        if reverse:
                            sorted_indices = sorted_indices[::-1]
                        row[start:j] = segment[sorted_indices]
                        start = None
        
        elif direction == 'vertical':
            for i in range(self.width):
                col = img_array[:, i]
                brightness = np.mean(col, axis=1)
                mask = brightness < threshold
                
                start = None
                for j in range(len(mask)):
                    if mask[j] and start is None:
                        start = j
                    elif not mask[j] and start is not None:
                        segment = col[start:j]
                        segment_brightness = brightness[start:j]
                        sorted_indices = np.argsort(segment_brightness)
                        if reverse:
                            sorted_indices = sorted_indices[::-1]
                        col[start:j] = segment[sorted_indices]
                        start = None
        
        self.image = Image.fromarray(img_array)
        return self
    
    def rgb_shift(self, r_shift: Tuple[int, int] = (0, 0), 
                  g_shift: Tuple[int, int] = (0, 0),
                  b_shift: Tuple[int, int] = (0, 0)) -> 'GlitchArtist':
        """
        Shift RGB channels independently to create chromatic aberration
        
        Args:
            r_shift: (x, y) shift for red channel
            g_shift: (x, y) shift for green channel
            b_shift: (x, y) shift for blue channel
        """
        img_array = np.array(self.image.convert('RGB'))
        
        # Create shifted channels
        r_channel = np.roll(img_array[:, :, 0], r_shift, axis=(1, 0))
        g_channel = np.roll(img_array[:, :, 1], g_shift, axis=(1, 0))
        b_channel = np.roll(img_array[:, :, 2], b_shift, axis=(1, 0))
        
        # Combine channels
        shifted = np.stack([r_channel, g_channel, b_channel], axis=2)
        self.image = Image.fromarray(shifted.astype(np.uint8))
        return self
    
    def scan_lines(self, line_height: int = 2, intensity: float = 0.3) -> 'GlitchArtist':
        """
        Add CRT-style scan lines
        
        Args:
            line_height: Height of each scan line in pixels
            intensity: Darkness of scan lines (0-1)
        """
        img_array = np.array(self.image).astype(float)
        
        for i in range(0, self.height, line_height * 2):
            end = min(i + line_height, self.height)
            img_array[i:end] *= (1 - intensity)
        
        self.image = Image.fromarray(img_array.astype(np.uint8))
        return self
    
    def data_mosh(self, corruption_rate: float = 0.01, block_size: int = 10) -> 'GlitchArtist':
        """
        Simulate data corruption by randomly corrupting blocks
        
        Args:
            corruption_rate: Percentage of blocks to corrupt (0-1)
            block_size: Size of corruption blocks
        """
        img_array = np.array(self.image)
        
        num_blocks = int((self.width * self.height) / (block_size ** 2) * corruption_rate)
        
        for _ in range(num_blocks):
            x = random.randint(0, self.width - block_size)
            y = random.randint(0, self.height - block_size)
            
            # Random corruption type
            corruption_type = random.choice(['shift', 'repeat', 'random'])
            
            if corruption_type == 'shift':
                # Shift block from another location
                src_x = random.randint(0, self.width - block_size)
                src_y = random.randint(0, self.height - block_size)
                img_array[y:y+block_size, x:x+block_size] = \
                    img_array[src_y:src_y+block_size, src_x:src_x+block_size]
            
            elif corruption_type == 'repeat':
                # Repeat a single row/column
                if random.random() > 0.5:
                    row = img_array[y, x:x+block_size]
                    img_array[y:y+block_size, x:x+block_size] = row
                else:
                    col = img_array[y:y+block_size, x:x+1]
                    img_array[y:y+block_size, x:x+block_size] = col
            
            elif corruption_type == 'random':
                # Random noise
                img_array[y:y+block_size, x:x+block_size] = \
                    np.random.randint(0, 256, (block_size, block_size, img_array.shape[2]))
        
        self.image = Image.fromarray(img_array.astype(np.uint8))
        return self
    
    def jpeg_compression_artifacts(self, quality: int = 5, iterations: int = 3) -> 'GlitchArtist':
        """
        Create JPEG compression artifacts by repeatedly compressing
        
        Args:
            quality: JPEG quality (1-100, lower = more artifacts)
            iterations: Number of compression cycles
        """
        img = self.image
        
        # Convert RGBA to RGB for JPEG compatibility
        if img.mode == 'RGBA':
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[3])
            img = rgb_img
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        for _ in range(iterations):
            buffer = io.BytesIO()
            img.save(buffer, format='JPEG', quality=quality)
            buffer.seek(0)
            img = Image.open(buffer)
        
        self.image = img
        return self
    
    def wave_distortion(self, amplitude: int = 10, frequency: float = 0.05, 
                       direction: str = 'horizontal') -> 'GlitchArtist':
        """
        Apply wave distortion effect
        
        Args:
            amplitude: Wave amplitude in pixels
            frequency: Wave frequency
            direction: 'horizontal' or 'vertical'
        """
        img_array = np.array(self.image)
        output = np.zeros_like(img_array)
        
        if direction == 'horizontal':
            for y in range(self.height):
                shift = int(amplitude * np.sin(2 * np.pi * frequency * y))
                output[y] = np.roll(img_array[y], shift, axis=0)
        else:
            for x in range(self.width):
                shift = int(amplitude * np.sin(2 * np.pi * frequency * x))
                output[:, x] = np.roll(img_array[:, x], shift, axis=0)
        
        self.image = Image.fromarray(output)
        return self
    
    def color_channel_swap(self, swap_type: str = 'random') -> 'GlitchArtist':
        """
        Swap color channels
        
        Args:
            swap_type: 'random', 'rgb_to_bgr', 'rgb_to_gbr', etc.
        """
        img_array = np.array(self.image.convert('RGB'))
        
        if swap_type == 'random':
            channels = [0, 1, 2]
            random.shuffle(channels)
            img_array = img_array[:, :, channels]
        elif swap_type == 'rgb_to_bgr':
            img_array = img_array[:, :, [2, 1, 0]]
        elif swap_type == 'rgb_to_gbr':
            img_array = img_array[:, :, [1, 2, 0]]
        elif swap_type == 'rgb_to_brg':
            img_array = img_array[:, :, [2, 0, 1]]
        
        self.image = Image.fromarray(img_array)
        return self
    
    def slice_and_shift(self, num_slices: int = 10, max_shift: int = 50) -> 'GlitchArtist':
        """
        Slice image horizontally and shift slices randomly
        
        Args:
            num_slices: Number of horizontal slices
            max_shift: Maximum shift amount in pixels
        """
        img_array = np.array(self.image)
        slice_height = self.height // num_slices
        
        for i in range(num_slices):
            start_y = i * slice_height
            end_y = start_y + slice_height
            shift = random.randint(-max_shift, max_shift)
            img_array[start_y:end_y] = np.roll(img_array[start_y:end_y], shift, axis=1)
        
        self.image = Image.fromarray(img_array)
        return self
    
    def random_glitch_combo(self, intensity: str = 'medium') -> 'GlitchArtist':
        """
        Apply a random combination of glitch effects
        
        Args:
            intensity: 'low', 'medium', or 'high'
        """
        effects = []
        
        if intensity == 'low':
            num_effects = random.randint(1, 2)
        elif intensity == 'medium':
            num_effects = random.randint(2, 4)
        else:  # high
            num_effects = random.randint(4, 6)
        
        available_effects = [
            lambda: self.rgb_shift(
                r_shift=(random.randint(-10, 10), 0),
                g_shift=(random.randint(-10, 10), 0),
                b_shift=(random.randint(-10, 10), 0)
            ),
            lambda: self.pixel_sort(
                threshold=random.randint(50, 200),
                direction=random.choice(['horizontal', 'vertical'])
            ),
            lambda: self.scan_lines(
                line_height=random.randint(2, 5),
                intensity=random.uniform(0.2, 0.5)
            ),
            lambda: self.data_mosh(
                corruption_rate=random.uniform(0.005, 0.02),
                block_size=random.randint(5, 20)
            ),
            lambda: self.wave_distortion(
                amplitude=random.randint(5, 20),
                frequency=random.uniform(0.01, 0.1),
                direction=random.choice(['horizontal', 'vertical'])
            ),
            lambda: self.slice_and_shift(
                num_slices=random.randint(5, 15),
                max_shift=random.randint(20, 100)
            ),
        ]
        
        selected_effects = random.sample(available_effects, min(num_effects, len(available_effects)))
        
        for effect in selected_effects:
            effect()
        
        return self
    
    def save(self, output_path: str, quality: int = 95):
        """Save the glitched image"""
        self.image.save(output_path, quality=quality)
        return self
    
    def show(self):
        """Display the image"""
        self.image.show()
        return self
    
    def get_image(self) -> Image.Image:
        """Return the PIL Image object"""
        return self.image

