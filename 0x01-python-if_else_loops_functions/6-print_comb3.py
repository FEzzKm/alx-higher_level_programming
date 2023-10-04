#!/usr/bin/python3
for a in range(9):
    if a == 8:
        print(89)
    else:
        for n in range(a+1, 10):
        print(f"{a}{n}", end=', ')
