# -*- coding: utf-8 -*-
# from tokenizer import tokenize
import pycrfsuite

from V2_CRF.features.features import sent2features
from V2_CRF.src.IO.reader import Reader

# from our


MODEL_NAME = "iter100"

def sent2labels(sent):
    return [y[1] for y in sent]


def sent2tokens(sent):
    return [y[0] for y in sent]


if __name__ == "__main__":
    reader = Reader("/data/data_POS_tag_tieng_viet")
    test_sents = reader.read('10000')
    #
    # data = [file for file in data]

    # input("..")
    # train_sents = list(nltk.corpus.conll2002.iob_sents("esp.train"))
    # test_sents = list(nltk.corpus.conll2002.iob_sents("esp.testb"))

    # print(train_sents[0])
    # input("...")

    # X_train = [sent2features(sent) for sent in train_sents]
    # y_train = [sent2labels(sent) for sent in train_sents]

    X_test = [sent2features(sent) for sent in test_sents]
    y_test = [sent2labels(sent) for sent in test_sents if len(sent) >= 1 and not sent[0][0]]

    print(X_test[0])
    tagger = pycrfsuite.Tagger()
    tagger.open(MODEL_NAME)

    sum = 0.0
    for test_sent in test_sents:
        true = [yy.encode("utf-8") for yy in sent2labels(test_sent)]

        print(test_sent)
        tmp_pred = tagger.tag(sent2features(test_sent, mode='test'))

        pred = [yy_pred.encode("utf-8") for yy_pred in tmp_pred]

        if len(true) != len(pred):
            input("Length is difference:", test_sent)
            exit()

        count = 0.0
        for xxx in range(len(pred)):
            if true[xxx] == pred[xxx]:
                count += 1

        # print(test_sent)
        # print(sent2labels(test_sent))
        # print(tagger.tag(sent2features(test_sent, mode='test')))

        if count/len(pred) < 0.7:
            print(true)
            print(pred)
            print(sent2tokens(test_sent))
            print(count / len(pred))
            sum += count / len(pred)
            input("..")

        # print(count / len(pred))
        # sum += count / len(pred)
        # input("..")

            # input("..")

    print("Avg acc:", sum/len(test_sents))
