def topKFrequent(nums: list[int], k: int) -> list[int]:
    hash_map = {}
    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    arr = []
    for num, count in hash_map.items():
        arr.append([count, num])
    arr.sort()

    res = []
    while len(res) < k:
        res.append(arr.pop()[1])
    return res


nums = [1, 2, 2, 3, 3, 3]
k = 2
print(topKFrequent(nums, k))
