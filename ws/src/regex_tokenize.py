# -*- coding: utf-8 -*-
import re
import sys
import unicodedata

# from underthesea.feature_engineering.text import Text


def Text(text):
    """ provide a wrapper for python string
    map byte to str (python 3)
    map str to unicode (python 2)
    all string in utf-8 encoding
    normalize string to NFC
    """
    if not is_unicode(text):
       text = text.decode("utf-8")
    text = unicodedata.normalize("NFC", text)
    return text


def is_unicode(text):
    if sys.version_info >= (3, 0):
        unicode_type = str
    else:
        unicode_type = unicode
    return type(text) == unicode_type


def tokenize(text):
    """
    tokenize text for word segmentation

    :param text: raw text input
    :return: tokenize text
    """
    # print(type(text))
    # print(type(text))

    text = Text(text)
    specials = ["==>", "->", "\.\.\.", ">>"]
    digit = "\d+([\.,_]\d+)+"
    email = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    web = "^(http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
    datetime = [
        "\d{1,2}\/\d{1,2}(\/\d+)?",
        "\d{1,2}-\d{1,2}(-\d+)?",
    ]
    word = "\w+"
    non_word = "[^\w\s]"
    abbreviations = [
        "[A-ZĐ]+\.",
        "Tp\.",
        "Mr\.", "Mrs\.", "Ms\.",
        "Dr\.", "ThS\."
    ]

    patterns = []
    patterns.extend(abbreviations)
    patterns.extend(specials)
    patterns.extend([web, email])
    patterns.extend(datetime)
    patterns.extend([digit, non_word, word])

    patterns = "(" + "|".join(patterns) + ")"
    if sys.version_info < (3, 0):
        patterns = patterns.decode('utf-8')
    tokens = re.findall(patterns, text, re.UNICODE)
    return u" ".join(["%s" % token[0] for token in tokens])


if __name__ == "__main__":
    xxx = "Mr.PhanHuyKinh 30-04-1975@gmail.com  dmm"
    print(tokenize(xxx))
