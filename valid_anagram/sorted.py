def isAnagram(s: str, t: str) -> bool:
    val1 = sorted(s)
    val2 = sorted(t)
    if val1 == val2:
        return True
    else:
        return False

s = "racecar"
t = "carrace"

print(s)
print(t)

print(isAnagram(s, t))
