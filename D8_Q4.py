def char_frequency(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0) + 1
    return freq

print(char_frequency("banana"))




