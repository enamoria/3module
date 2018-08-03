from __future__ import print_function

import argparse
import pickle
import logging

from sklearn_crfsuite import CRF

from data_helpers import read_data, checkModelFileExistAndCreateNewModelName, sent2label
from features.features import chunking_sent2features
from CONSTANT import ROOT_DIR


def parse_argument():
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
                        help="Name of the model (will be saved on disk). Default is chunk.pkl (add indices if duplicated)")

    parser.add_argument("-i", metavar="iter", type=int, default=300, help="Max iteration for optimization. Default 300")
    parser.add_argument("-d", metavar="delta", type=float, default=1e-5, help="stopping criteria. Default 1e-5")

    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

    logging.info("Start ...")

    # Argument parsing
    args = parse_argument()
    MODEL_NAME = checkModelFileExistAndCreateNewModelName(args.m.replace(".pkl", "") + ".pkl")
    MAX_ITER = args.i
    DELTA = args.d

    # Read data
    print("====================================================")
    train_sents = read_data(ROOT_DIR + "/data/ner/vlsp2016/corpus/train.txt")
    dev_sent = read_data(ROOT_DIR + "/data/ner/vlsp2016/corpus/dev.txt")
    test_sents = read_data(ROOT_DIR + "/data/ner/vlsp2016/corpus/test.txt")

    # Transform text data to feature
    print("====================================================")
    X_train = [chunking_sent2features(sent=sent, mode='train') for sent in train_sents]
    y_train = [sent2label(sent) for sent in train_sents]

    X_dev = [chunking_sent2features(sent=sent, mode='dev') for sent in dev_sent]
    y_dev = [sent2label(sent) for sent in dev_sent]

    X_test = [chunking_sent2features(sent=sent, mode='test') for sent in test_sents]
    y_test = [sent2label(sent) for sent in test_sents]

    # Build the model
    # print("Build the model ...")
    logging.info("Build the model..")
    model = CRF(
        algorithm='lbfgs',
        all_possible_transitions=True,
        c1=0.5, c2=0.005,
        max_iterations=MAX_ITER,
        delta=DELTA,
        period=30,
        verbose=True)

    # print("Training ...")
    logging.info("Training ...")
    model.fit(X_train, y_train, X_dev, y_dev)
    # print("Done training! Saving the model to /models/" + MODEL_NAME)
    logging.info("Done training! Saving the model to /models/" + MODEL_NAME)

    pickle.dump(model, open(MODEL_NAME, "wb"), protocol=2)
    logging.info("Done pickling!!!")
    # print("Done!!!")

    # Test, not necessary, can be commented for code condensation
    # print("=======================")
    # print("Testing ....")
    # score = model.score(X_test, y_test)
    # print(score)
    # print("Done!!!")



