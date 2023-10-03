#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """Return the text indented.
    
    Args:
        text (str): The text to indent.
    Raises:
        TypeError: If text is not a string.
    Return:
        The text indented.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    alpha = 0
    while alpha < len(text) and text[alpha] == ' ':
        alpha += 1
    while alpha < len(text):
        print(text[alpha], end="")
        if text [alpha] == '\n' or text[alpha] == '?' or text[alpha] == '.' or text[alpha] == ':':
            print('\n')
            alpha += 1
            while alpha < len(text) and text[alpha] == " ":
                alpha += 1
            continue
        alpha += 1
