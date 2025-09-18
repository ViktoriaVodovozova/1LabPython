def sum_two(nums, target):
    if len(nums) == 0:
        raise TypeError("Пусто")
    if target == 0:
        raise TypeError("Таргет равен нулю")
    if int(target) != target:
        raise TypeError("Таргет - нецелое число")
    if str(target) == target:
        raise TypeError("Таргет - строчное число")
    for x in nums:
        if int(x) != x:
            raise TypeError("В списке есть нецелое число")
        if str(x) == x:
            raise TypeError("В списке есть строка")
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)): 
            if nums[i] + nums[j] == target:
                res.append([i, j])
                return res[0] # берем только пару с наименьшими индексами
    return None


