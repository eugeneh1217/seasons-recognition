from PIL import Image
import data


class InputData:
    def __init__(self, data):
        self.data = data

    def resize(self, resolution):
        for category in self.data:
            for key in category.keys():
                category[key].resize(resolution)


lst_of_images = InputData(data.data)

lst_of_images.resize((400, 400))

print(lst_of_images.data[0]["cloudy1"].size)


