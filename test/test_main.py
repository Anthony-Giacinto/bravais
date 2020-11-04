import unittest
import math
import bravais.main as main


class TestBravais2DAngle(unittest.TestCase):

    def test_angle_degrees(self):
        self.assertEqual(main.Bravais2D(angle=90, degrees=True, plot=False).angle, math.pi/2)

    def test_angle_radians(self):
        self.assertEqual(main.Bravais2D(angle=math.pi/2, degrees=False, plot=False).angle, math.pi/2)

    def test_angle_exception(self):
        self.assertRaises(Exception, main.Bravais2D.angle, angle=math.pi, degrees=False, plot=False)
        self.assertRaises(Exception, main.Bravais2D.angle, angle=0, degrees=False, plot=False)


class TestBravais2dAVec(unittest.TestCase):

    def test_a_vec(self):
        bravais = main.Bravais2D(a=2.0, plot=False)
        self.assertEqual(bravais.a_vec[0], bravais.a)
        self.assertEqual(bravais.a_vec[1], 0)


class TestBravais2dBVec(unittest.TestCase):

    def test_b_vec(self):
        bravais = main.Bravais2D(a=2.0, b=3.0, angle=90, plot=False)
        self.assertEqual(bravais.b_vec[0], bravais.a*bravais.b*math.cos(bravais.angle))
        self.assertEqual(bravais.b_vec[1], bravais.b*math.sin(bravais.angle))


class TestBravais2DLattice(unittest.TestCase):

    def test_lattice_oblique(self):
        self.assertEqual(main.Bravais2D(a=2.0, b=1.0, angle=45, plot=False).lattice, 'Oblique')

    def test_lattice_centered_rectangular(self):
        self.assertEqual(main.Bravais2D(a=2.0, b=1.0, angle=90, centered=True, plot=False).lattice,
                         'Centered Rectangular')

    def test_lattice_rectangular(self):
        self.assertEqual(main.Bravais2D(a=2.0, b=1.0, angle=90, centered=False, plot=False).lattice,
                         'Rectangular')

    def test_lattice_hexagonal(self):
        self.assertEqual(main.Bravais2D(a=3.0, b=3.0, angle=60, plot=False).lattice, 'Hexagonal')
        self.assertEqual(main.Bravais2D(a=3.0, b=3.0, angle=120, plot=False).lattice, 'Hexagonal')

    def test_lattice_square(self):
        self.assertEqual(main.Bravais2D(a=3.0, b=3.0, angle=90, plot=False).lattice, 'Square')

    def test_lattice_exception(self):
        self.assertRaises(Exception, main.Bravais2D.lattice, a=3.0, b=3.0, angle=45, plot=False)


class TestBravais2DNumpoints(unittest.TestCase):

    def test_numpoints_value(self):
        self.assertEqual(main.Bravais2D(numpoints=25, plot=False).numpoints, 25)

    def test_numpoints_exception(self):
        self.assertRaises(Exception, main.Bravais2D.numpoints, numpoints=10, plot=False)
        self.assertRaises(Exception, main.Bravais2D.numpoints, numpoints=4, plot=False)
        self.assertRaises(Exception, main.Bravais2D.numpoints, numpoints=3, plot=False)


if __name__ == '__main__':
    unittest.main()
