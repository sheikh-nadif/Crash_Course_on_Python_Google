def count_letters(text):
    result ={}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1

    return result

print(count_letters("aaaaaa")) # Should be {'a':5}
print(count_letters("Hello World")) #Should be {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}
print(count_letters("banana")) # Should be {'b':1, 'a':3, 'n':2}
        