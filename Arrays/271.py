def encode(strs):
    """Encodes a list of strings to a single string."""

    result = ""
    for s in strs:
        result += str(len(s)) + "#" + s
    return result


def decode(s):
    """Decodes a single string to a list of strings."""
    result = []
    l = 0
    length = ""
    while l < len(s):
        if s[l] == "#":
            result.append(s[l + 1 : l + int(length) + 1])
            l += int(length)
            length = ""
        else:
            length += s[l]

        l += 1

    return result


print(decode("11#hello world5#world"))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
