import timeit
import math
from integrate_parallel import integrate_threaded, integrate_multiproc

def bench(func, *args, **kwargs):
    return timeit.timeit(lambda: func(*args, **kwargs), number=3) / 3

def run_parallel_benchmark():
    print("Сравнение потоков и процессов")
    n_iter_list = [10_000, 50_000, 100_000]
    n_jobs_list = [2, 4, 6, 8]

    for n_jobs in n_jobs_list:
        for n_iter in n_iter_list:
            t_threads = bench(integrate_threaded, math.sin, 0, math.pi,
                          n_jobs=n_jobs, n_iter=n_iter)
            t_procs = bench(integrate_multiproc, math.sin, 0, math.pi,
                        n_jobs=n_jobs, n_iter=n_iter)
            print(f"n_iter={n_iter}, n_jobs={n_jobs}: потоки={t_threads:.4f}с, процессы={t_procs:.4f}с")

if __name__ == "__main__":
    run_parallel_benchmark()