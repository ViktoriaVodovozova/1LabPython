"""Модель пользователя."""

from typing import List, Optional


class User:
    """Класс, представляющий пользователя."""

    _next_id = 1

    def __init__(self, name: str) -> None:
        """
        Инициализирует объект пользователя.

        Args:
            name: Имя пользователя
        """
        self._id = User._next_id
        User._next_id += 1
        self._name = ""
        self.name = name

    @property
    def id(self) -> int:
        """
        Возвращает уникальный идентификатор пользователя.

        Returns:
            int: ID пользователя
        """
        return self._id

    @property
    def name(self) -> str:
        """
        Возвращает имя пользователя.

        Returns:
            str: Имя пользователя
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Устанавливает имя пользователя.

        Args:
            value: Новое имя пользователя

        Raises:
            ValueError: Если имя пустое или не является строкой
        """
        if not isinstance(value, str):
            raise ValueError("Имя пользователя должно быть строкой")
        if not value.strip():
            raise ValueError("Имя пользователя не может быть пустым")
        self._name = value.strip()