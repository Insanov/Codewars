def generate_hashtag(s):
    words_list = [word for word in s.split(' ') if word]
    return '#' + ''.join(words_list)


s = " Hello there thanks for       trying my        Kata     "
print(generate_hashtag(s))
