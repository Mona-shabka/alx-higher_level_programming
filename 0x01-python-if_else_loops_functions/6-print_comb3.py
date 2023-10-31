#!/usr/bin/python3
for n in range(10):
    for m in range(n, 10):
        if n < m:
            print("{:d}{:d}".format(n, m),
                  end="\n" if n == 8 and m == 9 else ", ")
