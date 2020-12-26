import os
import re
from PIL import Image

data = []

# path of current directory as string
current_directory = os.getcwd()

# list of files within directory \data
data_files = os.listdir(current_directory + r'\data')

categories = []

# assuming that first instance of an alphabetical substring is the name of the category
for file in data_files:
    category = re.findall("^[A-Za-z]*", file)[0]
    if category in categories:
        data[categories.index(category)][file[:-4]] = Image.open(current_directory + r'\data\\' + file)
    else:
        data.append({file[:-4]: Image.open(current_directory + r'\data\\' + file)})
        categories.append(category)


