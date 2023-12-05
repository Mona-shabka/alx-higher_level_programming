#!/usr/bin/python3
"""file-appending function."""


def append_write(filename="", text=""):
    """Appends with a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
