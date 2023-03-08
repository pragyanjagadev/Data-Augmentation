from symbol import comparison

import numpy as np
import unittest
from matplotlib import pyplot as plt
import os.path
from os import getcwd
from pattern import Checker
from pattern import Circle
from pattern import Spectrum
from generator import ImageGenerator


def get_corner_points(image):
    # Utility function to check whether the augmentations where performed
    # expects batch of image - expected shape is [s,x,y,c]
    return image[:, [0, -1], :, :][:, :, [0, -1], :]

if __name__ == '__main__':
    # newObj = Checker(200, 50)
    # arr = newObj.draw()
    # if len(arr) > 0:
    # newObj.show()

    # circleObj = Circle(500, 100, [250, 120])
    # circleObj.draw()
    # circleObj.show()

     #obj_spectrum = Spectrum(256)
     #obj_spectrum.draw()
     #obj_spectrum.show()

    cur_path = getcwd()
    # file_path = os.path.join(cur_path, "data/exercise_data")
    # label_path = os.path.join(cur_path, "data/Labels.json")
    file_path = os.path.join("exercise_data")
    label_path = os.path.join("Labels.json")

    # label_path = 'Labels.json'
    # file_path = 'exercise_data/'
    # obj_image = ImageGenerator(file_path, label_path, 10, [5, 5, 5], True, True, True)
    obj_image = ImageGenerator(file_path, label_path, 10, [32, 32, 3], rotation=True, mirroring=True, shuffle=True)
    obj_image.show()

    # gen = ImageGenerator(file_path, label_path, 50, [32, 32, 3], rotation=False, mirroring=False,
    #                      shuffle=True)
    # b1_epoch0 = gen.next()[1]
    # gen.next()
    # b1_epoch1 = gen.next()[1]
    # print(b1_epoch0)
    # print(b1_epoch1)
    # print(np.sort(b1_epoch0, axis=None) == np.sort(b1_epoch1, axis=None))
    # print(b1_epoch0)
    # print(b1_epoch1)
    # print(np.all(np.sort(b1_epoch0, axis=None) == np.sort(b1_epoch1, axis=None)))
    # self.assertFalse(np.all(np.sort(b1_epoch0, axis=None) == np.sort(b1_epoch1, axis=None)))


