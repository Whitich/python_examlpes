import math
import unittest

from python_uygulamasi import euclidean_distance


class TestEuclideanDistance(unittest.TestCase):
    def test_3_4_5_triangle(self):
        self.assertEqual(euclidean_distance((0, 0), (3, 4)), 5.0)

    def test_same_points_zero_distance(self):
        self.assertEqual(euclidean_distance((7.5, -2.5), (7.5, -2.5)), 0.0)

    def test_negative_coordinates(self):
        self.assertEqual(euclidean_distance((-1, -2), (-4, -6)), 5.0)

    def test_large_coordinates_no_overflow(self):
        dist = euclidean_distance((0.0, 0.0), (1e200, 0.0))
        self.assertTrue(math.isfinite(dist))
        self.assertTrue(math.isclose(dist, 1e200, rel_tol=1e-15, abs_tol=0.0))

    def test_small_coordinates_no_underflow(self):
        dist = euclidean_distance((0.0, 0.0), (1e-200, 0.0))
        self.assertNotEqual(dist, 0.0)
        self.assertTrue(math.isclose(dist, 1e-200, rel_tol=1e-15, abs_tol=0.0))


if __name__ == "__main__":
    unittest.main()
