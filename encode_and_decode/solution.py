def encode(strs: list[str]) -> str:
    res = ""
    for str in strs:
        res += str + "#"
    return res


def decode(s: str) -> list[str]:
    output = []
    word = ""
    for i in range(len(s)):
        if s[i] == '#':
            output.append(word)
            word = ""
        else:
            word += s[i]
    return output



input = ["we","say",":","yes","!@#$%^&*()"]
encoded_input = encode(input)
decoded_input = decode(encoded_input)

print("Encode: ", encoded_input)
print("Decoded: ", decoded_input)
