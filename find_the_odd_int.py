def find_it(seq):
    for elem in seq:
        if seq.count(elem) % 2 == 1:
            return elem


seq = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
print(find_it(seq))
