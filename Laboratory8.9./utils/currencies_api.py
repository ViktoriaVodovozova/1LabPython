"""Модуль для работы с API курсов валют ЦБ РФ (в формате JSON)."""

import requests
from typing import List
from models.currency import Currency
import logging

# Настройка логгера для этого модуля
logger = logging.getLogger(__name__)

# URL API ЦБ РФ в формате JSON
CBR_JSON_API_URL = "https://www.cbr-xml-daily.ru/daily_json.js"


def get_currencies() -> List[Currency]:
    """
    Получает актуальные курсы всех валют с JSON API Центрального Банка РФ.

    Эта функция использует эндпоинт, который возвращает данные в удобном JSON формате,
    что упрощает парсинг по сравнению с XML-версией [[3], [5]].

    Returns:
        List[Currency]: Список объектов Currency с актуальными курсами.

    Raises:
        requests.exceptions.RequestException: При ошибке HTTP-запроса к API.
        KeyError, ValueError: При некорректной структуре ответа от API.
    """
    try:
        logger.info(f"Запрос курсов валют к API: {CBR_JSON_API_URL}")
        response = requests.get(CBR_JSON_API_URL, timeout=10)
        response.raise_for_status()  # Проверка на HTTP ошибки (4xx, 5xx)

        # API возвращает JSON, парсинг встроенный в requests
        data = response.json()
        currencies = []

        # Проверяем, что в ответе есть ключ 'Valute'
        if "Valute" not in data:
            raise ValueError("Ответ API не содержит ожидаемого ключа 'Valute'")

        # Проходим по всем валютам в ответе
        for currency_code, currency_info in data["Valute"].items():
            try:
                # Извлекаем необходимые поля из JSON-ответа
                num_code = str(currency_info["NumCode"])
                char_code = currency_info["CharCode"]
                name = currency_info["Name"]
                value = float(currency_info["Value"])
                nominal = int(currency_info["Nominal"])

                # Создаем объект модели Currency
                currency = Currency(
                    num_code=num_code,
                    char_code=char_code,
                    name=name,
                    value=value,
                    nominal=nominal
                )
                currencies.append(currency)

            except (KeyError, ValueError, TypeError) as e:
                # Логгируем ошибку для конкретной валюты, но не прерываем весь процесс
                logger.warning(f"Не удалось обработать валюту {currency_code}: {e}")
                continue

        logger.info(f"Успешно получено и обработано {len(currencies)} валют.")
        return currencies

    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка сети при запросе к API ЦБ РФ: {e}")
        # Пробрасываем исключение дальше, чтобы его мог обработать вызывающий код (сервер)
        raise
    except (KeyError, ValueError) as e:
        logger.error(f"Ошибка в структуре данных от API: {e}")
        raise