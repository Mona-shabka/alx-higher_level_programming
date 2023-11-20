#!/usr/bin/python3
def magic_calculation(a, b):
    r = 0
    for m in range(1, 3):
        try:
            if m > a:
                raise Exception('Too far')
            r += (a ** b) / m
        except Exception:
            r = b + a
            break
    return (r)
