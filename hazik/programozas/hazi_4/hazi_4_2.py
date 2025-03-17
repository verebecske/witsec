def alphabetic_value(word: str) -> int:
    word = word.lower()
    value = 0
    for letter in word:
        value += ord(letter) - 96
    return value

print(alphabetic_value("ac"))