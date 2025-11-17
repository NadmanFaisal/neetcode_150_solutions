def encode(strs: list[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(s: str) -> list[str]:
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j

    return res



input = ["we","say",":","yes","!@#$%^&*()"]
encoded_input = encode(input)
decoded_input = decode(encoded_input)

print("Encode: ", encoded_input)
print("Decoded: ", decoded_input)
