def sum_dig_pow(a, b):
    ret_list = []
    for num in range(a, b):
        tmp_num = num
        offset = 1
        while num > 10:
            print(num)
            num_len = len(str(num))
            print(num_len)
            digit = int(str(tmp_num)[num_len - offset])
            print(digit)
            bench = digit ** num_len
            print(bench)
            if num < bench:
                break
            num = num // 10 ** (num_len - 1) if bench == 0 else num - bench
            offset += 1
        print(num, tmp_num)
        print('\n')
        if str(tmp_num).startswith(str(num)):
            ret_list.append(tmp_num)
        # break
    return ret_list


print(sum_dig_pow(11, 100))
