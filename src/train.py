import os
import nltk
import pycrfsuite
import argparse
import pickle

from scipy.special._ufuncs import y0
from sklearn_crfsuite import CRF
from features.features import sent2features, train_word2features
from utils import *

# MODEL_NAME = 'WordSegModel_final_lbfgs_trantion_0.0_0.si05'
MODEL_NAME = 'ws_model_07_13.pkl'


def parse_argument():
    # TODO NEED TO BE REFINE: THIS IS COPIED FROM CHUNKING
    """
    Parse argument from commandline:
        Required arguments:


        Optional arguments:
            -m --model      :   Name of the model (will be saved on disk). Default chunk.pkl (add indices if duplicated)
            -i --iter       :   Max iteration for optimization. Default 300
            -e --epsilon    :   epsilon - stopping criteria. Default 1e-5
    :return: args: args list.
    """

    parser = argparse.ArgumentParser(description="Chunking trainer")

    parser.add_argument("-m", metavar="model", required=True, type=unicode, default="chunk1",
                        help="Name of the model (will be saved on disk). Default ws_model.pkl (indexed if duplicated)")

    parser.add_argument("-i", metavar="iter", type=int, default=300, help="Max iteration for optimization. Default 300")
    parser.add_argument("-d", metavar="delta", type=float, default=1e-5, help="stopping criteria. Default 1e-5")

    return parser.parse_args()


if __name__ == "__main__":
    filename_true = "train.txt"
    # fielname_pred = "pred.iob"
    MODEL_NAME = checkModelFileExistAndCreateNewModelName(MODEL_NAME)

    # Read data
    train_sents = []
    with open(filename_true, "r") as ftrue:
        raw_data = ftrue.read().strip("\n").strip(" ").split("\n\n")
        for sent in raw_data:
            train_sents.append([xxx.split("\t") for xxx in sent.split("\n")])

    # Feature extracting from templates
    X_train = [sent2features(sent) for sent in train_sents]  # if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]
    y_train = [sent2labels(sent) for sent in train_sents]  # len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]

    # print(X_train)
    # print(y_train)

    # X_test = [sent2features(sent, 'test') for sent in test_sents if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]
    # y_test = [sent2labels(sent) for sent in test_sents if len(sent) >= 1 and len(sent[0]) >= 1 and sent[0][0]]

    # X_test = [sent2features(sent) for sent in test_sents]
    # y_test = [sent2labels(sent) for sent in test_sents]

    # Training ...
    print("=======================================")
    print("Start training ...")
    model = CRF(algorithm="lbfgs",
                c1=0.1, c2=0.002,
                max_iterations=3000,
                all_possible_transitions=True,
                period=30,
                verbose=True)

    # model = CRF(algorithm='l2sgd', c2=0.01, verbose=True, max_iterations=3000,
    #             calibration_eta=0.1, calibration_rate=1.5, calibration_samples=100, calibration_max_trials=50)

    # model.set_params({
    #     'c2' = 0.2
    # })

    model.fit(X=X_train, y=y_train)
    print("Done training !")

    print("=======================================")
    print("Saving model ...")
    pickle.dump(model, open(MODEL_NAME, 'wb'), protocol=2)
    print("Done saving model !")

    print("=======================================")
    # print("Testing ...")
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
    # print("=====================")
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
