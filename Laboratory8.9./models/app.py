"""Модель приложения."""

from typing import Optional
from .author import Author


class App:
    """Класс, представляющий приложение."""

    def __init__(self, name: str, version: str, author: Author) -> None:
        """
        Инициализирует объект приложения.

        Args:
            name: Название приложения
            version: Версия приложения
            author: Объект автора приложения
        """
        self._name = ""
        self._version = ""
        self._author = None
        self.name = name
        self.version = version
        self.author = author

    @property
    def name(self) -> str:
        """
        Возвращает название приложения.

        Returns:
            str: Название приложения
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Устанавливает название приложения.

        Args:
            value: Новое название приложения

        Raises:
            ValueError: Если название пустое или не является строкой
        """
        if not isinstance(value, str):
            raise ValueError("Название приложения должно быть строкой")
        if not value.strip():
            raise ValueError("Название приложения не может быть пустым")
        self._name = value.strip()

    @property
    def version(self) -> str:
        """
        Возвращает версию приложения.

        Returns:
            str: Версия приложения
        """
        return self._version

    @version.setter
    def version(self, value: str) -> None:
        """
        Устанавливает версию приложения.

        Args:
            value: Новая версия приложения

        Raises:
            ValueError: Если версия пустая или не является строкой
        """
        if not isinstance(value, str):
            raise ValueError("Версия приложения должна быть строкой")
        if not value.strip():
            raise ValueError("Версия приложения не может быть пустой")
        self._version = value.strip()

    @property
    def author(self) -> Author:
        """
        Возвращает автора приложения.

        Returns:
            Author: Объект автора приложения
        """
        return self._author

    @author.setter
    def author(self, value: Author) -> None:
        """
        Устанавливает автора приложения.

        Args:
            value: Новый объект автора

        Raises:
            ValueError: Если переданный объект не является экземпляром Author
        """
        if not isinstance(value, Author):
            raise ValueError("Автор должен быть объектом класса Author")
        self._author = value