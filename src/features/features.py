"""
    Feature engineering procedure is defined here.
"""

from feature_function import *


def word2features(sent, i, mode):
    # word = sent[i][0]
    if mode == "test":  # test mode: no segment tag, just raw text
        word = sent[i]
        word1 = sent[i - 1] if i >= 1 else ""
        word2 = sent[i - 2] if i >= 2 else ""
        word3 = sent[i - 3] if i >= 3 else ""
        word4 = sent[i - 4] if i >= 4 else ""
    else:  # Test mode: in test mode, input string will be output of pos-tag, which was segmented and tagged
        word = sent[i][0]  # Labeled (both pos and chunk)
        word1 = sent[i - 1][0] if i >= 1 else ""
        word2 = sent[i - 2][0] if i >= 2 else ""
        word3 = sent[i - 3][0] if i >= 3 else ""
        word4 = sent[i - 4][0] if i >= 4 else ""

    features = {
        'word[-4:]': word4.lower() if i >= 4 else "",
        'word[-3:]': word3.lower() if i >= 3 else "",
        'word[-2:]': word2.lower() if i >= 2 else "",
        'word[-1:]': word1.lower() if i >= 1 else "",
        'word.lower': word.lower(),
        'word.title': word.title(),
        'number': isNumber(word),
        'punc&sym': isPunc(word),
        'BOS()': i == 0,
        'EOS()': i == len(sent) - 1,
        # 'num_tok': len(word.split("_")),
        'word.istitle': word.istitle(),
        'word.isupper': word.isupper(),

        'word.isInDict': isInDict(word),
        'bigram.isInDict': isInDict(word1 + " " + word),
        'trigram.isInDict': isInDict(word2 + " " + word1 + " " + word)
        # 'word.ispunc()': isPunc(word)
    }

    return features


def sent2features(sent, mode='train'):
    # if mode == 'train':
    #     return [train_word2features(sent, i) for i in range(len(sent)) if sent[i][0]]
    # if mode == 'test':
    #     return [test_word2features(sent, i) for i in range(len(sent)) if sent[i][0]]

    return [word2features(sent, i, mode) for i in range(len(sent))]
