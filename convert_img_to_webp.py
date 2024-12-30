# convert_img_to_webp
import os
from PIL import Image
from PIL import ImageOps

def convert_img_to_webp(img_path):
    try:
        # Open the image
        img = Image.open(img_path)
        
        # Calculate new dimensions while maintaining aspect ratio
        max_size = 1920
        ratio = min(max_size/img.width, max_size/img.height)
        if ratio < 1:
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.LANCZOS)
        
        # Prepare the output path
        output_path = os.path.splitext(img_path)[0] + '.webp'
        
        # Save as WebP with quality adjustment to keep file size under 1024KB
        quality = 80
        while True:
            img.save(output_path, 'WEBP', quality=quality)
            if os.path.getsize(output_path) <= 1024 * 1024 or quality <= 5:
                break
            quality -= 5
            
        # Remove original file if conversion successful
        os.remove(img_path)
        
    except Exception as e:
        print(f"Error converting {img_path}: {str(e)}")

if __name__ == '__main__':
    # iterate all files in the static/imgs directory
    for file in os.listdir('static/imgs'):
        if file.endswith('.jpg'):
            convert_img_to_webp(os.path.join('static/imgs', file))
