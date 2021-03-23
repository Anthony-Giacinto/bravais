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
        angle: (float) The angle between the two primitive vectors; can't be 0 or 180 degrees (default is 120.0).
        degrees: (bool) If True, the angles are in degrees and if False, the angles are in radians (default is True).
        centered: (bool) True if the lattice is a centered rectangular (default is False).
        numpoints: (int) The number of desired points to plot and must be a square number larger than 4;
        will be the number of 'non-centered' points if centered rectangular lattice (default is 16).
        plot: (bool) If True, will plot the lattice (default is True).
        a_vec: (numpy array) The first primitive vector.
        b_vec: (numpy array) The second primitive vector.
        lattice: (str) The name of the type of Bravais lattice (depends on a, b, angle, and centered).
        unit_cell_area: (float) The area of the unit cell.

    Functions:
        plot: Creates a 2D scatter plot.
    """

    def __init__(self, a=1.0, b=1.0, angle=120.0, degrees=True, centered=False, numpoints=16, plot=True):
        """
        :param a: (float) The magnitude of the first primitive vector (default is 1.0).
        :param b: (float) The magnitude of the second primitive vector (default is 1.0).
        :param angle: (float) The angle between the two primitive vectors; can't be 0 or 180 degrees (default is 120.0).
        :param degrees: (bool) If True, the angles are in degrees and if False, the angles are in radians
        (default is True).
        :param centered: (bool) True if the lattice is a centered rectangular (default is False).
        :param numpoints: (int) The number of desired points to plot and must be a square number larger than 4;
        will be the number of 'non-centered' points if centered rectangular lattice (default is 16).
        :param plot: (bool) If True, will plot the lattice (default is True).
        """

        self.a = np.abs(a)
        self.b = np.abs(b)
        self.degrees = degrees
        self.centered = centered
        self._numpoints = numpoints
        self._angle = angle
        if plot:
            self.plot()

    @property
    def angle(self):
        if self.degrees:
            angle = math.radians(self._angle)
        else:
            angle = self._angle
        if angle == 0.0 or angle == math.pi:
            raise Exception("The angle must not be 0 or 180 degrees.")
        return angle

    @property
    def a_vec(self):
        return np.array([self.a, 0])

    @property
    def b_vec(self):
        return np.array([self.b*math.cos(self.angle), self.b*math.sin(self.angle)])

    @property
    def lattice(self):
        if (self.a != self.b) and (self.angle != math.pi/2) and (not self.centered):
            return "Oblique"
        elif (self.a != self.b) and (self.angle == math.pi/2) and self.centered:
            return "Centered Rectangular"
        elif (self.a != self.b) and (self.angle == math.pi/2) and (not self.centered):
            return "Rectangular"
        elif (self.a == self.b) and (self.angle == 2*math.pi/3 or self.angle == math.pi/3) and (not self.centered):
            return "Hexagonal"
        elif (self.a == self.b) and (self.angle == math.pi/2) and (not self.centered):
            return "Square"
        else:
            raise Exception("Invalid combination of a, b, angle, and/or centered.")

    @property
    def unit_cell_area(self):
        return self.a*self.b*math.sin(self.angle)

    @property
    def numpoints(self):
        val = round(self._numpoints**0.5, 0)**2
        if val == self._numpoints and val >= 9:
            return self._numpoints
        else:
            raise Exception("numpoints must be a square number greater than or equal to 9.")

    def __find_points(self):
        """ Finds all the x and y coordinates of the lattice.

        :return: (list(list)) x, y
        """

        def f(start, stop, x_list, y_list):
            for j in np.arange(start, stop):
                for i in np.arange(start, stop):
                    vec = i*self.a_vec + j*self.b_vec
                    x_list.append(vec[0])
                    y_list.append(vec[1])
            return x_list, y_list

        p = int(self.numpoints**0.5)
        x, y = f(0, p, [], [])
        if self.centered:
            x, y = f(0.5, p - 1, x, y)
        return x, y

    def __unit_cell(self, x, y):
        """ Finds the x and y coordinates for the unit cell.

        :param x: (list) The x coordinates of the lattice points.
        :param y: (list) The y coordinates of the lattice points.
        :return: (list(list()) x, y
        """

        root = int(self.numpoints**0.5)
        return (x[0], x[1], x[1+root], x[root], x[0]), (y[0], y[1], y[1+root], y[root], y[0])

    def plot(self):
        """ Creates a 2D scatter plot. """

        x, y = self.__find_points()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        if self.degrees:
            angle = str(self._angle)
        else:
            angle = str(math.degrees(self.angle))
        title = "Bravais Lattice: " + self.lattice
        variables = "\n|a| = " + str(self.a) + ", |b| = " + str(self.b) + ", \u03b8  =  " + angle + "\u00b0"
        scaling = "\n(Axes may be scaled differently)"
        ax.set_title(title + variables + scaling)
        ax.scatter(x, y, label="Lattice Points")
        ax.plot(*self.__unit_cell(x, y), color="darkorange", label="Unit Cell")
        plt.legend(loc="best").set_draggable(True)
        plt.show()
