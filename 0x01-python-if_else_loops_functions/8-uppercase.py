#!/usr/bin/python3
def uppercase(str):
    uppercase = ""
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            uppercase += chr(ord(i) - 32)
        else:
            uppercase += i
    print("{:s}".format(uppercase))
