#!/usr/bin/python3
def element_at(my_list, idx):
    if idx in my_list:
       if idx < 0:
            return None
       else:
            return idx
