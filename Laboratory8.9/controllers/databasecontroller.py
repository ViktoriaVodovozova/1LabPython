import sqlite3
from typing import List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class DatabaseController:
    """Контроллер для работы с базой данных SQLite в памяти"""

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.row_factory = sqlite3.Row  # Позволяет обращаться к столбцам по имени
        self._initialize_database()

    def _initialize_database(self):
        """Инициализация базы данных и создание таблиц"""
        cursor = self.conn.cursor()

        # Таблица пользователей
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''')

        # Таблица валют
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS currency (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num_code TEXT NOT NULL,
            char_code TEXT NOT NULL,
            name TEXT NOT NULL,
            value REAL,
            nominal INTEGER
        )
        ''')

        # Таблица подписок пользователей на валюты
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_currency (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            currency_id INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES user(id),
            FOREIGN KEY(currency_id) REFERENCES currency(id),
            UNIQUE(user_id, currency_id)
        )
        ''')

        # Включение поддержки внешних ключей
        cursor.execute("PRAGMA foreign_keys = ON")

        # Заполнение тестовыми данными
        self._populate_initial_data()

        self.conn.commit()
        logger.info("База данных успешно инициализирована")

    def _populate_initial_data(self):
        """Заполнение базы тестовыми данными"""
        cursor = self.conn.cursor()

        # Тестовые пользователи
        users = [
            ("Ксю очень вайбовая",),
            ("Лера Шибитова",),
            ("Настя Пирогова",),
            ("Аня Панфилова",),
            ("Милена Назарова",),
            ("Лиза Сетало",),

        ]
        cursor.executemany("INSERT INTO user (name) VALUES (?)", users)

        # Тестовые валюты
        currencies = [
            ("840", "USD", "Доллар США", 77.5, 1),
            ("978", "EUR", "Евро", 90.34, 1),
            ("156", "CNY", "Китайский юань", 10.96, 10),
            ("392", "JPY", "Японская иена", 0.52, 100),
            ("826", "GBP", "Фунт стерлингов", 102.50, 1)
        ]
        cursor.executemany(
            "INSERT INTO currency (num_code, char_code, name, value, nominal) VALUES (?, ?, ?, ?, ?)",
            currencies
        )

        # Тестовые подписки
        subscriptions = [
            (1, 1),  # Пользователь 1 → USD
            (1, 2),  # Пользователь 1 → EUR
            (2, 1),  # Пользователь 2 → USD
            (3, 3),  # Пользователь 3 → CNY
            (4, 4),  # Пользователь 4 → JPY
            (5, 5),  # Пользователь 5 → GBP
            (6, 2)  # Новый пользователь 6 → EUR (уникальная пара!)
        ]
        cursor.executemany(
            "INSERT INTO user_currency (user_id, currency_id) VALUES (?, ?)",
            subscriptions
        )

    # CRUD для пользователей
    def get_all_users(self) -> List[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM user")
        return [dict(row) for row in cursor.fetchall()]

    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM user WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def get_user_subscriptions(self, user_id: int) -> List[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT c.* FROM currency c
        JOIN user_currency uc ON c.id = uc.currency_id
        WHERE uc.user_id = ?
        ''', (user_id,))
        return [dict(row) for row in cursor.fetchall()]

    # CRUD для валют
    def get_all_currencies(self) -> List[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM currency")
        return [dict(row) for row in cursor.fetchall()]

    def get_currency_by_id(self, currency_id: int) -> Optional[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM currency WHERE id = ?", (currency_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def update_currency_value(self, currency_id: int, new_value: float) -> bool:
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE currency SET value = ? WHERE id = ?",
            (new_value, currency_id)
        )
        self.conn.commit()
        return cursor.rowcount > 0

    def delete_currency(self, currency_id: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM currency WHERE id = ?", (currency_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    # Методы для подписок
    def add_subscription(self, user_id: int, currency_id: int) -> bool:
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO user_currency (user_id, currency_id) VALUES (?, ?)",
                (user_id, currency_id)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Подписка уже существует
            return False

    def remove_subscription(self, user_id: int, currency_id: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM user_currency WHERE user_id = ? AND currency_id = ?",
            (user_id, currency_id)
        )
        self.conn.commit()
        return cursor.rowcount > 0

    def close(self):
        """Закрытие соединения с базой данных"""
        self.conn.close()