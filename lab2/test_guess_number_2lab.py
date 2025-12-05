import unittest

from guess_number import guess_number


class TestMath(unittest.TestCase):
    def test_positive_seq(self):
        self.assertEqual(guess_number(5, [1, 2, 5, 8, 4], type="seq"), [5, 4])

    def test_positive_bin(self):
        self.assertEqual(guess_number(5, [1, 2, 5, 8, 4], type="bin"), [5, 2])

    def test_positive_bin_list(self):
        self.assertEqual(guess_number(5, [1, 18], type="bin_with_making_list"), [5, 4])

    def test_negative_target_seq(self):
        self.assertEqual(guess_number(-1, [-11, -2, -1, -5, -8, -4], type="seq"), [-1, 6])

    def test_negative_target_bin(self):
        self.assertEqual(guess_number(-1, [-11, -2, -1, -5, -8, -4], type="bin"), [-1, 3])

    def test_negative_target_bin_list(self):
        self.assertEqual(guess_number(-5, [-1, -18], type="bin_with_making_list"), [-5, 2])

    def test_target_none_seq(self):
        self.assertEqual(guess_number(0, [1, 2, 5, 8, 4], type="seq"), [None, 5])

    def test_target_none_bin(self):
        self.assertEqual(guess_number(0, [1, 2, 5, 8, 4], type="bin"), [None, 2])

    def test_target_none_bin_list(self):
        self.assertEqual(guess_number(0, [1, 9], type="bin_with_making_list"), [None, 3])

    def test_empty_list_seq(self):
        self.assertEqual(guess_number(5, [], type="seq"), [None, 0])

    def test_empty_list_bin(self):
        self.assertEqual(guess_number(5, [], type="bin"), [None, 0])

    def test_empty_list_bin_list(self):
        self.assertEqual(guess_number(5, [], type="bin_with_making_list"), None)

    def test_half_empty_list_bin_list(self):
        self.assertEqual(guess_number(5, [9], type="bin_with_making_list"), None)

    def test_targ_integrity(self):
        with self.assertRaises(TypeError):
            guess_number(8.2, [4, 7, 2], type="seq")

    def test_integrity(self):
        with self.assertRaises(TypeError):
            guess_number(8, [4.7, 7, 8.2], type="seq")

    def test_targ_str(self):
        with self.assertRaises(TypeError):
            guess_number("8", [4, 7, 2], type="seq")

    def test_str_in_list(self):
        with self.assertRaises(TypeError):
            guess_number(8, ["4", 7, 8], type="seq")


if __name__ == "__main__":
    unittest.main()
