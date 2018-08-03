# -*- coding: utf-8 -*-

""" Created on 4:49 PM 7/17/18
    @author: ngunhuconchocon
    @brief: provide api for calling chunking
"""

from __future__ import print_function
import sys
import os
import time
import pickle
import logging

from features.features import chunking_sent2features
import time


def chunk_tag(pos_tags, chunk_crf_model):
    """
    Perform chunking
    :param pos_tags: segmentated and tagged sentence
    :param chunk_crf_model: notunderthesea :D
    :return:
    """
    return _chunk_tag(pos_tags, chunk_crf_model)


def _chunk_tag(pos_tags, chunk_crf_model):
    # print("=== chunk ===")

    start = time.time()
    X_test = [chunking_sent2features(pos_tags, 'test')]
    tag_chunk = chunk_crf_model.predict(X_test)  # , format)
    result = [(pos_tags[ii][0], pos_tags[ii][1], tag_chunk[0][ii]) for ii in range(len(tag_chunk[0]))]

    # print(result)
    print("Executed time for chunking: " + str(time.time() - start))
    # print("=============")

    # for (word, tag, chunk) in result:
    #     print(word + "\t" + tag + "\t" + chunk)

    return result


if __name__ == "__main__":
    chunk_model_name = "chunk.pkl"
    ws_model_name = "ws_july_4.pkl"
    pos_model_name = "pos_0.pkl"

    curr_dir = os.path.abspath(os.path.dirname(__file__))
    print(curr_dir)
    models_dir = os.path.join(curr_dir, "models/")
    print(models_dir)

    ws_model = pickle.load(open(models_dir + ws_model_name, "rb"))
    pos_model = pickle.load(open(models_dir + pos_model_name, "rb"))
    chunk_model = pickle.load(open(models_dir + chunk_model_name, "rb"))

    text = "Các bạn hoàng tử vs công chúa, T là vua thì ai nhận là hoàng hâu đây?"
    ws_text =
    print(chunk_tag("Các bạn hoàng tử vs công chúa, T là vua thì ai nhận là hoàng hâu đây?", ws_model))