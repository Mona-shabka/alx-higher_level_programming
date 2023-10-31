#!/usr/bin/python3
for n in range(25, -1, -1):
    m = n + ord('A')
    if n % 2 == 1:
        m += 32
    print("{:c}".format(m), end="")
