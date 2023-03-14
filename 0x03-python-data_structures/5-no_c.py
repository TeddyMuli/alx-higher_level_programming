#!/usr/bin/python3
def no_c(my_string):
    output =""
    for char in my_string:
        if char not in ['c', 'C']:
            output += char
    return output