import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'models'))

from models.user import User
from models.currency import Currency
from models.author import Author
from models.app import App


class TestModels(unittest.TestCase):

    def test_user(self):
        user = User("Тест")
        self.assertEqual(user.name, "Тест")
        self.assertGreater(user.id, 0)

        with self.assertRaises(ValueError):
            User("")

    def test_currency(self):
        currency = Currency("840", "USD", "Доллар", 77.5, 1)
        self.assertEqual(currency.char_code, "USD")
        self.assertEqual(currency.value, 77.5)

        with self.assertRaises(ValueError):
            Currency("840", "USD", "Доллар", -1, 1)

    def test_author_and_app(self):
        author = Author("Викаа", "P3121")
        app = App("TestApp", "1.0", author)
        self.assertEqual(app.author.name, "Викаа")


if __name__ == "__main__":
    unittest.main(verbosity=2)