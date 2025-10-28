def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if len(nums)==0:
        return ValueError

    maxi_el=-10**10
    mini_el=10**10

    for i in range(len(nums)):
        if nums[i] > maxi_el:
            maxi = nums[i]
        if nums[i] < mini_el:
            mini = nums[i]

    return (mini, maxi)

    