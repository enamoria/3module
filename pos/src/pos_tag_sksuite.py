# -*- coding: utf-8 -*-

""" Created on 5:41 PM 7/16/18
    @author: ngunhuconchocon
    @brief:
"""

from __future__ import print_function

import argparse
import pickle
import os
import sys

from sklearn_crfsuite import CRF

sys.path.extend([os.path.dirname(os.path.dirname(__file__)), os.path.dirname(__file__)])

from features.features import sent2features
from IO.reader import Reader

MODEL_NAME = 'CH_label_punctuation.pkl'


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


def parse_argument():
    # TODO NEED TO BE REFINE: THIS IS COPIED FROM CHUNKING
    """
    Parse argument from commandline:
        Required arguments:

        Optional arguments:
            -m --model      :   Name of the model (will be saved on disk). Default pos.pkl (add indices if duplicated)
            -i --iter       :   Max iteration for optimization. Default 300
            -e --epsilon    :   epsilon - stopping criteria. Default 1e-5
    :return: args: args list.
    """

    parser = argparse.ArgumentParser(description="POS-tagging trainer")

    parser.add_argument("-m", metavar="model", required=True, type=unicode, default="ws",
                        help="Name of the model (will be saved on disk). Default pos.pkl (indexed if duplicated)")

    parser.add_argument("-i", metavar="iter", type=int, default=300, help="Max iteration for optimization. Default 300")
    parser.add_argument("-d", metavar="delta", type=float, default=1e-5, help="stopping criteria. Default 1e-5")

    return parser.parse_args()


def sent2labels(sent):
    return [y[1] for y in sent]


def sent2token(sent):
    return [y[0] for y in sent]


if __name__ == "__main__":
    args = parse_argument()

    # Model name, duplication check
    MODEL_NAME = checkModelFileExistAndCreateNewModelName(args.m.replace(".pkl", "") + ".pkl")

    reader = Reader("/data/train")
    reader_test = Reader("/data/test")

    test_sents = reader_test.read('10000')  # 10000 is the dataset
    train_sents = reader.read('10000')  # 10000 is the dataset

    X_train = [sent2features(sent, "train") for sent in train_sents if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]
    y_train = [sent2labels(sent) for sent in train_sents if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]

    X_test = [sent2features(sent, "test") for sent in test_sents if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]
    y_test = [sent2labels(sent) for sent in test_sents if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]

    # X_test = [sent2features(sent) for sent in test_sents]
    # y_test = [sent2labels(sent) for sent in test_sents]

    print("=======================================")
    print("Start training ...")
    # model = CRF(c1=0.5, c2=0.005, verbose=True, max_iterations=500)

    model = CRF(algorithm="lbfgs",
                c1=0.1, c2=0.002,
                max_iterations=3000,
                all_possible_states=True,
                all_possible_transitions=True,
                period=30,
                # calibration_eta=0.1,
                # calibration_rate=1.5,
                # calibration_samples=100,
                # calibration_max_trials=50,
                verbose=True)

    model.fit(X=X_train, y=y_train)
    print("Done training !")

    print("=======================================")
    print("Saving model ...")
    pickle.dump(model, open(MODEL_NAME, 'wb'), protocol=2)
    print("Done saving model! Model is saved to", MODEL_NAME)

    print("=======================================")
    # print("Testing ...")
    #
    # model = pickle.load(open(MODEL_NAME, 'rb'))  # , protocol=2)
    #
    # score = model.score(X_test, y_test)
    # y_pred = model.predict(X_test)
    # y_true = y_test
    #
    # print(y_pred)
    # print(y_test)
    # sum = 0
    # for i in range(len(y_pred)):
    #     count = 0
    #
    #     for j in range(len(y_pred[i])):
    #         if y_pred[i][j] == y_true[i][j]:
    #             count += 1
    #     print(count/float(len(y_pred[i])))
    #     sum += count/float(len(y_pred[i]))
    # print("Avg:", sum/len(y_pred))
    #
    # print(score)
    # print("Done testing !")

    # trainer.set_params({
    #     # 'c1': 1e-5,  # Coeff for L1 penalty
    #     'c2': 1e-3,  # Coeff for L2 penalty
    #     'max_iterations': 100,
    #
    #     # # include transitions that are possible, but not observed
    #     'feature.possible_transitions': True
    # })
    #
    # print("=====================")`
    # print("Start training ...")
    # trainer.params()
    #
    # trainer.train(MODEL_NAME)
    # print("Done training!")
    #
    # # tagger = pycrfsuite.Tagger().open('xxxxx')
    # #
    # # for test_sent in test_sents:
    # #     print(" ".join(sent2token(test_sents)))
    # #     print(tagger.tag(sent2features(test_sents)))
