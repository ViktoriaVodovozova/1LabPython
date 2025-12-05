import sys
import logging
from decorator import logger
from currency import get_currencies


# 1. Логирование в stdout
@logger(handle=sys.stdout)
def get_currencies_stdout(currency_codes):
    return get_currencies(currency_codes)


print("Логирование в stdout")
try:
    get_currencies_stdout(['USD', 'EUR'])
except Exception as e:
    print(f"Обработано исключение: {e}")

# 2. Файловое логирование
file_logger = logging.getLogger("currency_file")
file_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("currency.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
file_logger.addHandler(file_handler)


@logger(handle=file_logger)
def get_currencies_file(currency_codes):
    return get_currencies(currency_codes)


print("\n Логирование в файл currency.log")
try:
    get_currencies_file(['USD', 'XYZ'])  # XYZ вызовет KeyError
except KeyError as e:
    print(f"Перехвачено исключение: {e}")

# 3. Демонстрация solve_quadratic
quad_logger = logging.getLogger("quadratic")
quad_logger.setLevel(logging.INFO)
quad_logger.addHandler(logging.StreamHandler(sys.stdout))


@logger(handle=quad_logger)
def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0.
    Демонстрирует разные уровни логирования.
    """
    # Проверка типов
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        quad_logger.error(f"ERROR: Некорректные типы данных: a={a}, b={b}, c={c}")
        raise TypeError("Коэффициенты должны быть числами")

    # Критическая ошибка: a=b=0
    if a == 0 and b == 0:
        quad_logger.critical("CRITICAL: Оба коэффициента a и b равны 0. Уравнение не имеет смысла.")
        raise ValueError("a и b равны 0")

    discriminant = b ** 2 - 4 * a * c

    # Предупреждение: дискриминант < 0
    if discriminant < 0:
        quad_logger.warning(f"WARNING: Дискриминант отрицательный (D={discriminant}). Корней нет.")
        return []

    # Расчет корней
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    quad_logger.info(f"INFO: Два корня: x1={x1}, x2={x2}")
    return [x1, x2]


print("\nДемонстрация solve_quadratic")
print("1. Два корня (INFO):")
solve_quadratic(1, -3, 2)

print("\n2. Дискриминант < 0 (WARNING):")
solve_quadratic(1, 1, 1)

print("\n3. Некорректные данные (ERROR):")
try:
    solve_quadratic("abc", 5, 5)
except TypeError as e:
    print(f"Обработана ошибка: {e}")

print("\n4. a=b=0 (CRITICAL):")
try:
    solve_quadratic(0, 0, 64)
except ValueError as e:
    print(f"Обработана критическая ошибка: {e}")