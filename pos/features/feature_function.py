"""
    This script specify some feature function for CRF
"""
from __future__ import print_function

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.CONSTANT import punctuations_and_symbols


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def isPunc(s):
    if s in punctuations_and_symbols:
        return True
    return False


def isDate(s):
    raise NotImplementedError


def isNp(s):
    # TODO Need a dicktionary here
    if s.split("_") > 1 and s.istitle():  # Word with more than 2 syllables and istitle are highly probable to be a Np
        return True
    return False

    # raise NotImplementedError


# ADDED IN 13 Jul 2018: Add dictionary
# This dict is necessary for ws only
# def isInDict(word):
#     # A singleton is used
#     dict = Dictionary.Instance()
#     # xxx = dict.lookup(word)
#     return dict.lookup(word)
#
#     # raise NotImplementedError


if __name__ == "__main__":
    word = "Phan huy"
    print(word.istitle())
    print(isNp(word))
