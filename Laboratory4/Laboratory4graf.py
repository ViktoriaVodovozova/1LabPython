import timeit
from functools import lru_cache

import matplotlib.pyplot as plt


def fact_recursive(n: int) -> int:
    """Рекурсивный факториал"""
    if n == 0:
        return 1
    return n * fact_recursive(n - 1)


def fact_iterative(n: int) -> int:
    """Нерекурсивный факториал"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


@lru_cache(maxsize=128)
def fact_recursive_with_cache(n: int) -> int:
    """Рекурсивный факториал c кешированием"""
    if n == 0:
        return 1
    return n * fact_recursive_with_cache(n - 1)


@lru_cache(maxsize=128)
def fact_iterative_with_cache(n: int) -> int:
    """Нерекурсивный факториал с кешированием"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def benchmark(func, data, number=1, repeat=5):
    """Возвращает среднее время выполнения func на наборе data"""
    total = 0
    for n in data:
        times = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
        total += min(times)
    return total / len(data)


def main():
    test_data = list(range(10, 300, 10))

    res_recursive = []
    res_iterative = []
    res_recursive_cache = []
    res_iterative_cache = []

    for n in test_data:
        res_recursive.append(benchmark(fact_recursive, [n], number=10000, repeat=5))
        res_iterative.append(benchmark(fact_iterative, [n], number=10000, repeat=5))
        res_recursive_cache.append(benchmark(fact_recursive_with_cache, [n], number=10000, repeat=5))
        res_iterative_cache.append(benchmark(fact_iterative_with_cache, [n], number=10000, repeat=5))

    # Первый график - без кеширования
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(test_data, res_recursive, label="Рекурсивный")
    plt.plot(test_data, res_iterative, label="Итеративный")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Без кеширования")
    plt.legend()

    # Второй график - с кешированием
    plt.subplot(1, 2, 2)
    plt.plot(test_data, res_recursive_cache, label="Рекурсивный с кешем")
    plt.plot(test_data, res_iterative_cache, label="Итеративный с кешем")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("С кешированием")
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
