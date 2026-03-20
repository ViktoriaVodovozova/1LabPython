import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. СОЗДАНИЕ И ОБРАБОТКА МАССИВОВ
# ============================================================

def create_vector():
    """
    Создать массив от 0 до 9.
    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.arange.html
    Returns:
        numpy.ndarray: Массив чисел от 0 до 9 включительно
    """
    return np.arange(10)
# print(create_vector())


def create_matrix():
    """
    Создать матрицу 5x5 со случайными числами [0,1].
    Изучить:
    https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html
    Returns:
        numpy.ndarray: Матрица 5x5 со случайными значениями от 0 до 1
    """
    # Подсказка: используйте np.random.rand(5,5)
    return np.random.rand(5,5)



def reshape_vector(vec):
    """
    Преобразовать (10,) -> (2,5)
    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
    Args:
        vec (numpy.ndarray): Входной массив формы (10,)
    Returns:
        numpy.ndarray: Преобразованный массив формы (2, 5)
    """
    # Подсказка: используйте vec.reshape(2,5)
    return vec.reshape(2, 5)


def transpose_matrix(mat):
    """
    Транспонирование матрицы.
    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
    Args:
        mat (numpy.ndarray): Входная матрица
    Returns:
        numpy.ndarray: Транспонированная матрица
    """
    return np.transpose(mat)


# # ============================================================
# # 2. ВЕКТОРНЫЕ ОПЕРАЦИИ
# # ============================================================

def vector_add(a, b):
    """
    Сложение векторов одинаковой длины.
    (Векторизация без циклов)
    Args:
        a (numpy.ndarray): Первый вектор
        b (numpy.ndarray): Второй вектор
    Returns:
        numpy.ndarray: Результат поэлементного сложения
    """
    # Подсказка: используйте оператор +
    return a + b


def scalar_multiply(vec, scalar):
    """
    Умножение вектора на число.
    Args:
        vec (numpy.ndarray): Входной вектор
        scalar (float/int): Число для умножения
    Returns:
        numpy.ndarray: Результат умножения вектора на скаляр
    """
    # Подсказка: используйте оператор *
    return vec * scalar


def elementwise_multiply(a, b):
    """
    Поэлементное умножение.
    Args:
        a (numpy.ndarray): Первый вектор/матрица
        b (numpy.ndarray): Второй вектор/матрица
    Returns:
        numpy.ndarray: Результат поэлементного умножения
    """
    # Подсказка: используйте оператор *
    return a * b


def dot_product(a, b):
    """
    Скалярное произведение.
    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.dot.html
    Args:
        a (numpy.ndarray): Первый вектор
        b (numpy.ndarray): Второй вектор
    Returns:
        float: Скалярное произведение векторов
    """
    # Подсказка: используйте np.dot(a, b)
    return np.dot(a,b)


# # ============================================================
# # 3. МАТРИЧНЫЕ ОПЕРАЦИИ
# # ============================================================

def matrix_multiply(a, b):
    """
    Умножение матриц.
    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
    Args:
        a (numpy.ndarray): Первая матрица
        b (numpy.ndarray): Вторая матрица
    Returns:
        numpy.ndarray: Результат умножения матриц
    """
    # Подсказка: используйте a @ b или np.matmul(a, b)
    return np.matmul(a,b)


def matrix_determinant(a):
    """
    Определитель матрицы.
    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html
    Args:
        a (numpy.ndarray): Квадратная матрица
    Returns:
            float: Определитель матрицы
        """
    # Подсказка: используйте np.linalg.det(a)
    return np.linalg.det(a)


def matrix_inverse(a):
    """
    Обратная матрица.
    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html
    Args:
        a (numpy.ndarray): Квадратная матрица
    Returns:
        numpy.ndarray: Обратная матрица
    """
    # Подсказка: используйте np.linalg.inv(a)
    return np.linalg.inv(a)


def solve_linear_system(a, b):
    """
    Решить систему Ax = b
    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html
    Args:
        a (numpy.ndarray): Матрица коэффициентов A
        b (numpy.ndarray): Вектор свободных членов b
    Returns:
        numpy.ndarray: Решение системы x
    """
    # Подсказка: используйте np.linalg.solve(a, b)
    return np.linalg.solve(a,b)


