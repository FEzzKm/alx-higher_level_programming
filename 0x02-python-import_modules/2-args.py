#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = len(sys.argv) - 1
    if a == 0:
        print("0 arguments.")
    elif a == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
