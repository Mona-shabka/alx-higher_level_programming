#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for m in range(0, list_length):
        try:
            d = my_list_1[m] / my_list_2[m]
        except TypeError:
            print("wrong type")
            d = 0
        except ZeroDivisionError:
            print("division by 0")
            d = 0
        except IndexError:
            print("out of range")
            d = 0
        finally:
            new_list.append(d)
    return (new_list)
