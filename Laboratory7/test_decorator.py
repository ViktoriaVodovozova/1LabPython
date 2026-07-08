import unittest
import io
import logging
from decorator import logger
from currency import get_currencies


class TestDecoratorLogging(unittest.TestCase):

    def setUp(self):
        # создается поток StringIO
        self.stream = io.StringIO()

        @logger(handle=self.stream)
        def wrapped_get_currencies(currency_codes, url=None):
            if url:
                return get_currencies(currency_codes, url)
            return get_currencies(currency_codes)

        self.wrapped = wrapped_get_currencies

    def test_logging_success(self):
        """Проверка логирования успешного вызова через StringIO"""
        result = self.wrapped(['USD'])
        logs = self.stream.getvalue()

        self.assertIn("INFO: Вызов wrapped_get_currencies(['USD'])", logs)
        self.assertIn("INFO: wrapped_get_currencies вернула", logs)
        self.assertIn("USD", str(result))
        self.assertIsInstance(result['USD'], float)

    def test_logging_connection_error(self):
        """Проверка логирования ConnectionError через декоратор"""
        with self.assertRaises(ConnectionError):
            self.wrapped(['USD'], url="https://invalid-url")

        logs = self.stream.getvalue()
        self.assertIn("ERROR", logs)
        self.assertIn("ConnectionError", logs)
        self.assertIn("API недоступен", logs)

    def test_logging_key_error(self):
        """Проверка логирования KeyError через декоратор"""
        with self.assertRaises(KeyError):
            self.wrapped(['XYZ'])  # Несуществующая валюта

        logs = self.stream.getvalue()
        self.assertIn("ERROR", logs)
        self.assertIn("KeyError", logs)
        self.assertIn("XYZ", logs)

    def test_logging_with_logger_object(self):
        """Проверка логирования через logging.Logger"""
        log_stream = io.StringIO()
        test_logger = logging.getLogger("test_logger")
        test_logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(log_stream)
        formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
        handler.setFormatter(formatter)
        test_logger.addHandler(handler)

        @logger(handle=test_logger)
        def test_func():
            return "OK"

        result = test_func()
        log_content = log_stream.getvalue()
        self.assertEqual(result, "OK")
        self.assertIn("INFO:test_logger:INFO: Вызов test_func()", log_content)
        self.assertIn("INFO:test_logger:INFO: test_func вернула 'OK'", log_content)


if __name__ == "__main__":
    unittest.main(verbosity=2)