#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    co, m = 0, 0
    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end="")
            co += 1
        except (ValueError, TypeError):
            pass
    print()
    return (co)
