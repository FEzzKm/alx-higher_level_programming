#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    sys.argv.pop(0)
    a = len(sys.argv)

    if (a == 0):
        print("0 arguments.")
    elif (a == 1):
        print("1 argument:")
        print("{:d}: {}".format(len(sys.argv), sys.argv[0]))
    else:
        print("{:d} arguments:".format(a))
        number = 1
        for argument in sys.argv:
            print("{:d}: {}".format(number, argument))
            number += 1
