import concurrent.futures
from typing import Callable
from integrate import integrate

def integrate_threaded(f: Callable[[float], float], a: float, b: float, *,
                       n_jobs: int = 2, n_iter: int = 100_000) -> float:
    """Вычисление интеграла с использованием потоков (ThreadPoolExecutor)."""
    if n_jobs <= 0:
        raise ValueError("n_jobs должен быть >= 1")
    if a > b:
        raise ValueError("Нижний предел не может быть больше верхнего.")
    if n_iter <= 0:
        raise ValueError("n_iter должен быть положительным целым числом.")
    step = (b - a) / n_jobs
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        futures = [
            executor.submit(integrate, f, a + i * step, a + (i + 1) * step,
                            n_iter=n_iter // n_jobs)
            for i in range(n_jobs)]
        return sum(fut.result() for fut in futures)

def integrate_multiproc(f: Callable[[float], float], a: float, b: float, *,
                        n_jobs: int = 2, n_iter: int = 100_000) -> float:
    """Вычисление интеграла с использованием процессов (ProcessPoolExecutor)."""
    if n_jobs <= 0:
        raise ValueError("n_jobs должен быть >= 1")
    if a > b:
        raise ValueError("Нижний предел не может быть больше верхнего.")
    if n_iter <= 0:
        raise ValueError("n_iter должен быть положительным целым числом.")
    step = (b - a) / n_jobs
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        futures = [
            executor.submit(integrate, f, a + i * step, a + (i + 1) * step,
                            n_iter=n_iter // n_jobs)
            for i in range(n_jobs)]
        return sum(fut.result() for fut in futures)