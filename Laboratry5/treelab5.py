def gen_bin_tree(height=4, root=4, l_b=lambda x: x * 4, r_b=lambda x: x + 1):
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

    if int(height) != height:
        raise TypeError("Введено нецелое количесество этажей")
    if str(height) == height:
        raise TypeError("Введено строковое представление числа")
    if height < 0:
        raise TypeError("Отрицательная высота")
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


def main():
    """
    Основная функция для демонстрации работы моего варианта gen_bin_tre.
    left_branch = root * 4
    right_branch = root + 1
    """
    res = gen_bin_tree(4, 4, lambda x: x * 4, lambda y: y + 1)
    print(res)


if __name__ == "__main__":
    main()


