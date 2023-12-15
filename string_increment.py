def increment_string(string):
    for index, sym in enumerate(string[::-1]):
        print(index, string[index])
        print(sym.isdigit())

    return string



print(increment_string("foo123456"))
