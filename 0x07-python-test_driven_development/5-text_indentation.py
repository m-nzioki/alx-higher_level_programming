#!/usr/bin/python3

"""Defines a text-identation function"""


def text_identation(text):
    """Prints text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text(str): input text
    Raises:
        TypeError if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    split_text = []
    for char in text:
        if char in ['.', '?', ':']:
            split_text.append('\n\n')
        else:
            split_text.append(char)

        print(''.join(split_text).strip())
