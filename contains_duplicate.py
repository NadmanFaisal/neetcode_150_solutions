def hasDuplicate(nums: list[int]) -> bool:
    hash_map = {}
    for num in nums:
        if num in hash_map.keys():
            return True
        else:
            hash_map[num] = 0
    return False
        

nums = [1, 2, 3, 4]
print(hasDuplicate(nums))
