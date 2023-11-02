#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    for m in range(len(sys.argv) - 1):
        total += int(sys.argv[m + 1])
    print(total)
