import unittest

from main import sum_two


class Testsum_two(unittest.TestCase):
    def test_correct_from_example(self):
        self.assertEqual(sum_two([2, 7, 11, 15], 9), [0, 1])

        self.assertEqual(sum_two([3, 2, 4], 6), [1, 2])

        self.assertEqual(sum_two([3, 3], 6), [0, 1])

    def test_correct_negative_num(self):
        self.assertEqual(sum_two([-4, -3, -2], -5), [1, 2])

    def test_correct_huge_num(self):
        self.assertEqual(sum_two([100000, 400000, 4, 210000], 400004), [1, 2])


    def test_empty(self):
        with self.assertRaises(TypeError):
            sum_two([], 56)

    def test_targ_zero(self):
        with self.assertRaises(TypeError):
            sum_two([1, 2, 3], 0)

    def test_integrity_target(self):
        with self.assertRaises(TypeError):
            sum_two([1, 3, 7], 12.56)

    def test_integrity(self):
        with self.assertRaises(TypeError):
            sum_two([1.23, 1.56, 90.7], 10)

    def test_str_in_num(self):
        with self.assertRaises(TypeError):
            sum_two([1, 3, "8"], 4)

    def test_str_in_target(self):
        with self.assertRaises(TypeError):
            sum_two([1, 3, 8], "4")

if __name__ == "__main__":
    unittest.main()
