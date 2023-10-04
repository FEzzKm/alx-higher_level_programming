#!/usr/bin/python3
for a in range(100):
    if a == 99:
        print("{:02}".format(a))
    else:
        print("{:02}".format(a), end=', ')
