import requests


def get_currencies(currency_codes: list, url="https://www.cbr-xml-daily.ru/daily_json.js") -> dict:
    """
    Получает курсы валют с API ЦБ РФ.

    Args:
        currency_codes (list): Список кодов валют (например, ['USD', 'EUR'])
        url (str): URL API (по умолчанию — реальный API ЦБ)

    Returns:
        dict: Словарь с курсами {код: значение}

    Raises:
        ConnectionError: Если API недоступен
        ValueError: Если JSON некорректный
        KeyError: Если отсутствует ключ "Valute" или валюта
        TypeError: Если курс имеет неверный тип
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            raise ValueError("Некорректный JSON в ответе API")

        # Проверка наличия корневого ключа
        if "Valute" not in data:
            raise KeyError("Отсутствует ключ 'Valute' в ответе API")

        result = {}
        for code in currency_codes:
            # Проверка наличия валюты
            if code not in data["Valute"]:
                raise KeyError(f"Валюта '{code}' отсутствует в данных")

            # Получение значения курса
            currency_data = data["Valute"][code]
            if "Value" not in currency_data:
                raise KeyError(f"Для валюты '{code}' отсутствует ключ 'Value'")

            value = currency_data["Value"]

            # Проверка типа курса
            if not isinstance(value, (int, float)):
                raise TypeError(f"Курс валюты '{code}' имеет неверный тип: {type(value)}")

            result[code] = value

        return result

    except requests.exceptions.ConnectionError:
        raise ConnectionError("API недоступен")
    except requests.exceptions.Timeout:
        raise ConnectionError("Таймаут подключения к API")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Ошибка запроса к API: {str(e)}")