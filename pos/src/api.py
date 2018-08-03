# -*- coding: utf-8 -*-

""" Created on 5:41 PM 7/16/18
    @author: ngunhuconchocon
    @brief:
"""

from __future__ import print_function

import os
import pickle
import time


def pos_tag(word_seg, pos_crf_model):
    """
    Perform part of speech tagging
    :param word_seg: segmentatted sentence
    :param pos_crf_model: notunderthesea :D
    :return:
    """
    return _pos_tag(word_seg, pos_crf_model)


def _pos_tag(word_seg, pos_crf_model):
    # print("=== pos-tag ===")

    start = time.time()
    X_test = [postag_sent2features(word_seg, 'test')]

    # result = pos_crf_model.predict(word_seg)  # , format)
    tags = pos_crf_model.predict(X_test)  # , format)
    result = [(word_seg[ii], tags[0][ii]) for ii in range(len(word_seg))]
    # print(result)
    # print("Executed time for tagging: " + str(time.time() - start))
    return result