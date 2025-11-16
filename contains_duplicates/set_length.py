def hasDuplicate(nums: list[int]) -> bool:
    return len(set(nums)) < len(nums)

nums = [1, 2, 2, 3, 4]
print(hasDuplicate(nums))
