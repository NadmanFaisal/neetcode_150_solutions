def twoSum(nums: list[int], target: int) -> list[int]:
    hash_map = {}
    for i in range(0, len(nums)):
        suspect = target - nums[i]
        if suspect in hash_map:
            return [hash_map[suspect], i]
        else:
            hash_map[nums[i]] = i



nums = [5, 4, 6]
target = 10

print(twoSum(nums, target))
