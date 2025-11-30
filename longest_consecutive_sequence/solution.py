def longestConsecutive(nums: list[int]) -> int:
    set_nums = set(nums)
    longest = 0

    for num in nums:
        if num in set_nums:
            if (num - 1) not in set_nums:
                length = 0
                while (num + length) in nums:
                    length += 1
                longest = max(length, longest)
    return longest

nums = [2,20,4,10,3,4,5]
print(longestConsecutive(nums))
