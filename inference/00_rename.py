import os
import shutil

destination_folder = './'
source_folder = 'toy_imgs'

# Iterate over subfolders in the source folder
folder_paths = []
i = 0
for filename in os.listdir(source_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(filename)
        os.rename(source_folder + "/" + filename, source_folder + "/" + str(i) + ".jpg")
        i += 1


    