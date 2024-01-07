#!/usr/bin/python3
"""function replaces element in list in specific position wo modifying original list"""


def new_in_list(my_list, idx, element):
    l = len(my_list)

    copy_list = my_list[:]

    if 0 <= idx < l:
        copy_list[idx] = element

    return (copy_list)
