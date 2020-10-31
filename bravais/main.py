"""
Contains the Bravais2D class that can plot a 2D Bravais lattice.

Classes:
    Bravais2D: Plots a 2D Bravais lattice.
"""


import math
import numpy as np
import matplotlib.pyplot as plt


class Bravais2D:
    """ Plots a 2D Bravais lattice.

    Instance Attributes:
        a: (float) The magnitude of the first primitive vector (default is 1.0).
        b: (float) The magnitude of the second primitive vector (default is 1.0).
        angle: (float) The angle between the two primitive vectors; can't be 0 or 180 degrees (default is 90.0).
        degrees: (bool) If true, angle is in degrees and if False, angle is in radians (default is True).
        centered: (bool) True if the lattice is a centered rectangular (default is False).
        numpoints: (int) The number of desired points to plot and must be a square number larger than 4;
        will be the number of 'non-centered' points if centered rectangular lattice (default is 25).
        lattice: (str) The name of the type of Bravais lattice (depends on a, b, angle, and centered).

    Functions:
        plot: Creates a 2D scatter plot.
    """

    def __init__(self, a=1.0, b=1.0, angle=90.0, degrees=True, centered=False, numpoints=25):
        """
        :param a: (float) The magnitude of the first primitive vector (default is 1.0).
        :param b: (float) The magnitude of the second primitive vector (default is 1.0).
        :param angle: (float) The angle between the two primitive vectors; can't be 0 or 180 degrees (default is 90.0).
        :param degrees: (bool) If true, angle is in degrees and if False, angle is in radians (default is True).
        :param centered: (bool) True if the lattice is a centered rectangular (default is False).
        :param numpoints: (int) The number of desired points to plot and must be a square number larger than 4;
        will be the number of 'non-centered' points if centered rectangular lattice (default is 25).
        """

        self.a = np.abs(a)
        self.b = np.abs(b)
        self.degrees = degrees
        self.centered = centered
        self._numpoints = numpoints
        self._angle = angle
        self.plot()

    @property
    def angle(self):
        if self.degrees:
            angle = math.radians(self._angle)
            if angle == 0 or angle == math.pi:
                raise Exception('The angle must not be 0 or 180 degrees.')
            else:
                return angle
        else:
            if self._angle == 0 or self._angle == math.pi:
                raise Exception('The angle must not be 0 or 180 degrees.')
            else:
                return self._angle

    @property
    def _a_vec(self):
        return np.array([self.a, 0])

    @property
    def _b_vec(self):
        return np.array([self.a*self.b*math.cos(self.angle), self.b*math.sin(self.angle)])

    @property
    def lattice(self):
        if (self.a != self.b) and (self.angle != math.pi/2):
            return 'Oblique'
        elif (self.a != self.b) and (self.angle == math.pi/2) and self.centered:
            return 'Centered Rectangular'
        elif (self.a != self.b) and (self.angle == math.pi/2) and (not self.centered):
            return 'Rectangular'
        elif (self.a == self.b) and (self.angle == 2*math.pi/3 or self.angle == math.pi/3):
            return 'Hexagonal'
        elif (self.a == self.b) and (self.angle == math.pi/2):
            return 'Square'
        else:
            raise Exception('Invalid combination of a, b, and angle.')

    @property
    def numpoints(self):
        val = round(self._numpoints**0.5, 0)**2
        if val == self._numpoints and val > 4:
            return self._numpoints
        else:
            raise Exception('numpoints must be a square number larger than 4.')

    def __append_points(self, start, stop, x, y):
        """ Appends x and y coordinates of the lattice to two lists.

        :param start: (float) The start of np.arange.
        :param stop: (float) The end of np.arange.
        :param x: (list) The list of x values.
        :param y: (list) The list of y values.
        :return: (list(list)) x, y
        """

        for j in np.arange(start, stop):
            for i in np.arange(start, stop):
                vec = i*self._a_vec + j*self._b_vec
                x.append(vec[0])
                y.append(vec[1])
        return x, y

    def __find_points(self):
        """ Finds all the x and y coordinates of the lattice.

        :return: (list(list)) x, y
        """

        p = int(self.numpoints**0.5)
        points = self.__append_points(0, p, [], [])
        if self.centered:
            points = self.__append_points(0.5, p - 1, points[0], points[1])
        return points[0], points[1]

    def plot(self):
        """ Creates a 2D scatter plot. """

        p = self.__find_points()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(p[0], p[1])
        ax.set_title('Bravais Lattice:\n' + self.lattice)
        plt.show()
