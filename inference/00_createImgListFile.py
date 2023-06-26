import os
import shutil

destination_folder = './'
source_folder = 'toy_imgs'

file_path =  source_folder+ 'img.list'


# Iterate over subfolders in the source folder
folder_paths = []
for filename in os.listdir(source_folder):
    folder_path = source_folder + "/" +  filename
    folder_paths.append(folder_path)



    