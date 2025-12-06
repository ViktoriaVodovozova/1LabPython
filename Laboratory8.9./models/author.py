"""Модель автора приложения."""

from typing import Optional


class Author:
    """Класс, представляющий автора приложения."""

    def __init__(self, name: str, group: str) -> None:
        """
        Инициализирует объект автора.

        Args:
            name: Имя автора
            group: Учебная группа автора
        """
        self._name = ""
        self._group = ""
        self.name = name
        self.group = group

    @property
    def name(self) -> str:
        """
        Возвращает имя автора.

        Returns:
            str: Имя автора
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Устанавливает имя автора.

        Args:
            value: Новое имя автора

        Raises:
            ValueError: Если имя пустое или не является строкой
        """
        if not isinstance(value, str):
            raise ValueError("Имя автора должно быть строкой")
        if not value.strip():
            raise ValueError("Имя автора не может быть пустым")
        self._name = value.strip()

    @property
    def group(self) -> str:
        """
        Возвращает учебную группу автора.

        Returns:
            str: Учебная группа автора
        """
        return self._group

    @group.setter
    def group(self, value: str) -> None:
        """
        Устанавливает учебную группу автора.

        Args:
            value: Новая учебная группа

        Raises:
            ValueError: Если группа пустая или не является строкой
        """
        if not isinstance(value, str):
            raise ValueError("Учебная группа должна быть строкой")
        if not value.strip():
            raise ValueError("Учебная группа не может быть пустой")
        self._group = value.strip()