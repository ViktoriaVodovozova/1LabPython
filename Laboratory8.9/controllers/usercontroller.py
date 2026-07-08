from typing import List, Dict, Any, Optional
from controllers.databasecontroller import DatabaseController


class UserController:
    """Контроллер для бизнес-логики работы с пользователями"""

    def __init__(self, db_controller: DatabaseController):
        self.db = db_controller

    def list_users(self) -> List[Dict[str, Any]]:
        """Получение списка всех пользователей"""
        return self.db.get_all_users()

    def get_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Получение пользователя по ID"""
        return self.db.get_user_by_id(user_id)

    def get_user_subscriptions(self, user_id: int) -> List[Dict[str, Any]]:
        """Получение подписок пользователя"""
        return self.db.get_user_subscriptions(user_id)

    def add_subscription(self, user_id: int, currency_id: int) -> bool:
        """Добавление подписки пользователя на валюту"""
        return self.db.add_subscription(user_id, currency_id)

    def remove_subscription(self, user_id: int, currency_id: int) -> bool:
        """Удаление подписки пользователя с валюты"""
        return self.db.remove_subscription(user_id, currency_id)
