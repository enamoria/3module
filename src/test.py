# -*- coding: utf-8 -*-

import pickle
import argparse
from src.features.features import sent2features, train_word2features
from src.utils import *
from src.eval import segmentatedWordMatch, word_segmentation_accuracy

MODEL_NAME = "ws_model.pkl_2"


def parse_argument():
    parser = argparse.ArgumentParser(description="Test a model")
    parser.add_argument("-n", metavar='NAME', type=str, help="Name of model which is going to be tested")
    return parser.parse_args()

if __name__ == "__main__":
    # parseArgument()
    # args = parseArgument()
    #
    # MODEL_NAME = args.n

    # MODEL_NAME = "WordSegModel_final_LBFGS_1000_iter"
    # MODEL_NAME = "WordSegModel_final_l2sgd"
    # MODEL_NAME = "WordSegModel_final_lbfgs_states_transaction_0.0_0.05"

    print("=======================================")
    print("Reading testing data ....")
    test_sents = []
    filename_test = "test.txt"

    with open(filename_test, "r") as ftrue:
        raw_data = ftrue.read().strip("\n").strip(" ").split("\n\n")
        for sent in raw_data:
            test_sents.append([xxx.split("\t") for xxx in sent.split("\n")])

    X_test = [sent2features(sent, 'test') for sent in test_sents if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]
    y_test = [sent2labels(sent) for sent in test_sents if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]

    print("Done!")
    print("=======================================")
    print("Load the model ...")
    model = pickle.load(file=open(MODEL_NAME, "rb"))
    print("Done loading", MODEL_NAME)

    print("=======================================")
    print("Testing ...")
    score = model.score(X_test, y_test)
    y_pred = model.predict(X_test)

        # print(y_pred[1])
        # print(test_sents[1])

    sum_accuracy = 0
    for i, (y1, y2) in enumerate(zip(y_pred, y_test)):
        try:
            acc = segmentatedWordMatch(y1, y2) / float(y2.count("B-W"))
            # print("Sent", i, ":", round(acc, 4))
            sum_accuracy += acc

            # if acc > 0.9:
            #     x1 = test_sents[i]
            #     x2 = [[test_sents[i][j][0], y_pred[i][j]] for j in range(len(test_sents[i]))]
            #
            #     print("x1", list_to_sentence(x1))
            #     print("x2", list_to_sentence(x2))
            #     print(acc, y2.count("B-W"))
            #     input("..")
            #     # print(i, test_sents[i])
        except ZeroDivisionError:
            print("y1", y1)
            print("y2", y2)

    total_words = sum([len(xxx) for xxx in test_sents])
    print("Avg accuracy:", sum_accuracy / float(len(y_test)), "over", len(y_test), "sentences (total of", total_words, "words)")

    # print("=======================================")
    # print("Segmentate a sentence ...")
    # test = "Đối với các chuyên khoa khác như : Phẩu thuật tổng quát ( nội trú 5 năm ) , sản ( nội trú 5 năm ) , chấn thương chỉnh hình ( nội trú 5 năm ) . Và chuyên sâu mỗi chuyên khoa tầm ( 1 - 3 năm tùy chuyên khoa ) . Nói chung cũng tầm 15 - 16 năm ( cho lầm sàn , chưa kể Ph.D )"
    # print(test)
    # test = [[x, "X"] for x in test.split(" ")]
    # print(test)
    # test_seg_tag = model.predict([sent2features(test, 'test')])
    # sent_with_tag = [[test[j][0], test_seg_tag[0][j]] for j in range(len(test))]
    # print(list_to_sentence(sent_with_tag))

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