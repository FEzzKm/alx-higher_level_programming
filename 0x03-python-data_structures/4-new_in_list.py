#!/usr/bin/python3
"""replace element in a list without modify the original list"""


def new_in_list(my_list, idx, element):
    l = len(my_list)

    cp_list = my_list[:]

    if 0 <= idx < l:
        cp_list[idx] = element

    return(cp_list)
