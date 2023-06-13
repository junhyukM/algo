word = input()

if word.isupper():
    word_l = word.lower()
    print(f'{word}(ASCII: {ord(word)}) => {word_l}(ASCII: {ord(word_l)})')
elif word.islower():
    word_u = word.upper()
    print(f'{word}(ASCII: {ord(word)}) => {word_u}(ASCII: {ord(word_u)})')
else:
    print(word)        