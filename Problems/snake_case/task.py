word = input()

for letter in word:
    if letter.isupper():
        word = word.replace(letter, '_' + letter.lower())
        # print(word)
        # letters = "_" + letters.lower()

print(word)