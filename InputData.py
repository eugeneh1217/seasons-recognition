from PIL import Image
import data
import random


class InputData:
    """
    A class to manage raw data, processed data, and data manipulation methods
    """

    def __init__(self, raw, train_x=[], train_y=[], test_x=[], test_y=[]):
        """
        Constructs attributes for InputData object.

        :param raw: list of dictionaries that holds images and image file names
        :param train_x: independant variable values for training
        :param train_y: dependant variable values for training
        :param test_x: independant variable values for testing
        :param test_y: dependant variable values for testing
        """
        self.raw = raw
        self.train_x = train_x
        self.train_y = train_y
        self.test_x = test_x
        self.test_y = test_y

    def resize(self, resolution):
        """
        Normalize size of input images.

        :param resultion: tuple of two ints that specify final size of images
        """
        for category in self.raw:
            for key in category.keys():
                category[key] = category[key].resize(resolution)

    def split(self, ratio):
        """
        Split data into testing and training set.
        :param ratio: float between 0 and 1 that indicates what fraction of data will be used for training
        """
        """1. combine the four dictionaries into one using update 
           2. use len to get the number of images, then multiply by the ratio to get the training number
           3. use random function to pick a random label from the dictionary and start creating a list for labels
           3. at the same time access the image corresponds to labels and create list for the images
           4. erase the list inside dictionary each time its picked out
           5. do the same again to the rest lists in the dictionary to randamize the testing set"""
        all_data = dict()
        for category in self.raw:
            all_data.update(category)
        training_size = int(ratio * len(all_data))
        for iteration in range(training_size):
            index = random.randrange(len(all_data))
            key = list(all_data.keys())[index]





        