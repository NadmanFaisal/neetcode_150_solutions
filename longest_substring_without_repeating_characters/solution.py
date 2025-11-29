def lengthOfLongestSubstring(s: str) -> int:
    lP = 0
    char_set = set()
    res = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[lP])
            lP += 1
        char_set.add(s[r])
        res = max(res, r - lP + 1)
    return res

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
