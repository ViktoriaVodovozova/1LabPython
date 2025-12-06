"""Основной модуль клиент-серверного приложения с CRUD"""

import http.server
import socketserver
import urllib.parse
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
from jinja2 import Environment, PackageLoader, select_autoescape
from models.author import Author
from models.app import App
from utils.currencies_api import get_currencies
from controllers.databasecontroller import DatabaseController
from controllers.currencycontroller import CurrencyController
from controllers.usercontroller import UserController
from controllers.pages import PagesController

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Инициализация Jinja2 Environment
env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape(['html', 'xml'])
)

# Инициализация базы данных
db_controller = DatabaseController()
currency_controller = CurrencyController(db_controller)
user_controller = UserController(db_controller)
pages_controller = PagesController(env)

# Тестовые данные
main_author = Author(name="Виктория", group="P3121")
main_app = App(name="CurrenciesListApp", version="1.0", author=main_author)

# Последнее обновление курсов
last_update = datetime.now().strftime("%d.%m.%Y %H:%M:%S")


def update_currencies_from_api():
    """Обновляет курсы валют из API ЦБ РФ"""
    global last_update
    try:
        api_currencies = get_currencies()
        cursor = db_controller.conn.cursor()

        # Обновляем курсы для каждой валюты из API
        for currency in api_currencies:
            cursor.execute('''
            UPDATE currency 
            SET value = ? 
            WHERE char_code = ?
            ''', (currency.value, currency.char_code))

        db_controller.conn.commit()
        last_update = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        logger.info(f"Успешно обновлены курсы для {cursor.rowcount} валют")
    except Exception as e:
        logger.error(f"Ошибка при обновлении курсов валют: {e}")


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    """Обработчик HTTP запросов с поддержкой CRUD."""

    def _send_response(self, content: str, status_code: int = 200, content_type: str = "text/html") -> None:
        content_bytes = content.encode('utf-8')
        self.send_response(status_code)
        self.send_header("Content-type", f"{content_type}; charset=utf-8")
        self.send_header("Content-length", str(len(content_bytes)))  # ← длина в БАЙТАХ!
        self.end_headers()
        self.wfile.write(content_bytes)

    def _get_navigation(self) -> List[Dict[str, str]]:
        """Возвращает навигационное меню."""
        return [
            {"caption": "Главная", "href": "/"},
            {"caption": "Пользователи", "href": "/users"},
            {"caption": "Валюты", "href": "/currencies"},
            {"caption": "Автор", "href": "/author"}
        ]

    def do_GET(self) -> None:
        """Обрабатывает GET запросы."""
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        try:
            if parsed_path.path == "/":
                self._handle_index()
            elif parsed_path.path == "/users":
                self._handle_users()
            elif parsed_path.path == "/user":
                user_id = query_params.get("id", [""])[0]
                if user_id.isdigit():
                    self._handle_user(int(user_id))
                else:
                    self._send_error(400, "Некорректный ID пользователя")
            elif parsed_path.path == "/currencies":
                self._handle_currencies()
            elif parsed_path.path == "/author":
                self._handle_author()
            elif parsed_path.path == "/currency/delete":
                currency_id = query_params.get("id", [""])[0]
                if currency_id.isdigit():
                    self._handle_delete_currency(int(currency_id))
                else:
                    self._send_error(400, "Некорректный ID валюты")
            elif parsed_path.path == "/currency/update":
                # Обработка обновления курса валюты
                updated = False
                for char_code, value_str in query_params.items():
                    if char_code.upper() in ["USD", "EUR", "CNY", "JPY", "GBP"]:
                        try:
                            new_value = float(value_str[0])
                            currency = currency_controller.get_currency_by_char_code(char_code.upper())
                            if currency:
                                currency_controller.update_currency_value(currency['id'], new_value)
                                updated = True
                        except (ValueError, TypeError):
                            continue
                if updated:
                    self._handle_currencies()
                else:
                    self._send_error(400, "Некорректные параметры для обновления")
            elif parsed_path.path == "/currency/show":
                self._handle_show_currencies()
            elif parsed_path.path.startswith("/static/"):
                self._handle_static(parsed_path.path)
            else:
                self._send_error(404, "Страница не найдена")
        except Exception as e:
            logger.error(f"Ошибка при обработке запроса: {e}")
            self._send_error(500, "Внутренняя ошибка сервера")

    def _handle_index(self) -> None:
        """Обрабатывает запрос к главной странице."""
        context = {
            "title": "Главная страница",
            "myapp": main_app,
            "author": main_author,
            "navigation": self._get_navigation()
        }
        html_content = pages_controller.render_index(context)
        self._send_response(html_content)

    def _handle_users(self) -> None:
        """Обрабатывает запрос к списку пользователей."""
        users = user_controller.list_users()
        context = {
            "title": "Список пользователей",
            "myapp": main_app,
            "author": main_author,
            "navigation": self._get_navigation(),
            "users": users
        }
        html_content = pages_controller.render_users(context)
        self._send_response(html_content)

    def _handle_user(self, user_id: int) -> None:
        """Обрабатывает запрос к странице конкретного пользователя."""
        user = user_controller.get_user(user_id)
        if not user:
            self._send_error(404, "Пользователь не найден")
            return

        subscriptions = user_controller.get_user_subscriptions(user_id)

        context = {
            "title": f"Пользователь: {user['name']}",
            "myapp": main_app,
            "author": main_author,
            "navigation": self._get_navigation(),
            "user": user,
            "subscriptions": subscriptions
        }
        html_content = pages_controller.render_user_detail(context)
        self._send_response(html_content)

    def _handle_currencies(self) -> None:
        """Обрабатывает запрос к списку валют."""
        # Обновляем курсы из API
        update_currencies_from_api()

        currencies = currency_controller.list_currencies()

        context = {
            "title": "Курсы валют",
            "myapp": main_app,
            "author": main_author,
            "navigation": self._get_navigation(),
            "currencies": currencies,
            "last_update": last_update
        }
        html_content = pages_controller.render_currencies(context)
        self._send_response(html_content)

    def _handle_author(self) -> None:
        """Обрабатывает запрос к информации об авторе."""
        context = {
            "title": "Информация об авторе",
            "myapp": main_app,
            "author": main_author,
            "navigation": self._get_navigation()
        }
        html_content = pages_controller.render_author(context)
        self._send_response(html_content)

    def _handle_delete_currency(self, currency_id: int) -> None:
        """Обрабатывает запрос на удаление валюты."""
        success = currency_controller.delete_currency(currency_id)
        if success:
            self.send_response(302)
            self.send_header("Location", "/currencies")
            self.end_headers()
        else:
            self._send_error(404, "Валюта не найдена")

    def _handle_show_currencies(self) -> None:
        """Выводит валюты в консоль для отладки."""
        currencies = currency_controller.list_currencies()
        logger.info("Текущие валюты в базе данных:")
        for currency in currencies:
            logger.info(f"{currency['char_code']}: {currency['value']}")

        self._send_response("Курсы валют выведены в консоль сервера", content_type="text/plain")

    def _handle_static(self, path: str) -> None:
        """Обрабатывает запросы к статическим файлам."""
        # Для учебного проекта можно вернуть заглушку
        if path.endswith(".css"):
            content_type = "text/css"
            content = "body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }"
        else:
            content_type = "text/plain"
            content = ""

        self.send_response(200)
        self.send_header("Content-type", content_type)
        self.send_header("Content-length", str(len(content)))
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

    def _send_error(self, status_code: int, message: str) -> None:
        """Отправляет страницу с ошибкой."""
        context = {
            "title": f"Ошибка {status_code}",
            "myapp": main_app,
            "author": main_author,
            "navigation": self._get_navigation(),
            "error_message": message,
            "status_code": status_code
        }

        # Используем base.html для отображения ошибки
        template = env.get_template("base.html")
        html_content = template.render(
            **context,
            content=f"""
            <section class="error">
                <h2>Ошибка {status_code}</h2>
                <p>{message}</p>
                <p><a href="/">Вернуться на главную страницу</a></p>
            </section>
            """
        )
        self._send_response(html_content, status_code)


def run_server(port: int = 8199) -> None:
    """Запускает HTTP сервер."""
    with socketserver.TCPServer(("", port), MyRequestHandler) as httpd:
        logger.info(f"Сервер запущен на порту {port}")
        logger.info("Доступные маршруты:")
        logger.info("  http://localhost:8199/ - Главная страница")
        logger.info("  http://localhost:8199/users - Список пользователей")
        logger.info("  http://localhost:8199/user?id=1 - Информация о пользователе")
        logger.info("  http://localhost:8199/currencies - Курсы валют")
        logger.info("  http://localhost:8199/author - Информация об авторе")
        logger.info("  http://localhost:8199/currency/delete?id=1 - Удаление валюты")
        logger.info("  http://localhost:8199/currency/update?USD=78.5 - Обновление курса")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            logger.info("Сервер остановлен")
        except Exception as e:
            logger.error(f"Ошибка сервера: {e}")
        finally:
            db_controller.close()


if __name__ == "__main__":
    run_server()
