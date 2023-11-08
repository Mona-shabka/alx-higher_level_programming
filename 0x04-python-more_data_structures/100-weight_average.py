#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    else:
        return (sum(m * n for m, n in my_list) / sum(n for m, n in my_list))
