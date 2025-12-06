"""Модель валюты."""

from typing import Optional


class Currency:
    """Класс, представляющий валюту."""

    def __init__(self, num_code: str, char_code: str, name: str,
                 value: float, nominal: int) -> None:
        """
        Инициализирует объект валюты.

        Args:
            num_code: Цифровой код валюты
            char_code: Символьный код валюты
            name: Название валюты
            value: Курс валюты
            nominal: Номинал (за сколько единиц валюты указан курс)
        """
        self._id = f"{num_code}_{char_code}"
        self._num_code = ""
        self._char_code = ""
        self._name = ""
        self._value = 0.0
        self._nominal = 0
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value
        self.nominal = nominal

    @property
    def id(self) -> str:
        """
        Возвращает уникальный идентификатор валюты.

        Returns:
            str: ID валюты (комбинация цифрового и символьного кодов)
        """
        return self._id

    @property
    def num_code(self) -> str:
        """
        Возвращает цифровой код валюты.

        Returns:
            str: Цифровой код валюты
        """
        return self._num_code

    @num_code.setter
    def num_code(self, value: str) -> None:
        """
        Устанавливает цифровой код валюты.

        Args:
            value: Новый цифровой код

        Raises:
            ValueError: Если код пустой или не является строкой
        """
        if not isinstance(value, str):
            raise ValueError("Цифровой код должен быть строкой")
        if not value.strip():
            raise ValueError("Цифровой код не может быть пустым")
        self._num_code = value.strip()

    @property
    def char_code(self) -> str:
        """
        Возвращает символьный код валюты.

        Returns:
            str: Символьный код валюты
        """
        return self._char_code

    @char_code.setter
    def char_code(self, value: str) -> None:
        """
        Устанавливает символьный код валюты.

        Args:
            value: Новый символьный код

        Raises:
            ValueError: Если код пустой или не является строкой
        """
        if not isinstance(value, str):
            raise ValueError("Символьный код должен быть строкой")
        if not value.strip():
            raise ValueError("Символьный код не может быть пустым")
        self._char_code = value.strip()

    @property
    def name(self) -> str:
        """
        Возвращает название валюты.

        Returns:
            str: Название валюты
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Устанавливает название валюты.

        Args:
            value: Новое название

        Raises:
            ValueError: Если название пустое или не является строкой
        """
        if not isinstance(value, str):
            raise ValueError("Название валюты должно быть строкой")
        if not value.strip():
            raise ValueError("Название валюты не может быть пустым")
        self._name = value.strip()

    @property
    def value(self) -> float:
        """
        Возвращает курс валюты.

        Returns:
            float: Курс валюты
        """
        return self._value

    @value.setter
    def value(self, value: float) -> None:
        """
        Устанавливает курс валюты.

        Args:
            value: Новый курс

        Raises:
            ValueError: Если курс не является числом или отрицательный
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Курс валюты должен быть числом")
        if value <= 0:
            raise ValueError("Курс валюты должен быть положительным")
        self._value = float(value)

    @property
    def nominal(self) -> int:
        """
        Возвращает номинал валюты.

        Returns:
            int: Номинал (за сколько единиц валюты указан курс)
        """
        return self._nominal

    @nominal.setter
    def nominal(self, value: int) -> None:
        """
        Устанавливает номинал валюты.

        Args:
            value: Новый номинал

        Raises:
            ValueError: Если номинал не является целым числом или не положительный
        """
        if not isinstance(value, int):
            raise ValueError("Номинал должен быть целым числом")
        if value <= 0:
            raise ValueError("Номинал должен быть положительным")
        self._nominal = value
