import os
from PIL import Image

def center_image_with_alpha(image_path):
    # Load the image and convert it to RGBA mode
    image = Image.open(image_path).convert("RGBA")

    # Get the dimensions of the image
    width, height = image.size

    # Set the initial alpha area boundaries
    left, upper, right, lower = width, height, 0, 0

    # Iterate over the image to find the boundaries of the alpha area
    alpha_data = image.getdata(3)  # Get the alpha channel data
    for y in range(height):
        for x in range(width):
            if alpha_data[y * width + x] != 0:  # Check if the pixel is visible (non-transparent)
                left = min(left, x)
                upper = min(upper, y)
                right = max(right, x)
                lower = max(lower, y)

    # Calculate the new dimensions of the image
    new_width = right - left + 1
    new_height = lower - upper + 1

    # Crop the alpha area
    cropped_image = image.crop((left, upper, right + 1, lower + 1))

    # Create a new image with the determined dimensions
    centered_image = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))

    # Paste the cropped alpha area onto the new image at the center
    centered_image.paste(cropped_image, ((new_width - cropped_image.width) // 2, (new_height - cropped_image.height) // 2))

    # Save the centered image to a file
    centered_image.save(image_path, format='PNG')

# Loop through all images in image_dir directory
image_dir = "npc"
for filename in os.listdir(image_dir):
    if filename.endswith(".png"):
        image_path = os.path.join(image_dir, filename)
        center_image_with_alpha(image_path)