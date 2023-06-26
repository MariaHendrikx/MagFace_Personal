import os
import shutil

destination_folder = './'
source_folder = 'd04201'
reference_folder = source_folder + '/reference'

file_path =  'img.list'


# Iterate over subfolders in the source folder
folder_paths = []
for filename in os.listdir(source_folder):
    if(filename == 'reference'):
        continue
    folder_path =  "OneImage" + "/" + source_folder + "/" +  filename
    folder_paths.append(folder_path)


with open(file_path, 'w') as file:
    for folder_path in folder_paths:
        file.write(folder_path + '\n')

    