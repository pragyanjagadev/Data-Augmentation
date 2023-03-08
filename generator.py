import os.path
import json
# import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from os import getcwd
from os import listdir
from os.path import isfile, join
import math

from scipy import ndimage
from skimage.transform import resize

# from skimage.transform import resize
import random
import glob


# from PIL import Image


# In this exercise task you will implement an image generator. Generator objects in python are defined as having a next function.
# This next function returns the next generated object. In our case it returns the input of a neural network each time it gets called.
# This input consists of a batch of images and its corresponding labels.
class ImageGenerator:
    def __init__(self, file_path, label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
        # Define all members of your generator class object as global members here.
        # These need to include:
        # the batch size
        # the image size
        # flags for different augmentations and whether the data should be shuffled for each epoch
        # Also depending on the size of your data-set you can consider loading all images into memory here already.
        # The labels are stored in json format and can be directly loaded as dictionary.
        # Note that the file names correspond to the dicts of the label dictionary.

        self.labels = None
        self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog',
                           7: 'horse', 8: 'ship', 9: 'truck'}
        # TODO: implement constructor

        self.file_path = file_path
        self.label_path = label_path
        self.batch_size = batch_size
        self.batch_idx = 0
        self.image_size = image_size
        self.json_file = open(self.label_path)
        self.json_labels = json.load(self.json_file)
        self.images_data = [f for f in listdir(self.file_path) if isfile(join(self.file_path, f))]
        self.no_iteration = math.ceil(len(self.images_data) / self.batch_size)
        self.mirroring = mirroring
        self.rotation = rotation
        self.shuffle = shuffle
        self.start = 0
        self.end = self.batch_size
        self.batch_idx = 0
        self.curr_epoch = 0
        self.npy_images = glob.glob(os.path.join('exercise_data', '*.npy'))
        self.call_next = 0

    def next(self):

        if self.shuffle:
            np.random.shuffle(self.npy_images)

        self.call_next = self.call_next + 1

        images_list = []
        labels = []

        for i in range(self.start, self.end):
            if i < len(self.npy_images):
                img, label = self.load(i)
                images_list.append(img)
                images = np.array(images_list)
                labels.append(label)

        if len(images_list) != self.batch_size:
            i = 0
            while len(images_list) != self.batch_size:
                img, label = self.load(i)
                images_list.append(img)
                images = np.array(images_list)
                labels.append(label)
                i = i + 1

        self.start = self.end
        self.batch_idx = self.batch_idx + 1
        self.end = self.start + self.batch_size
        if self.call_next > self.no_iteration:
            self.curr_epoch = self.curr_epoch + 1
        if self.shuffle:
            np.random.shuffle(images)
            np.random.shuffle(labels)
        return images, labels

    def load(self, i):

        img_path = self.npy_images[i]
        label_key = self.npy_images[i].split('/')[1].split('.')[0]
        label = self.json_labels[label_key]
        img = np.load(img_path)
        img = resize(img, self.image_size)
        img = self.augment(img)
        return img, label

    def augment(self, img):

        # this function takes a single image as an input and performs a random transformation
        # (mirroring and/or rotation) on it and outputs the transformed image
        # TODO: implement augmentation function
        mirr = random.choice([False, True])
        angle = random.choice([0, 90, 180, 270])
        # rotating img
        if self.mirroring:
            if mirr:
                img = np.fliplr(img)
        # mirroring img
        if self.rotation:
            if angle == 90:
                img = np.rot90(img, 1)
            elif angle == 180:
                img = np.rot90(img, 2)
            elif angle == 270:
                img = np.rot90(img, 3)
        return img

    def current_epoch(self):
        # return the current epoch number
        return self.curr_epoch

    def class_name(self, int_label):
        # This function returns the class name for a specific input
        # TODO: implement class name function
        return self.class_dict[self.labels[int_label]]

    def show(self):
        # In order to verify that the generator creates batches as required, this functions calls next to get a
        # batch of images and labels and visualizes it.
        # TODO: implement show method
        for i in range(0, self.no_iteration):
            images, labels = self.next()
            self.labels = labels
            idx = 0
            fig = plt.figure(figsize=(8, 8))
            columns = 3
            rows = math.ceil(self.batch_size / columns)

            for i in range(1, int(self.batch_size + 1)):
                label = self.class_name(idx)
                fig.add_subplot(rows, columns, i)
                plt.title(label)
                plt.imshow(images[idx])
                plt.axis('off')
                idx = idx + 1

            plt.show()
