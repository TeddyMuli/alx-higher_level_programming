#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            x = my_list_1[i]
            y = my_list_2[i]
            if isinstance(x, (int, float)) and isinstance(y, (int, float)):
                if (y == 0):
                    raise ZeroDivisionError
                result.append(x / y)
            else:
                raise TypeError
        except IndexError:
            print("out of range")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        finally:
            pass
    return result
