import unittest
from unittest.mock import MagicMock
from controllers.currencycontroller import CurrencyController


class TestCurrencyController(unittest.TestCase):
    def setUp(self):
        # Создаем мок для DatabaseController
        self.mock_db = MagicMock()
        self.controller = CurrencyController(self.mock_db)

    def test_list_currencies(self):
        """Тест получения списка валют"""
        # Настраиваем мок
        mock_currencies = [
            {"id": 1, "char_code": "USD", "value": 77.5},
            {"id": 2, "char_code": "EUR", "value": 90.34}
        ]
        self.mock_db.get_all_currencies.return_value = mock_currencies

        # Вызываем метод контроллера
        result = self.controller.list_currencies()

        # Проверяем результат
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['char_code'], "USD")
        self.assertEqual(result[1]['value'], 90.34)

        # Проверяем, что метод базы данных был вызван
        self.mock_db.get_all_currencies.assert_called_once()

    def test_update_currency_value(self):
        """Тест обновления курса валюты"""
        # Настраиваем мок для успешного обновления
        self.mock_db.update_currency_value.return_value = True

        # Вызываем метод контроллера
        result = self.controller.update_currency_value(1, 78.0)

        # Проверяем результат
        self.assertTrue(result)

        # Проверяем вызов метода базы данных с правильными параметрами
        self.mock_db.update_currency_value.assert_called_once_with(1, 78.0)

        # Тестируем ошибку при отрицательном значении
        with self.assertRaises(ValueError):
            self.controller.update_currency_value(1, -10.0)

    def test_delete_currency(self):
        """Тест удаления валюты"""
        # Настраиваем мок для успешного удаления
        self.mock_db.delete_currency.return_value = True

        # Вызываем метод контроллера
        result = self.controller.delete_currency(1)

        # Проверяем результат
        self.assertTrue(result)

        # Проверяем вызов метода базы данных
        self.mock_db.delete_currency.assert_called_once_with(1)


if __name__ == "__main__":
    unittest.main(verbosity=2)