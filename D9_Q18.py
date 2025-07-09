def split_words_by_starting_letter(words):
    vowels = "aeiouAEIOU"
    vowel_words = [word for word in words if word[0] in vowels]
    consonant_words = [word for word in words if word[0] not in vowels]
    return vowel_words, consonant_words
