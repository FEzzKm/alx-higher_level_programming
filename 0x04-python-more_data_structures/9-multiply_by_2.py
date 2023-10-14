#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    td = a_dictionary.copy()
    for x in td.keys():
        td[x] *= 2
    return (td)
