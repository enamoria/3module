"""
    Feature engineering procedure is defined here.

    There are 3 modes in extracting feature. The features will be the same,
    but because of differences between the data, the code of this mode will
    differ from the others.
        + raw: only text, without any tags
        + train: text with its tag
        + test: text with its tag
"""

from __future__ import print_function

from feature_function import *


def word2features(sent, i, mode=None):
    assert mode is not None, "specify a mode (raw/train/test) in feature extracting"

    if mode == "raw":
        word = sent[i]
    else:
        word = sent[i][0]

    # word = sent[i][0]
    # postag = sent[i][1]

    features = {
        'word[-4:]': word.lower()[-4:],
        'word[-3:]': word.lower()[-3:],
        'word[-2:]': word.lower()[-2:],
        'word[-1:]': word.lower()[-1:],
        'word.lower()': word.lower(),
        'number': isNumber(word),
        'punc&sym': isPunc(word),
        'BOS()': i == 0,
        'EOS()': i == len(sent) - 1,
        'num_tok': len(word.split("_")),
        'word.istitle()': word.istitle(),
        'word.isupper()': word.isupper(),
        'word.ispunc()': isPunc(word)
    }

    return features


def postag_word2features(sent, i, mode=None):
    assert mode is not None, "specify a mode (raw/train/test) in feature extracting"

    if mode == "raw":  # Do not confused raw mode with test mode: input in raw mode is raw text, while test mode input have pos-tag and were segmented beforehand
        word = sent[i]  # Just splited text, no label
        word1 = sent[i - 1] if i >= 1 else ""
        word2 = sent[i - 2] if i >= 2 else ""
        word3 = sent[i - 3] if i >= 3 else ""
        word4 = sent[i - 4] if i >= 4 else ""
    else:  # Train or test mode: in test mode, input string will be output of pos-tag, which was segmented
        word = sent[i][0]  # Labeled (pos)
        word1 = sent[i - 1][0] if i >= 1 else ""
        word2 = sent[i - 2][0] if i >= 2 else ""
        word3 = sent[i - 3][0] if i >= 3 else ""
        word4 = sent[i - 4][0] if i >= 4 else ""

    features = {
        'sent[-4:]': word4.lower(),
        'sent[-3:]': word3.lower(),
        'sent[-2:]': word2.lower(),
        'sent[-1:]': word1.lower(),

        'word.lower': word.lower(),
        'word.title': word.title(),

        'number': isNumber(word),
        'punc&sym': isPunc(word),
        'isNp': isNp(word),

        'BOS()': i == 0,
        'EOS()': i == len(sent) - 1,

        'num_tok': len(word.split("_")),

        'word.istitle()': word.istitle(),
        'word.isupper()': word.isupper(),
        'word.ispunc()': isPunc(word),
    }

    return features


def sent2features(sent, mode):
    # if mode == 'train':
    #     return [train_word2features(sent, i) for i in range(len(sent)) if sent[i][0]]
    # if mode == 'test':
    #     return [test_word2features(sent, i) for i in range(len(sent)) if sent[i][0]]

    return [word2features(sent, i, mode) for i in range(len(sent))]
    # return [postag_word2features(sent, i, mode) for i in range(len(sent))]
