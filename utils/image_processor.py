from PIL import Image, ImageOps
import os
import math
from .apple_specs import APPLE_SPECS


class ScreenshotProcessor:
    def __init__(self):
        self.specs = APPLE_SPECS
    
    def find_closest_spec(self, width, height):
        """Find the closest Apple specification for given dimensions"""
        is_portrait = height > width
        
        best_match = None
        best_score = float('inf')
        
        for spec_key, spec_data in self.specs.items():
            if is_portrait:
                target_w, target_h = spec_data['portrait']
            else:
                target_w, target_h = spec_data['landscape']
            
            # Calculate similarity score based on aspect ratio and size
            aspect_ratio_input = width / height
            aspect_ratio_target = target_w / target_h
            
            aspect_diff = abs(aspect_ratio_input - aspect_ratio_target)
            size_diff = abs((width * height) - (target_w * target_h)) / (target_w * target_h)
            
            # Weight aspect ratio more heavily than size
            score = aspect_diff * 2 + size_diff * 0.5
            
            if score < best_score:
                best_score = score
                best_match = {
                    'spec_key': spec_key,
                    'name': spec_data['name'],
                    'dimensions': (target_w, target_h),
                    'orientation': 'portrait' if is_portrait else 'landscape'
                }
        
        return best_match
    
    def resize_image(self, image_path, target_dimensions):
        """Resize image to target specification using smart cropping"""
        try:
            with Image.open(image_path) as img:
                # Convert to RGB if necessary (handles PNG with transparency)
                if img.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                
                # Use ImageOps.fit for smart cropping with centering
                resized_img = ImageOps.fit(
                    img, 
                    target_dimensions, 
                    method=Image.Resampling.LANCZOS,
                    centering=(0.5, 0.5)  # Center crop
                )
                
                return resized_img
                
        except Exception as e:
            raise Exception(f"Error resizing image: {str(e)}")
    
    def process_screenshot(self, input_path, output_path):
        """Main processing function"""
        try:
            # Get original image dimensions
            with Image.open(input_path) as img:
                original_width, original_height = img.size
            
            # Find closest Apple specification
            best_match = self.find_closest_spec(original_width, original_height)
            
            if not best_match:
                raise Exception("Could not find suitable Apple specification")
            
            # Resize image
            resized_img = self.resize_image(input_path, best_match['dimensions'])
            
            # Save as PNG for best App Store compatibility
            resized_img.save(output_path, 'PNG', optimize=True)
            
            return {
                'success': True,
                'original_dimensions': (original_width, original_height),
                'target_dimensions': best_match['dimensions'],
                'device_name': best_match['name'],
                'orientation': best_match['orientation'],
                'output_path': output_path
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }