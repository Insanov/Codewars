def spin_words(sentence):
    return ' '.join(list(map(lambda x: x[::-1], sentence.split(' '))))


sentence = "his sentence is a sentence"
print(spin_words(sentence))
