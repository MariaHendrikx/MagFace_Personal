import os
import shutil

prefix = '40_'
destination_folder = '40'

# Iterate over subfolders in the source folder
source_folder = 'FastImages'
for foldername in os.listdir(source_folder):
    folder_path = os.path.join(source_folder, foldername)

    # loop over the images
    for filename in os.listdir(folder_path):
        if filename.startswith(prefix) and os.path.isfile(os.path.join(folder_path, filename)):
            # Copy the file to the destination folder
            shutil.copyfile(os.path.join(folder_path, filename), os.path.join(destination_folder, filename))
            print(f"Moved {filename} to {destination_folder}")

def move_images(source_folder, destination_folder, prefix):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)