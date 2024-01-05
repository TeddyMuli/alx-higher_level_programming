#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    index = 0
    while count < x:
        try:
            item = my_list[index]
            if isinstance(item, int):
                print("{:d}".format(item), end='')
                count += 1
            index += 1
        except IndexError:
            break
    print()  # print a newline after the integers
    return count