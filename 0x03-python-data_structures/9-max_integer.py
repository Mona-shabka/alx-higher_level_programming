#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    m_list = my_list.copy()
    m_list.sort()
    return (m_list[-1])
