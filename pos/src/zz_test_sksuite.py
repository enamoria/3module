# -*- coding: utf-8 -*-

from __future__ import print_function

import pickle
import os
import sys

if sys.version_info[0] < 3:
    from itertools import izip as zip
else:
    import zip

sys.path.extend([os.path.dirname(os.path.dirname(__file__)), os.path.dirname(__file__)])

from features.features import sent2features
from IO.reader import Reader


def sent2labels(sent):
    return [y[1] for y in sent]


def sent2tokens(sent):
    return [y[0] for y in sent]


if __name__ == "__main__":
    reader = Reader("/data/test")
    test_sents = reader.read('10000')

    print(test_sents[1])
    MODEL_NAME = "pos_8.pkl"

    X_test = [sent2features(sent, 'test') for sent in test_sents if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]
    y_test = [sent2labels(sent) for sent in test_sents if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]

    loaded_model = pickle.load(open(MODEL_NAME.replace(".pkl", "") + ".pkl", 'rb'))
    print("Loaded", MODEL_NAME, loaded_model)
    print(loaded_model.classes_)

    sum = 0.0

    y_pred = loaded_model.predict(X_test)
    print(y_pred)
    print([[str(yi) for yi in y] for y in y_test])
    print(loaded_model.score(X_test, y_test))

    # for (pred, true) in zip(y_pred, y_test):
    #     match = 0
    #     for i in range(len(pred)):
    #         if pred[i] == true[i]:
    #             match += 1
    #
    #     if match/float(len(pred)) < 0.9:
    #         print("===================")
    #         print(match/float(len(pred)))
    #         print(pred)
    #         print([str(x) for x in true])
    #         raw_input("Wait ......................")

    # for test_sent in test_sents:
    #     true = [yy for yy in sent2labels(test_sent)]
    #     print(true)
    #     sent_feat = sent2features(test_sent, 'test')
    #
    #     tmp_pred = loaded_model.predict(sent_feat)
    #     print(tmp_pred)
    #
    #     pred = [yy_pred for yy_pred in tmp_pred]
    #
    #     if len(true) != len(pred):
    #         input("Length is difference:", test_sent)
    #         exit()
    #
    #     count = 0.0
    #     for xxx in range(len(pred)):
    #         if true[xxx] == pred[xxx]:
    #             count += 1
    #
    #     # print(test_sent)
    #     # print(sent2labels(test_sent))
    #     # print(tagger.tag(sent2features(test_sent, mode='test')))
    #
    #     if count/len(pred) < 0.7:
    #         # print(true)
    #         # print(pred)
    #         # print(sent2tokens(test_sent))
    #         print(count / len(pred))
    #         sum += count / len(pred)
    #         input("..")
    #
    #     # print(count / len(pred))
    #     # sum += count / len(pred)
    #     # input("..")
    #
    #         # input("..")
    #
    # print("Avg acc:", sum/len(test_sents))
