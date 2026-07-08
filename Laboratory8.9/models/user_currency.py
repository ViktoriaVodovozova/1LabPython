"""Модель связи пользователя и валюты (подписка)."""

from typing import Optional


class UserCurrency:
    """Класс, представляющий связь пользователя и валюты."""

    _next_id = 1

    def __init__(self, user_id: int, currency_id: str) -> None:
        """
        Инициализирует объект связи пользователя и валюты.

        Args:
            user_id: ID пользователя
            currency_id: ID валюты
        """
        self._id = UserCurrency._next_id
        UserCurrency._next_id += 1
        self._user_id = 0
        self._currency_id = ""
        self.user_id = user_id
        self.currency_id = currency_id

    @property
    def id(self) -> int:
        """
        Возвращает уникальный идентификатор связи.

        Returns:
            int: ID связи
        """
        return self._id

    @property
    def user_id(self) -> int:
        """
        Возвращает ID пользователя.

        Returns:
            int: ID пользователя
        """
        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        """
        Устанавливает ID пользователя.

        Args:
            value: Новый ID пользователя

        Raises:
            ValueError: Если ID не является целым числом или не положительный
        """
        if not isinstance(value, int):
            raise ValueError("ID пользователя должен быть целым числом")
        if value <= 0:
            raise ValueError("ID пользователя должен быть положительным")
        self._user_id = value

    @property
    def currency_id(self) -> str:
        """
        Возвращает ID валюты.

        Returns:
            str: ID валюты
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, value: str) -> None:
        """
        Устанавливает ID валюты.

        Args:
            value: Новый ID валюты

        Raises:
            ValueError: Если ID пустой или не является строкой
        """
        if not isinstance(value, str):
            raise ValueError("ID валюты должен быть строкой")
        if not value.strip():
            raise ValueError("ID валюты не может быть пустым")
        self._currency_id = value.strip()