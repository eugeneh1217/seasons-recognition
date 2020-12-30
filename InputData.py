from PIL import Image
import data


class InputData:
    def __init__(self, data):
        self.data = data

    def resize(self, resolution):
        for category in self.data:
            for key in category.keys():
                category[key] = category[key].resize(resolution)
