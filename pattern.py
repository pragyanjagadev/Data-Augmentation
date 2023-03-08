from copy import deepcopy

import numpy as np
from matplotlib import pyplot as plt


class Checker:

    def __init__(self, resolution, tile_size):
        self.resolution = resolution
        self.tile_size = tile_size
        self.output = []

    def draw(self):
        # white_tile = np.zeroes
        # n = int(self.resolution / 2 * self.tile_size)
        # # print("Checkerboard pattern:")
        # print(n)
        # x = np.zeros((n, n), dtype=int)
        # # x = np.ones((25, 25), dtype=int)
        # x[1::2, ::2] = 1
        # x[::2, 1::2] = 1
        # self.output = x
        # if self.resolution % (2 * self.tile_size):
        #     print('Error: Resolution/2*TileSize must be an integer')
        #     return []
        black_tile = np.zeros((self.tile_size, self.tile_size))
        white_tile = np.ones((self.tile_size, self.tile_size))
        reps = int(self.resolution / (2 * self.tile_size))
        row_odd = np.tile(np.concatenate((black_tile, white_tile), axis=1), (1, reps))
        row_even = np.tile(np.concatenate((white_tile, black_tile), axis=1), (1, reps))
        self.output = np.tile(np.concatenate((row_odd, row_even), axis=0), (reps, 1))

        # a = np.concatenate((np.zeros(self.tile_size), np.ones(self.tile_size)))
        # b = np.pad(a, int((self.resolution ** 2) / 2 - self.tile_size), 'wrap')
        # c = b.reshape((self.resolution, self.resolution))
        # self.output = (c+c.T==1).astype(int)
        # self.output = (c+c.T).astype(int)
        # # print(a)
        # print(b)
        # # print(c)
        # print(c+c.T==0)
        # print("............................")
        # print(c.T)
        # self.output = self.output
        return deepcopy(self.output)

    def show(self):
        # print(self.output)
        fig, ax = plt.subplots()
        i = ax.imshow(self.output, cmap="gray")
        fig.colorbar(i)

        plt.show()


class Circle:

    def __init__(self, resolution, radius, coordinates):
        self.resolution = resolution
        self.radius = radius
        self.coordinates = coordinates
        self.output = []

    def draw(self):
        xx = np.linspace(0, self.resolution - 1, self.resolution)
        yy = np.linspace(0, self.resolution - 1, self.resolution)
        [X, Y] = np.meshgrid(xx, yy)
        zz = (X - self.coordinates[0]) ** 2 + (Y - self.coordinates[1]) ** 2 <= self.radius ** 2
        self.output = zz.astype(float)
        print(zz[100])
        return deepcopy(self.output)

    def show(self):
        plt.figure()
        plt.imshow(self.output, cmap="gray")
        plt.show()


class Spectrum():
    def __init__(self, resolution):
        self.resolution = resolution
        self.output = []

    def draw(self):
        # print("pragyan spectrum")

        op = np.zeros([self.resolution, self.resolution, 3])  # init the array
        print(op)
        # RGB
        op[:, :, 0] = np.linspace(0, 1, self.resolution)
        op[:, :, 1] = np.linspace(0, 1, self.resolution).reshape(self.resolution, 1)
        op[:, :, 2] = np.linspace(1, 0, self.resolution)
        # print(op)
        self.output = op
        return deepcopy(self.output)

    def show(self):
        plt.imshow(self.output)
        plt.show()


