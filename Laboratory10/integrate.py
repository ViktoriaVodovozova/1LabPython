import math
from typing import Callable


def integrate(f: Callable[[float], float], a: float, b: float, *, n_iter: int = 100_000) -> float:
    """
    Численное интегрирование методом прямоугольников.
    Вычисляет приближённое значение определённого интеграла,
    используя левые прямоугольники и равномерное разбиение отрезка.

    Args:
        f: Интегрируемая функция одной переменной.
        a: Нижний предел интегрирования.
        b: Верхний предел интегрирования.
        n_iter: Количество прямоугольников. Должно быть положительным целым числом.

    Returns:
        Приближённое значение интеграла.

    Raises:
        ValueError: Если a > b или n_iter <= 0.

    """
    if a > b:
        raise ValueError("Нижний предел интегрирования не может быть больше верхнего.")
    if n_iter <= 0:
        raise ValueError("n_iter должен быть положительным целым числом.")

    acc = 0.0
    step = (b - a) / n_iter
    for i in range(n_iter):
        x = a + i * step
        acc += f(x) * step
    return acc