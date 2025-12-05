import unittest
from currency import get_currencies

class TestGetCurrencies(unittest.TestCase):

    def test_valid_currency(self):
        """Тест корректного запроса для USD и EUR"""
        result = get_currencies(['USD', 'EUR'])
        self.assertIn('USD', result)
        self.assertIn('EUR', result)
        self.assertIsInstance(result['USD'], float)
        self.assertGreater(result['USD'], 0)
        self.assertGreater(result['EUR'], 0)

    def test_nonexistent_currency(self):
        """Тест несуществующей валюты"""
        with self.assertRaises(KeyError) as cm:
            get_currencies(['XYZ'])
        self.assertIn("XYZ", str(cm.exception))
        self.assertIn("отсутствует в данных", str(cm.exception))

    def test_connection_error(self):
        """Тест ошибки подключения"""
        with self.assertRaises(ConnectionError):
            get_currencies(['USD'], url="https://invalid-url")

    def test_invalid_json(self):
        """Тест некорректного JSON"""
        with self.assertRaises(ValueError) as cm:
            get_currencies(['USD'], url="https://example.com")
        self.assertIn("Некорректный JSON", str(cm.exception))

if __name__ == "__main__":
    unittest.main(verbosity=2)