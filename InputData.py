from PIL import Image
import data


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
        """Normalize size of input images."""
        for category in self.raw:
            for key in category.keys():
                category[key] = category[key].resize(resolution)

    def split(self, ratio):
        """
        Split data into testing and training set.
        :param ratio: float between 0 and 1 that indicates what fraction of data will be used for training
        """
        