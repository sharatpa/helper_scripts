import glob
import os
## Replace the file path with the folder.
folder_path = os.getcwd()
file_type = '\*.py'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)

print (max_file)