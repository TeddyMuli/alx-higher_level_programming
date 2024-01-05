#!/usr/bin/python3

def safe_print_division(a, b):
    c = 0
    try:
        if (b != 0):
            c = a / b
        else:
            c = None
        
        return c
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(c))

