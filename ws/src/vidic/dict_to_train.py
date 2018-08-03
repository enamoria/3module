# -*- coding: utf-8 -*-

""" Created on 10:11 AM 8/1/18
    @author: ngunhuconchocon
    @brief:
"""

from __future__ import print_function
import os

try:
    range=xrange
except NameError:
    pass


def read_data(filepath):
    """
    Return the sentence set read from filepath (ConLL format)
    :param filepath: path of the text file in ConLL format
    :return: a list of sentences with each word ws tag
    """
    words = []
    with open(filepath, "r") as f:
        raw_data = f.read().strip("\n").strip(" ").split("\n")
        for word in raw_data:
            word_part = [[part, "I_W"] for part in word.split(" ")]
            if len(word_part) == 2:
                word_part[0][1] = "B_W"
                words.append(word_part)
                # words.append([xxx.replace("B-W", "B_W").replace("I-W", "I_W").replace("o", "O").split("\t") for xxx in sent.split("\n")])

    return words


def dict_to_conll(word_list):
    with open("dict_conll", "w") as f:
        for word in word_list:
            for word_part in word:
                f.write(word_part[0] + "\t" + word_part[1] + "\n")
            f.write("\n")


if __name__ == "__main__":
    words = read_data(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Viet39K.txt"))
    dict_to_conll(words)
    print(len(words))
    print(words[8000])
    print(" ".join([x[0].decode("utf8") for x in words[8000]]))
