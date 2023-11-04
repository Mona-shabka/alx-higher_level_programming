#!/usr/bin/python3
def no_c(my_string):
    m = ""
    for n in range(len(my_string)):
        if n != 'c' and n != 'C':
            m += n
    return (m)
