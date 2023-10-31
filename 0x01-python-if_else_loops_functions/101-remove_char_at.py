#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    for m, i in enumerate(str):
        if m != n:
            new_string += i
        return new_string
