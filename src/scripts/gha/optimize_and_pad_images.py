import os
import sys
import argparse
import subprocess
from PIL import Image

def process_image(input_path):
    try:
        # Prepare the output filename
        output_path = os.path.splitext(input_path)[0] + '.png'
        temp_path = output_path + '.temp.png'

        # Convert to PNG using ImageMagick (lossless)
        subprocess.run(['convert', input_path, '-colorspace', 'RGB', 'PNG32:' + temp_path], check=True)

        # Open the converted image with Pillow
        with Image.open(temp_path) as img:
            # Get the bounding box of the non-zero regions in the image
            bbox = img.getbbox()
            
            if bbox:
                # Crop to the bounding box
                cropped = img.crop(bbox)
                
                # Calculate the size of the smallest square that fits the content
                size = max(cropped.width, cropped.height)
                
                # Create a new square image with transparent background
                square_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
                
                # Calculate position to paste the cropped image
                paste_pos = ((size - cropped.width) // 2, (size - cropped.height) // 2)
                
                # Paste the cropped image onto the square background
                square_img.paste(cropped, paste_pos)
            else:
                # If there's no content (fully transparent image), just use the original
                square_img = img.copy()

            # Save as PNG
            square_img.save(output_path, 'PNG')

        # Remove the temporary file
        os.remove(temp_path)

        # Optimize with optipng
        subprocess.run(['optipng', '-o2', '-quiet', output_path], check=True)

        # Remove the original file if it's different from the output
        if input_path != output_path:
            os.remove(input_path)

        print(f"Successfully processed: {input_path} -> {output_path}")
        return True

    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")
        return False

def main(args):
    if args.all:
        # Process all images in the directory
        for root, _, files in os.walk(args.directory):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                    process_image(os.path.join(root, file))
    elif args.files_from:
        # Read files from the specified file
        with open(args.files_from, 'r') as f:
            files = f.read().splitlines()
        for file_path in files:
            if os.path.exists(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                if not process_image(file_path):
                    return False
    else:
        print("No files specified and --all not used. Nothing to do.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process images to square PNG format.")
    parser.add_argument('--all', action='store_true', help='Process all images in the directory')
    parser.add_argument('--directory', default='images', help='Directory containing images to process')
    parser.add_argument('--files-from', help='File containing list of files to process')
    args = parser.parse_args()

    if main(args):
        sys.exit(0)
    else:
        sys.exit(1)