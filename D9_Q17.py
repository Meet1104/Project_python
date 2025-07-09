def split_vowels(s):
    vowels = "aeiouAEIOU"
    v = ''.join([c for c in s if c in vowels])
    c = ''.join([c for c in s if c not in vowels])
    return v, c
