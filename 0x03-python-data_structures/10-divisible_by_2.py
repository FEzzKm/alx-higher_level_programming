#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ a function that finds all multiples of 2 in a list"""
    m = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            m.append(True)
        else:
            m.append(False)

    return (m)