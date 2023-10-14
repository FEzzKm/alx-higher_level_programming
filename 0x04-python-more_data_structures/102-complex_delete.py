#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    kd = []
    for k in a_dictionary:
        if a_dictionary[k] == value:
            kd.append(k)
    for k in kd:
        del a_dictionary[k]
    return a_dictionary