# # ============================================================
# # 4. СТАТИСТИЧЕСКИЙ АНАЛИЗ
# # ============================================================

def load_dataset(path="data/students_scores.csv"):
    """
    Загрузить CSV и вернуть NumPy массив.
    Args:
        path (str): Путь к CSV файлу
    Returns:
        numpy.ndarray: Загруженные данные в виде массива
    """
    # Подсказка: используйте pd.read_csv(path).to_numpy()
    return pd.read_csv(path).to_numpy()


def statistical_analysis(data):
    """
    Представьте, что данные — это результаты экзамена по математике.
    Нужно оценить:
    - средний балл
    - медиану
    - стандартное отклонение
    - минимум
    - максимум
    - 25 и 75 перцентили
    Изучить:
    https://numpy.org/doc/stable/reference/generated/numpy.mean.html
    https://numpy.org/doc/stable/reference/generated/numpy.median.html
    https://numpy.org/doc/stable/reference/generated/numpy.std.html
    https://numpy.org/doc/stable/reference/generated/numpy.percentile.html
    Args:
        data (numpy.ndarray): Одномерный массив данных
    Returns:
        dict: Словарь со статистическими показателями
    """
    # Подсказка: используйте np.mean(), np.median(), np.std(),
    # np.min(), np.max(), np.percentile(data, 25), np.percentile(data, 75)
    return{
        "mean": np.mean(data),
        "median": np.median(data),
        "std": np.std(data),
        "min": np.min(data),
        "max": np.max(data),
        "percentile_25": np.percentile(data, 25),
        "percentile_75": np.percentile(data, 75)
    }



def normalize_data(data):
    """
    Min-Max нормализация.
    Формула: (x - min) / (max - min)
    Args:
        data (numpy.ndarray): Входной массив данных
    Returns:
        numpy.ndarray: Нормализованный массив данных в диапазоне [0, 1]
    """
    # Подсказка: вычислите min и max# Шаг 1: находим минимум и максимум в данных
    min_val = np.min(data)
    max_val = np.max(data)

    # Шаг 2: защита от деления на ноль (если все значения одинаковы)
    if max_val == min_val:
        return np.zeros_like(data, dtype=float)

    # Шаг 3: применяем формулу нормализации ко всему массиву сразу
    # NumPy автоматически применит операцию к каждому элементу (векторизация!)
    normalized = (data - min_val) / (max_val - min_val)

    return normalized

# # ============================================================
# # 5. ВИЗУАЛИЗАЦИЯ
# # ============================================================

def plot_histogram(data):
    """
    Построить гистограмму распределения оценок по математике.
    Изучить:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
    Args:
        data (numpy.ndarray): Данные для гистограммы
    """
    # Подсказка: используйте plt.hist(), добавьте заголовок, подписи осей,
    # сохраните в папку plots с помощью plt.savefig()
    plt.hist(data)
    plt.title('Распределение оценок по математике')
    plt.xlabel('Оценка')
    plt.ylabel('Частота')

    os.makedirs('plots', exist_ok=True)
    plt.savefig('plots/histogram.png')
    plt.close()



def plot_heatmap(matrix):
    """
    Построить тепловую карту корреляции предметов.

    Изучить:
    https://seaborn.pydata.org/generated/seaborn.heatmap.html

    Args:
        matrix (numpy.ndarray): Матрица корреляции
    """
    # Подсказка: используйте sns.heatmap(), добавьте заголовок, сохраните
    sns.heatmap(matrix)
    plt.title('Тепловая карта корреляции')

    os.makedirs('plots', exist_ok=True)
    plt.savefig('plots/heatmap.png')
    plt.close()


def plot_line(x, y):
    """
    Построить график зависимости: студент -> оценка по математике.

    Изучить:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

    Args:
        x (numpy.ndarray): Номера студентов
        y (numpy.ndarray): Оценки студентов
    """
    # Подсказка: используйте plt.plot(), добавьте заголовок, подписи осей,
    # сохраните график
    plt.plot(x, y)
    plt.title('Оценки студентов по математике')
    plt.xlabel('Номер студента')
    plt.ylabel('Оценка')

    os.makedirs('plots', exist_ok=True)
    plt.savefig('plots/line_plot.png')
    plt.close()
