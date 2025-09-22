def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        return ValueError

    maxi=-10**10
    mini=10**10

    for i in range(len(nums)):
        if nums[i] > maxi:
            maxi = nums[i]
        if nums[i] < mini:
            mini = nums[i]

    return (mini, maxi)
nums=[-5, -2, -9]


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    itog=[]
    for element in mat:
        if isinstance(element,(list,tuple)):
            for member in element:
                itog.append(member)
        else:
            return TypeError
    return itog
print(flatten(([1, 2], (3, 4, 5))))


