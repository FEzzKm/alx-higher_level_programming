#!/usr/bin/python3
"""
    5-text_indentation Module
"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after each of this characters
        '.', '?', ':'

        Args:
            text: inital string to work on
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    stl = list()
    nt = list()
    letters_list = list()

    for character in text:
        letters_list.append(character)
        if character in ['.', '?', ':']:
            stl.append(''.join(letters_list))
            letters_list.clear()

    if letters_list:
        stl.append("".join(letters_list))
    letters_list.clear()

    for sentence in stl:
        nt.append(sentence.strip(' '))
    stl.clear()

    for character in nt[-1]:
        if character in ['.', '?', ':']:
            print("\n\n".join(nt))
            print()
            return

    print("\n\n".join(nt), end='')
