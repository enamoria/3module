"""
    This script specify some feature function for CRF
"""

import sys
import os

sys.path.append(os.path.dirname(__file__))

from CONSTANT import punctuations_and_symbols


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
    if s.split("_") > 1 and s.istitle():
        return True
    return False

    # raise NotImplementedError


# EDITED IN 13 Jul 2018: Add dictionary
def isInDict(word):

    raise NotImplementedError
