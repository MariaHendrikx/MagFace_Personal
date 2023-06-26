from PIL import Image
import os

# Set paths for input PNG images and output JPG images
png_folder = "toy_imgs"
jpg_folder = "toy_imgs"

# Create the output JPG folder if it doesn't exist
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# List all PNG files in the input folder
png_files = [file for file in os.listdir(png_folder) if file.endswith(".jpg") or file.endswith(".png")]
print(png_files)

# Iterate over the PNG files and convert them to JPG
for i, png_file in enumerate(png_files):
    # Open the PNG image
    png_path = os.path.join(png_folder, png_file)
    image = Image.open(png_path)

    # Convert the image to JPG format
    jpg_file = f"{png_file[:-4]}.jpg"  # Output JPG file name
    jpg_path = os.path.join(jpg_folder, jpg_file)
    image.save(jpg_path, "JPEG")

    # Resize the JPG image to 112x112
    resized_image = image.resize((112, 112))
    resized_jpg_path = os.path.join(jpg_folder, f"{jpg_file}")
    resized_image.save(resized_jpg_path, "JPEG")

    # Close the images
    image.close()
    resized_image.close()

    # Optionally, you can delete the original PNG file after conversion
    # os.remove(png_path)