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

    def __find_array(self):
        r_array = []
        x_array = []
        y_array = []
        p = int(self.numpoints**0.5)
        for y in range(p):
            for x in range(p):
                r_array.append(x*self._a_vec + y*self._b_vec)
        if self.centered:
            inner_p = p - 1
            for y in np.arange(0.5, inner_p):
                for x in np.arange(0.5, inner_p):
                    r_array.append(x*self._a_vec + y*self._b_vec)
        for i in range(len(r_array)):
            r_array[i] = r_array[i].tolist()
        for item in r_array:
            x_array.append(item[0])
            y_array.append(item[1])
        return x_array, y_array

    def plot(self):
        """ Creates a 2D scatter plot. """

        arr = self.__find_array()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(arr[0], arr[1])
        ax.set_title('Bravais Lattice:\n' + self.lattice)
        plt.show()
