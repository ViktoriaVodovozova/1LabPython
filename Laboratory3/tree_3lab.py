def gen_bin_tree(height: int = 0, root=4, l_b=lambda x: x, r_b=lambda y: y):
    """
        Генерирует бинарное дерево в виде словаря.

        Args:
            height: Высота дерева (целое число)
            root: Корневое значение
            l_b: Функция для левого потомка
            r_b: Функция для правого потомка

        Returns:
            Словарь вида {корень: [левый потомок, правое потомок]}
    """
    if int(height) != height:
        raise TypeError("Введено нецелое количесество этажей")
    if str(height) == height:
        raise TypeError("Введено строковое представление числа")
    if height <= 1:
        return {str(root): []}
    return {str(root): [gen_bin_tree(height - 1, l_b(root), l_b, r_b),
                        gen_bin_tree(height - 1, r_b(root), l_b, r_b)]}


def main():
    """
    Основная функция для демонстрации работы моего варианта gen_bin_tre.
    left_branch = root * 4
    right_branch = root + 1
    """
    gen_bin_tree(4, 4, lambda x: x * 4, lambda y: y + 1)
    print(gen_bin_tree(4, 4, lambda x: x * 4, lambda y: y + 1))


if __name__ == "__main__":
    main()
