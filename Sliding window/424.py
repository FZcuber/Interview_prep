def characterReplacement(s, k):
    if len(s) == 1:
        return 1

    l, result = 0, 1
    freq_table = {}
    max_freq = 0

    for r in range(len(s)):

        freq_table[s[r]] = freq_table.get(s[r], 0) + 1

        max_freq = max(freq_table.values())

        if (r - l + 1) - max_freq > k:
            freq_table[s[l]] -= 1
            l += 1

        result = max(result, r - l + 1)

    return result


print(characterReplacement("ABAA", 0))
