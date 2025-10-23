import timeit

import matplotlib.pyplot as plt


def build_tree_iterative(height=4, root=4, l_b=lambda x: x * 4, r_b=lambda x: x + 1):
    """
    Строит бинарное дерево итеративным способом.

    Args:
        height: Высота дерева
        root: Значение корня
        l_b: Функция для левого потомка
        r_b: Функция для правого потомка

    Returns:
        Бинарное дерево в виде словаря
    """
    # Используем очередь для обхода в ширину
    queue = []
    current_height = 0
    tree = {str(root): []}

    if height > 1:
        queue.append((str(root), tree[str(root)]))

    while queue and current_height < height - 1:
        level_size = len(queue)
        for i in range(level_size):
            current_root, current_list = queue.pop(0)

            if '.' in current_root:
                current_value = float(current_root)
            else:
                current_value = int(current_root)

            left_value = l_b(current_value)
            right_value = r_b(current_value)
            left_root = {str(left_value): []}
            right_root = {str(right_value): []}
            current_list.extend([left_root, right_root])

            # Добавляем потомков в очередь для следующего уровня
            if current_height + 1 < height - 1:
                queue.append((str(left_value), left_root[str(left_value)]))
                queue.append((str(right_value), right_root[str(right_value)]))

        current_height += 1

    return tree


def build_tree_recursive(height=4, root=4, l_b=lambda x: x * 4, r_b=lambda y: y + 1):
    """
    Строит бинарное дерево рекурсивным способом.

    Args:
        height: Высота дерева
        root: Значение корня
        l_b: Функция для левого потомка
        r_b: Функция для правого потомка

    Returns:
        Бинарное дерево в виде словаря
    """
    if height <= 1:
        return {str(root): []}
    return {str(root): [build_tree_recursive(height - 1, l_b(root), l_b, r_b),
                        build_tree_recursive(height - 1, r_b(root), l_b, r_b)]}


def benchmark(func, n, number=1, repeat=5):
    """
    Замеряет время выполнения функции.

    Args:
        func: Функция для тестирования
        n: Параметр для функции
        number: Количество запусков
        repeat: Количество повторений

    Returns:
        Минимальное время выполнения
    """
    times = timeit.repeat(lambda: func(height=n), number=number, repeat=repeat)
    return min(times)


def main():
    """Основная функция для сравнения производительности."""
    test_data = list(range(1, 10))

    res_recursive = []
    res_without_recursive = []

    for n in test_data:
        res_without_recursive.append(benchmark(build_tree_iterative, n, repeat=3, number=10))
        res_recursive.append(benchmark(build_tree_recursive, n, repeat=3, number=10))

    # Визуализация
    plt.plot(test_data, res_recursive, label="Рекурсивный")
    plt.plot(test_data, res_without_recursive, label="Итеративный")
    plt.xlabel("Высота дерева")
    plt.ylabel("Время (сек)")
    plt.title("Рекурсивный и итеративный способы построения бинарного дерева")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
