#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counts = len(sys.argv) - 1
    if counts == 0:
        print("0 arguments.")
    elif counts == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(counts))
    for m in range(counts):
        print("{}: {}".format(m + 1, sys.argv[m + 1]))
