#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    m_list = []
    for m in my_list:
        if m % 2 == 0:
            m_list.append(True)
        else:
            m_list.append(False)
    return (m_list)
