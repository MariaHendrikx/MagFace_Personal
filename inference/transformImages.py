from PIL import Image
import os

def createImgListFile(images_folder):
    img_list_path = os.path.join(images_folder, "img.list")
    with open(img_list_path, 'w') as file:
        pass  # Creating an empty file

def retouchImage(img_file, images_folder, new_name):
    # Open the PNG image
    png_path = os.path.join(images_folder, img_file)
    image = Image.open(png_path)

    # Convert the image to JPG format
    jpg_file = f"{new_name}.jpg"  # Output JPG file name
    jpg_path = os.path.join(images_folder, jpg_file)
    image.save(jpg_path, "JPEG")

    # Rename image
    new_jpg_path = os.path.join(images_folder, f"{new_name}.jpg")
    os.rename(jpg_path, new_jpg_path)

    # Resize the JPG image to 112x112
    resized_image = image.resize((112, 112))
    resized_image.save(new_jpg_path, "JPEG")

    # Append the resized image path to the existing file
    with open(os.path.join(images_folder, "img.list"), 'a') as file:
        file.write(new_jpg_path + '\n')

    # Delete the old image with the old name
    os.remove(os.path.join(images_folder, img_file))

    # Close the images
    image.close()
    resized_image.close()


# Set paths for input PNG images and output JPG images
images_folder = "OneImage/d04201"
# Create the output JPG folder if it doesn't exist
if not os.path.exists(images_folder):
    os.makedirs(images_folder)

# List all PNG/jpg files in the input folder
img_files = [file for file in os.listdir(images_folder) if file.endswith(".jpg") or file.endswith(".png")]

createImgListFile(images_folder)
# Iterate over the PNG files and convert them to JPG
for i, png_file in enumerate(img_files):
    print(png_file)
    retouchImage(png_file, images_folder, i)


