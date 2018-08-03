# -*- coding: utf-8 -*-
from __future__ import print_function

import pickle
import argparse
from features.features import sent2features  # , train_word2features
from utils import *
from eval import segmentatedWordMatch, word_segmentation_accuracy

# MODEL_NAME = "ws_model.pkl_2"


def parse_argument():
    parser = argparse.ArgumentParser(description="Test a model")
    parser.add_argument("-n", metavar='NAME', type=str, help="Name of model which is going to be tested")
    return parser.parse_args()


if __name__ == "__main__":
    # parseArgument()
    # args = parse_argument()

    # MODEL_NAME = args.n + pkl
    MODEL_NAME = "ws.pkl"
    model_path = "./models/"
    print("=======================================")
    print("Reading testing data ....")
    test_sents = []
    filename_test = "test.txt"

    with open(filename_test, "r") as ftrue:
        raw_data = ftrue.read().strip("\n").strip(" ").split("\n\n")
        for sent in raw_data:
            test_sents.append([xxx.replace("B-W", "B_W").replace("I-W", "I_W").replace("o", "O").split("\t") for xxx in sent.split("\n")])

    X_test = [sent2features(sent, 'test') for sent in test_sents if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]
    y_test = [sent2labels(sent) for sent in test_sents if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]

    print("Done!")
    print("=======================================")
    print("Load the model ...")
    model = pickle.load(file=open(os.path.join(model_path, MODEL_NAME), "rb"))
    print(model)
    print("Done loading", MODEL_NAME)

    print("=======================================")
    print("Testing ...")
    score = model.score(X_test, y_test)
    y_pred = model.predict(X_test)

    sum_accuracy = 0
    for i, (y1, y2) in enumerate(zip(y_pred, y_test)):
        try:
            acc = segmentatedWordMatch(y1, y2) / float(y2.count(WORD_BEGIN) + y2.count("O"))  # B_W
            sum_accuracy += acc
        except ZeroDivisionError:
            print("y1", y1)
            print("y2", y2)

    total_words = sum([len(xxx) for xxx in test_sents])
    print("Avg accuracy:", sum_accuracy / float(len(y_test)), "over", len(y_test), "sentences (total of", total_words, "words)")
