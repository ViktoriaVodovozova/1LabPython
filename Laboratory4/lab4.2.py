import matplotlib.pyplot as plt
import numpy as np
import timeit
import random
from functools import lru_cache
# help(lru_cache)

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

@lru_cache(maxsize=None)
def fact_recursive_with_cash(n: int) -> int:
    """Рекурсивный факториал c кешированием"""
    if n == 0:
        return 1
    return n * fact_recursive(n - 1)

@lru_cache(maxsize=700)
def fact_iterative_with_cash(n: int) -> int:
    """Нерекурсивный факториал с кешированием"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def benchmark(func, n, repeat=10):
    """Возвращает среднее время выполнения func(n)"""
    times = timeit.repeat(lambda: func(n), number=100, repeat=repeat)
    return min(times)



def main():
    # фиксированный набор данных
    test_data = list(range(10, 300, 10))

    res_recursive = []
    res_iterative = []
    res_recursive_cash = []
    res_iterative_cash = []

    for n in test_data:
        res_recursive.append(benchmark(fact_recursive, n))
        res_iterative.append(benchmark(fact_iterative, n))
        res_recursive_cash.append(benchmark(fact_recursive_with_cash, n))
        res_iterative_cash.append(benchmark(fact_iterative_with_cash, n))


    # 2Визуализация
    plt.plot(test_data, res_recursive_cash, label="Рекурсивный с кэшированием")
    plt.plot(test_data, res_iterative_cash, label="Итеративный с кэшированием")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение рекурсивного и итеративного факториала c кешированием")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()