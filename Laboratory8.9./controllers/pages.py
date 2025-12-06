from jinja2 import Environment
from typing import Dict, Any


class PagesController:
    """Контроллер для рендеринга страниц"""

    def __init__(self, env: Environment):
        self.env = env

    def render_index(self, context: Dict[str, Any]) -> str:
        """Рендеринг главной страницы"""
        template = self.env.get_template("index.html")
        return template.render(**context)


    def render_author(self, context: Dict[str, Any]) -> str:
        """Рендеринг страницы об авторе"""
        template = self.env.get_template("author.html")
        return template.render(**context)

    def render_users(self, context: Dict[str, Any]) -> str:
        """Рендеринг страницы со списком пользователей"""
        template = self.env.get_template("users.html")
        return template.render(**context)

    def render_user_detail(self, context: Dict[str, Any]) -> str:
        """Рендеринг страницы с детальной информацией о пользователе"""
        template = self.env.get_template("user.html")
        return template.render(**context)

    def render_currencies(self, context: Dict[str, Any]) -> str:
        """Рендеринг страницы со списком валют"""
        template = self.env.get_template("currencies.html")
        return template.render(**context)