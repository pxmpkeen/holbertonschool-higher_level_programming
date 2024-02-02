#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    rest = []
    for i in range(0, list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            rest.append(res)
    return rest
