# -*- coding: utf-8 -*-

""" Created on 4:26 PM 7/16/18
    @author: ngunhuconchocon
    @brief:
"""

from __future__ import print_function
import time

import pickle
import logging
import os

from features.features import sent2features
from regex_tokenize import tokenize


def word_seg(text, word_seg_crf_model):
    """
    Perform word segmentation
    :param text: input, raw
    :param word_seg_crf_model: notunderthesea :D
    :return: list[segmentated words]
    """
    return _word_seg(text, word_seg_crf_model)


def _word_seg(text, word_seg_crf_model):
    sentence = tokenize(text).split()
    X_test = [sent2features(sentence, 'test')]

    # logging.info("  Instance model")
    # crf_model = CRFModel.Instance()
    # logging.info("  Predict")

    start = time.time()
    IOBtag = word_seg_crf_model.predict(X_test)
    # print("Executed time for segmentating: " + str(time.time() - start))

    # logging.info("  tokenize output")
    # tokens = [token[0] for token in output[0]]
    # tags = [token[1] for token in output[0]]

    output = []
    # for tag, token in zip(tags, tokens):
    for tag, token in zip(IOBtag[0], sentence):
        if tag == "I-W":
            output[-1] = output[-1] + u" " + token
        else:
            output.append(token)

    # if format == "text":
    #     output = u" ".join([item.replace(" ", "_") for item in output])

    return output


if __name__ == "__main__":
    ws_model = "ws_july_3.pkl"
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    print(curr_dir)
    models_dir = os.path.join(curr_dir, "models/")
    print(models_dir)
    ws_model = pickle.load(open(models_dir + ws_model, 'rb'))

    print(word_seg("Các bạn hoàng tử vs công chúa, T là vua thì ai nhận là hoàng hâu đây?", ws_model))