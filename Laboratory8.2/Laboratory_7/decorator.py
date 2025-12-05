import sys
import functools
import logging


def logger(func=None, *, handle=sys.stdout):
    """
    Параметризуемый декоратор для логирования.
    Поддерживает 3 режима:
    1. sys.stdout (по умолчанию)
    2. Любой файлоподобный объект (например, io.StringIO)
    3. Объект logging.Logger
    """
    if func is None:
        return functools.partial(logger, handle=handle)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Определяем тип логгера
        is_logging_logger = isinstance(handle, logging.Logger)

        # Формируем строку аргументов
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        # Логирование старта вызова
        start_msg = f"INFO: Вызов {func.__name__}({signature})"

        if is_logging_logger:
            handle.info(start_msg)
        else:
            handle.write(start_msg + "\n")

        try:
            result = func(*args, **kwargs)
            # Логируем успешное завершение
            end_msg = f"INFO: {func.__name__} вернула {repr(result)}"
            if is_logging_logger:
                handle.info(end_msg)
            else:
                handle.write(end_msg + "\n")
            return result
        except Exception as e:
            # Логируем ошибку
            error_msg = f"ERROR: Исключение в {func.__name__}: {type(e).__name__} - {str(e)}"
            if is_logging_logger:
                handle.error(error_msg)
            else:
                handle.write(error_msg + "\n")
            raise

    return wrapper