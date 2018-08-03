# -*- coding: utf-8 -*-
from __future__ import print_function

import os
from CONSTANT import WORD_BEGIN, WORD_INSIDE

B_W = WORD_BEGIN
I_W = WORD_INSIDE


def checkModelFileExistAndCreateNewModelName(name):
    i = 0
    tmp = name
    while os.path.isfile(tmp):
        # tmp = name + "_" + str(i)
        tmp = name.replace(".pkl", "_" + str(i) + ".pkl")
        i += 1

    if tmp != name:
        print(name, "is exist. Output file renamed to", tmp)
    else:
        print(name, "is available")
    return tmp


def sent2labels(sent):
    return [y[1] for y in sent]


def sent2token(sent):
    return [y[0] for y in sent]


def list_to_sentence(sent):
    tmp = ""
    for i, word in enumerate(sent):
        if i == len(sent) - 1:
            tmp += word[0]
        else:
            if word[1] == B_W:
                if sent[i+1][1] != I_W: # B_W or O
                    tmp += word[0] + " "
                else:
                    tmp += word[0] + "_"
            elif word[1] == I_W:
                if sent[i+1][1] != I_W: # B_W or O
                    tmp += word[0] + " "
                else:
                    tmp += word[0] + "_"
            else:
                tmp += word[0] + " "

    return tmp

if __name__ == "__main__":
    sent = [['Không', 'B-W'], ['chỉ', 'B-W'], ['nước', 'B-W'], ['mắt', 'I-W'], [',', 'B-W'], ['mồ', 'B-W'], ['hôi', 'I-W'], ['và', 'B-W'], ['máu', 'B-W'], ['của', 'B-W'], ['các', 'B-W'], ['thuyền', 'B-W'], ['viên', 'I-W'], ['đổ', 'B-W'], ['trên', 'B-W'], ['sàn', 'B-W'], ['tàu', 'B-W'], [',', 'B-W'], ['họ', 'B-W'], ['đã', 'B-W'], ['phải', 'B-W'], ['trả', 'B-W'], ['giá', 'I-W'], ['cho', 'B-W'], ['cuộc', 'B-W'], ['“', 'B-W'], ['thoát', 'B-W'], ['nghèo', 'B-W'], ['”', 'B-W'], ['bằng', 'B-W'], ['chính', 'B-W'], ['tính', 'B-W'], ['mạng', 'I-W'], ['của', 'B-W'], ['mình', 'B-W'], ['.', 'B-W']]
    print(list_to_sentence(sent))
