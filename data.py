import os
import platform
import re
from PIL import Image

# list of pillow images
data = []

# path of current directory as string
current_directory = os.getcwd()

# path of data directory
data_path = '\\data\\' if 'indows' in platform.system() else '/data/'

# list of files within directory \data
data_files = os.listdir(current_directory + data_path)

categories = []

# assuming that first instance of an alphabetical substring is the name of the category
for file in data_files:
    category = re.findall("^[A-Za-z]*", file)[0]
    if category in categories:
        data[categories.index(category)][file[:-4]] = Image.open(current_directory + data_path + file)
    else:
        data.append({file[:-4]: Image.open(current_directory + data_path + file)})
        categories.append(category)


