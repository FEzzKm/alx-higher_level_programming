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

    STL = list()
    NT = list()
    letters_list = list()

    for character in text:
        letters_list.append(character)
        if character in ['.', '?', ':']:
            STL.append(''.join(letters_list))
            letters_list.clear()

    if letters_list:
        STL.append("".join(letters_list))
    letters_list.clear()

    for sentence in STL:
        NT.append(sentence.strip(' '))
    STL.clear()

    for character in NT[-1]:
        if character in ['.', '?', ':']:
            print("\n\n".join(NT))
            print()
            return

    print("\n\n".join(NT), end='')
