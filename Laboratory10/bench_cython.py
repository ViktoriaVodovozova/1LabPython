import timeit
import math
import pyximport
pyximport.install()

from integrate_cy import integrate_cy
from integrate import integrate

def run_cython_benchmark():
    print("Сравнение Python vs Cython (с noGIL)")
    n_iter = 200_000

    t_py = timeit.timeit(
        lambda: integrate(math.sin, 0, math.pi, n_iter=n_iter),
        number=3
    ) / 3

    t_cy = timeit.timeit(
        lambda: integrate_cy(0.0, math.pi, n_iter),
        number=3
    ) / 3

    print(f"Python        : {t_py:.4f} сек")
    print(f"Cython (noGIL): {t_cy:.4f} сек")
    print(f"Ускорение     : {t_py / t_cy:.2f}x")

    # Проверка: работает ли многопоточность с noGIL
    import concurrent.futures
    def parallel_cython(n_jobs=4):
        step = math.pi / n_jobs
        n_per = n_iter // n_jobs
        with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as ex:
            futures = [
                ex.submit(integrate_cy, i * step, (i + 1) * step, n_per)
                for i in range(n_jobs)
            ]
            return sum(f.result() for f in futures)

    t_par = timeit.timeit(lambda: parallel_cython(4), number=3) / 3
    print(f"Cython + 4 потока: {t_par:.4f} сек (ускорение vs однопоточному: {t_cy / t_par:.2f}x)")

if __name__ == "__main__":
    run_cython_benchmark()