from PIL import Image
import os
import subprocess

def add_padding_to_square(image_path):
    original_image = Image.open(image_path)
    if original_image.mode != 'RGBA':
        original_image = original_image.convert('RGBA')

    original_size = original_image.size  # (width, height)
    max_dimension = max(original_size)
    # Calculate padding to add to make the image square
    delta_w = max_dimension - original_size[0]
    delta_h = max_dimension - original_size[1]
    padding = (delta_w // 2, delta_h // 2, delta_w - (delta_w // 2), delta_h - (delta_h // 2))
    new_image = Image.new('RGBA', (max_dimension, max_dimension), (255, 255, 255, 0))
    new_image.paste(original_image, (padding[0], padding[1]))
    return new_image

def run_pngquant(image_path):
    # Ensure pngquant is available in the system path
    command = ['pngquant', '--force', '--ext', '.png', image_path]
    subprocess.run(command, check=True)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".png"):
                file_path = os.path.join(root, filename)
                # Add padding to make the image square
                new_image = add_padding_to_square(file_path)
                # Save the padded image over the original file
                new_image.save(file_path, format='PNG')
                # Optimize the image with pngquant
                run_pngquant(file_path)

process_directory('.')  # Start from the current directory
