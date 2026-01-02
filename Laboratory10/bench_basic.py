import timeit
import math
from integrate import integrate

def run_basic_benchmark():
    print("Базовые замеры времени (только Python)")
    n_list = [10_000, 50_000, 100_000]
    for n in n_list:
        time_taken = timeit.timeit(
            lambda: integrate(math.sin, 0, math.pi, n_iter=n), number=3) / 3
        print(f"n_iter = {n:>6,} → {time_taken:.4f} сек")

if __name__ == "__main__":
    run_basic_benchmark()


