def hasDuplicate(nums: list[int]) -> bool:
    vals = set()
    for num in nums:
        if num in vals:
            return True
        else:
            vals.add(num)

nums = [1, 2, 2, 3, 4]
print(hasDuplicate(nums))
