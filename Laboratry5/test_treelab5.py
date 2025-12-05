import unittest

from tree import gen_bin_tree


class TestMath(unittest.TestCase):
    def test_another_tree(self):
        self.assertEqual(gen_bin_tree(3, 7, lambda x: x * 2, lambda y: y + 1),
                         {'7': [{'14': [{'28': []}, {'15': []}]}, {'8': [{'16': []}, {'9': []}]}]})

    def test_float_main_root(self):
        self.assertEqual(gen_bin_tree(3, 7.7, lambda x: x + 1, lambda y: y + 2),
                         {'7.7': [{'8.7': [{'9.7': []}, {'10.7': []}]},
                                  {'9.7': [{'10.7': []}, {'11.7': []}]}]})

    def test_float_both_roots(self):
        self.assertEqual(gen_bin_tree(3, 7, lambda x: x + 2.1, lambda y: y + 1.2),
                         {'7': [{'9.1': [{'11.2': []}, {'10.299999999999999': []}]},
                                {'8.2': [{'10.299999999999999': []}, {'9.399999999999999': []}]}]})

    def test_height_zero(self):
        self.assertEqual(gen_bin_tree(0, 7, lambda x: x + 1, lambda y: y + 2),
                         {'7': []})

    def test_negativ_op(self):
        self.assertEqual(gen_bin_tree(3, 100, lambda x: x - 1, lambda y: y // 2),
                         {'100': [{'99': [{'98': []}, {'49': []}]},
                                  {'50': [{'49': []}, {'25': []}]}]})

    def test_float_height(self):
        with self.assertRaises(TypeError):
            gen_bin_tree(3.7, 7, lambda x: x + 1, lambda y: y + 2)

    def test_str_height(self):
        with self.assertRaises(TypeError):
            gen_bin_tree("3", 7, lambda x: x + 1, lambda y: y + 2)

    def test_negative_height(self):
        with self.assertRaises(TypeError):
            gen_bin_tree(-1, 7, lambda x: x + 1, lambda y: y + 2)


if __name__ == "__main__":
    unittest.main()
