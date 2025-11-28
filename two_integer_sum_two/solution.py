def twoSum(numbers: list[int], target: int) -> list[list[int]]:
    lP = 0
    rP = len(numbers) - 1
    while (lP <= rP):
        sum = numbers[lP] + numbers[rP]
        if sum > target:
            rP -= 1
        elif sum < target:
            lP += 1
        else:
            return [lP + 1, rP + 1]

nums = [1, 2,3,4]
target = 3
print(twoSum(nums, target))
