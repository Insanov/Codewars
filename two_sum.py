def two_sum(numbers, target):
    extra_list = []
    for index, elem in enumerate(numbers):
        sec_index = extra_list.index(elem) if elem in extra_list else -1
        extra_list.append(target - elem)
        print(index, sec_index, extra_list)
        if sec_index > -1:
            return (index, sec_index)


numbers = [1, 2, 3]
target = 4
two_sum(numbers, target)
