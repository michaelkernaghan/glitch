"""
Generative Glitch Art - Create glitch art from scratch
Perfect for NFT collections with procedurally generated unique pieces
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import random
from typing import Tuple, List
import colorsys


class GenerativeGlitchArt:
    """Generate glitch art from scratch using procedural generation"""
    
    def __init__(self, width: int = 1000, height: int = 1000):
        self.width = width
        self.height = height
        self.image = None
    
    def create_base_gradient(self, colors: List[Tuple[int, int, int]] = None) -> Image.Image:
        """Create a gradient base image"""
        if colors is None:
            # Generate random colors
            colors = [
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                for _ in range(random.randint(2, 5))
            ]
        
        img = Image.new('RGB', (self.width, self.height))
        draw = ImageDraw.Draw(img)
        
        # Create gradient
        for y in range(self.height):
            # Calculate which colors to blend
            position = y / self.height * (len(colors) - 1)
            idx = int(position)
            blend = position - idx
            
            if idx >= len(colors) - 1:
                color = colors[-1]
            else:
                color1 = colors[idx]
                color2 = colors[idx + 1]
                color = tuple(
                    int(c1 * (1 - blend) + c2 * blend)
                    for c1, c2 in zip(color1, color2)
                )
            
            draw.line([(0, y), (self.width, y)], fill=color)
        
        self.image = img
        return img
    
    def create_geometric_base(self, num_shapes: int = 50) -> Image.Image:
        """Create a base with random geometric shapes"""
        img = Image.new('RGB', (self.width, self.height), color=(0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        for _ in range(num_shapes):
            shape_type = random.choice(['rectangle', 'ellipse', 'line', 'polygon'])
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
            if shape_type == 'rectangle':
                x1 = random.randint(0, self.width)
                y1 = random.randint(0, self.height)
                x2 = random.randint(x1, self.width)
                y2 = random.randint(y1, self.height)
                draw.rectangle([x1, y1, x2, y2], fill=color, outline=color)
            
            elif shape_type == 'ellipse':
                x1 = random.randint(0, self.width)
                y1 = random.randint(0, self.height)
                x2 = random.randint(x1, self.width)
                y2 = random.randint(y1, self.height)
                draw.ellipse([x1, y1, x2, y2], fill=color, outline=color)
            
            elif shape_type == 'line':
                x1 = random.randint(0, self.width)
                y1 = random.randint(0, self.height)
                x2 = random.randint(0, self.width)
                y2 = random.randint(0, self.height)
                width = random.randint(1, 10)
                draw.line([x1, y1, x2, y2], fill=color, width=width)
            
            elif shape_type == 'polygon':
                points = [
                    (random.randint(0, self.width), random.randint(0, self.height))
                    for _ in range(random.randint(3, 8))
                ]
                draw.polygon(points, fill=color, outline=color)
        
        self.image = img
        return img
    
    def create_noise_base(self, noise_type: str = 'color') -> Image.Image:
        """Create a noise-based image"""
        if noise_type == 'color':
            # RGB noise
            noise = np.random.randint(0, 256, (self.height, self.width, 3), dtype=np.uint8)
        elif noise_type == 'grayscale':
            # Grayscale noise
            noise = np.random.randint(0, 256, (self.height, self.width), dtype=np.uint8)
            noise = np.stack([noise] * 3, axis=2)
        elif noise_type == 'perlin':
            # Simplified Perlin-like noise
            noise = self._generate_perlin_noise()
        
        self.image = Image.fromarray(noise)
        return self.image
    
    def _generate_perlin_noise(self) -> np.ndarray:
        """Generate Perlin-like noise"""
        # Create low-resolution noise
        scale = 10
        low_res_height = self.height // scale
        low_res_width = self.width // scale
        
        low_res = np.random.randint(0, 256, (low_res_height, low_res_width, 3), dtype=np.uint8)
        
        # Upscale with interpolation
        img = Image.fromarray(low_res)
        img = img.resize((self.width, self.height), Image.BILINEAR)
        
        return np.array(img)
    
    def create_vaporwave_aesthetic(self) -> Image.Image:
        """Create a vaporwave-style base"""
        # Vaporwave color palette
        colors = [
            (255, 113, 206),  # Hot pink
            (1, 255, 255),    # Cyan
            (255, 71, 255),   # Magenta
            (1, 1, 255),      # Blue
            (255, 255, 1),    # Yellow
        ]
        
        img = Image.new('RGB', (self.width, self.height))
        draw = ImageDraw.Draw(img)
        
        # Create gradient background
        for y in range(self.height):
            color_idx = int((y / self.height) * (len(colors) - 1))
            next_idx = min(color_idx + 1, len(colors) - 1)
            blend = (y / self.height) * (len(colors) - 1) - color_idx
            
            color = tuple(
                int(colors[color_idx][i] * (1 - blend) + colors[next_idx][i] * blend)
                for i in range(3)
            )
            draw.line([(0, y), (self.width, y)], fill=color)
        
        # Add grid
        grid_spacing = 50
        for x in range(0, self.width, grid_spacing):
            draw.line([(x, 0), (x, self.height)], fill=(255, 255, 255, 128), width=2)
        
        for y in range(0, self.height, grid_spacing):
            draw.line([(0, y), (self.width, y)], fill=(255, 255, 255, 128), width=2)
        
        self.image = img
        return img
    
    def create_cyberpunk_aesthetic(self) -> Image.Image:
        """Create a cyberpunk-style base"""
        # Dark background with neon accents
        img = Image.new('RGB', (self.width, self.height), color=(10, 0, 20))
        draw = ImageDraw.Draw(img)
        
        # Neon colors
        neon_colors = [
            (0, 255, 255),    # Cyan
            (255, 0, 255),    # Magenta
            (255, 255, 0),    # Yellow
            (0, 255, 0),      # Green
        ]
        
        # Add random neon lines and shapes
        for _ in range(100):
            color = random.choice(neon_colors)
            shape_type = random.choice(['line', 'rectangle', 'circle'])
            
            if shape_type == 'line':
                x1 = random.randint(0, self.width)
                y1 = random.randint(0, self.height)
                x2 = random.randint(0, self.width)
                y2 = random.randint(0, self.height)
                draw.line([x1, y1, x2, y2], fill=color, width=random.randint(1, 5))
            
            elif shape_type == 'rectangle':
                x1 = random.randint(0, self.width)
                y1 = random.randint(0, self.height)
                w = random.randint(10, 100)
                h = random.randint(10, 100)
                draw.rectangle([x1, y1, x1+w, y1+h], outline=color, width=2)
            
            elif shape_type == 'circle':
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
                r = random.randint(5, 50)
                draw.ellipse([x-r, y-r, x+r, y+r], outline=color, width=2)
        
        self.image = img
        return img
    
    def generate_unique_nft(self, seed: int = None, style: str = 'random') -> Image.Image:
        """
        Generate a unique NFT-ready glitch art piece
        
        Args:
            seed: Random seed for reproducibility
            style: 'random', 'vaporwave', 'cyberpunk', 'geometric', 'gradient', 'noise'
        """
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
        
        # Choose style
        if style == 'random':
            style = random.choice(['vaporwave', 'cyberpunk', 'geometric', 'gradient', 'noise'])
        
        # Create base
        if style == 'vaporwave':
            self.create_vaporwave_aesthetic()
        elif style == 'cyberpunk':
            self.create_cyberpunk_aesthetic()
        elif style == 'geometric':
            self.create_geometric_base(num_shapes=random.randint(30, 100))
        elif style == 'gradient':
            self.create_base_gradient()
        elif style == 'noise':
            self.create_noise_base(noise_type=random.choice(['color', 'perlin']))
        
        return self.image
    
    def get_image(self) -> Image.Image:
        """Return the generated image"""
        return self.image
    
    def save(self, output_path: str, quality: int = 95):
        """Save the generated image"""
        if self.image:
            self.image.save(output_path, quality=quality)
        return self


def generate_nft_collection(num_pieces: int, output_dir: str = './nft_collection',
                            width: int = 1000, height: int = 1000):
    """
    Generate a complete NFT collection with unique glitch art pieces
    
    Args:
        num_pieces: Number of NFTs to generate
        output_dir: Directory to save the collection
        width: Image width
        height: Image height
    """
    import os
    from src.glitch_effects import GlitchArtist
    
    os.makedirs(output_dir, exist_ok=True)
    
    for i in range(num_pieces):
        print(f"Generating NFT {i+1}/{num_pieces}...")
        
        # Generate base
        generator = GenerativeGlitchArt(width=width, height=height)
        base_image = generator.generate_unique_nft(seed=i)
        
        # Apply glitch effects
        glitcher = GlitchArtist(image=base_image)
        glitcher.random_glitch_combo(intensity=random.choice(['medium', 'high']))
        
        # Save
        output_path = os.path.join(output_dir, f'glitch_nft_{i:04d}.png')
        glitcher.save(output_path)
    
    print(f"Collection complete! {num_pieces} NFTs saved to {output_dir}")


if __name__ == '__main__':
    # Example: Generate a small collection
    generate_nft_collection(num_pieces=10, output_dir='./sample_collection')

