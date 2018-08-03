import nltk
import pycrfsuite
from sklearn_crfsuite import CRF

from V2_CRF.features.features import sent2features, train_word2features
from V2_CRF.src.IO.reader import Reader


def sent2labels(sent):
    return [y[1] for y in sent]


def sent2token(sent):
    return [y[0] for y in sent]

if __name__ == "__main__":
    reader = Reader("/data/data_POS_tag_tieng_viet")
    # reader_test = Reader("/data/test_data_POS_tag_tieng_viet")

    # test_sents = reader_test.read('10000')
    train_sents = reader.read('10000')

    # train_sents = list(nltk.corpus.conll2002.iob_sents("esp.train"))
    # test_sents = list(nltk.corpus.conll2002.iob_sents("esp.testb"))

    X_train = [sent2features(sent) for sent in train_sents]
    y_train = [sent2labels(sent) for sent in train_sents]

    print(train_sents[0])
    print(train_word2features(train_sents[0], 0))

    # X_test = [sent2features(sent) for sent in test_sents]
    # y_test = [sent2labels(sent) for sent in test_sents]

    trainer = pycrfsuite.Trainer(verbose=True)

    for xx, yy in zip(X_train, y_train):
        # try:
        # print(xseq[0][1])
        # print(xseq[0][1].encode("utf8"))
        # print([yy.encode("utf-8") for yy in yseq])

        xseq = []
        for xxx in xx:
            xseq.append([xxxx.encode("utf-8") for xxxx in xxx])
        yseq = [yyyy.encode("utf-8") for yyyy in yy]

        # print(yseq)

            # for xx in xseq:
            #     # print("xx")
            #     trainer.append(xx, xx)
            # for yy in yseq:
            #     # print("yy")
            #     trainer.append(yy, yy)
        trainer.append(xseq, yseq)
            # trainer.append(yseq, yseq)
            # print(yseq)
        # except UnicodeEncodeError as e:
        #     print(yseq)
        #     print("Shit happened:", e)
        #     pass

    trainer.set_params({
        # 'c1': 1e-5,  # Coeff for L1 penalty
        'c2': 1e-3,  # Coeff for L2 penalty
        'max_iterations': 100,

        # # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    })

    print("=====================")
    print("Start training ...")
    trainer.params()

    trainer.train('iter100')
    print("Done training!")

    # tagger = pycrfsuite.Tagger().open('xxxxx')
    #
    # for test_sent in test_sents:
    #     print(" ".join(sent2token(test_sents)))
    #     print(tagger.tag(sent2features(test_sents)))
