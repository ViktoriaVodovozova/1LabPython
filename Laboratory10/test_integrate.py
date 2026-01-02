import unittest
import math
from integrate import integrate

class TestIntegrate(unittest.TestCase):

    def test_integral_sin_0_to_pi(self):
        result = integrate(math.sin, 0, math.pi, n_iter=200_000)
        self.assertAlmostEqual(result, 2.0, delta=0.005)


    def test_integral_cos_0_to_pi_over_2(self):
        result = integrate(math.cos, 0, math.pi / 2, n_iter=200_000)
        self.assertAlmostEqual(result, 1.0, delta=0.005)

    def test_integral_x_squared_0_to_1(self):
        result = integrate(lambda x: x ** 2, 0, 1, n_iter=200_000)
        self.assertAlmostEqual(result, 1 / 3, delta=0.0005)

    def test_zero_interval(self):
        result = integrate(math.exp, 3.0, 3.0, n_iter=1000)
        self.assertEqual(result, 0.0)

    def test_odd_function_symmetric_interval(self):
        result = integrate(lambda x: x, -1, 1, n_iter=200_000)
        self.assertAlmostEqual(result, 0.0, delta=1e-4)

    def test_invalid_a_greater_b(self):
        with self.assertRaises(ValueError):
            integrate(math.sin, 2, 1, n_iter=1000)

    def test_invalid_n_iter_negative(self):
        with self.assertRaises(ValueError):
            integrate(math.sin, 0, 1, n_iter=-100)

if __name__ == "__main__":
    unittest.main(verbosity=2)