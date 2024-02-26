from PIL import Image
import os

def convert_to_webp(directory, quality=100):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            file_path = os.path.join(directory, filename)
            image = Image.open(file_path)

            # Ensure the image is in 'RGBA' mode for transparency
            if image.mode != 'RGBA':
                image = image.convert('RGBA')

            # Define the output path for the WebP image
            output_path = os.path.splitext(file_path)[0] + '.webp'

            # Convert and save the image as WebP
            image.save(output_path, 'WEBP', quality=quality)

directory = '.'  # Current directory
convert_to_webp(directory)