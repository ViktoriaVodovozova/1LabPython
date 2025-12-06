from typing import List, Dict, Any, Optional
from controllers.databasecontroller import DatabaseController


class CurrencyController:
    """Контроллер для бизнес-логики работы с валютами"""

    def __init__(self, db_controller: DatabaseController):
        self.db = db_controller

    def list_currencies(self) -> List[Dict[str, Any]]:
        """Получение списка всех валют"""
        return self.db.get_all_currencies()

    def get_currency(self, currency_id: int) -> Optional[Dict[str, Any]]:
        """Получение валюты по ID"""
        return self.db.get_currency_by_id(currency_id)

    def update_currency_value(self, currency_id: int, new_value: float) -> bool:
        """Обновление курса валюты"""
        if new_value <= 0:
            raise ValueError("Курс валюты должен быть положительным числом")
        return self.db.update_currency_value(currency_id, new_value)

    def delete_currency(self, currency_id: int) -> bool:
        """Удаление валюты"""
        return self.db.delete_currency(currency_id)

    def get_currency_by_char_code(self, char_code: str) -> Optional[Dict[str, Any]]:
        """Получение валюты по символьному коду"""
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM currency WHERE char_code = ?", (char_code,))
        row = cursor.fetchone()
        return dict(row) if row else None