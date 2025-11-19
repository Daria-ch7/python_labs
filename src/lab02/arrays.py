def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """принимаем список, содержащий целые числа или числа с плавающей точкой; возвращаем кортеж из двух чисел (целых/с плав. точкой)"""

    if len(nums) == 0:
        return ValueError

    maxi_el = -(10**10)
    mini_el = 10**10

    for i in range(len(nums)):
        if nums[i] > maxi_el:
            maxi = nums[i]
        if nums[i] < mini_el:
            mini = nums[i]

    return (mini, maxi)


print(min_max([-5, -2, -9]))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """принимаем список, содержащий целые числа или числа с плавающей точкой; возвращаем список, содержащий числа (целые/с плав. точкой)"""

    if len(nums) == 0:
        return ValueError

    return sorted(set(nums))


"""сначала создаем список уникальных значений, потом сортируем его"""

print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))


def flatten(mat: list[list | tuple]) -> list:
    """принимаем список, содержащий целые числа или числа с плавающей точкой; возвращаем список"""
    itog_list = []
    for element in mat:
        if isinstance(element, (list, tuple)):
            """проверяю, что эл-т из списка действительно является списком/кортежем"""
            for member in element:
                """добавляю каждый эл-т списка/кортежа из принятого списка"""
                itog_list.append(member)
        else:
            return TypeError
        """если у меня эл-т в исходном списке не список/кортеж, то выдаем ошибку"""
    return itog_list


print(flatten(([1, 2], (3, 4, 5))))
