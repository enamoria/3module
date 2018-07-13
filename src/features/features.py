"""
    Feature engineering procedure is defined here.
"""

from feature_function import *

def train_word2features(sent, i):  # sent: [('Melbourne', 'NP', 'B-LOC'), ('(', 'Fpa', 'O'), ('Australia', 'NP', 'B-LOC'), (')', 'Fpt', 'O'), (',', 'Fc', 'O'), ('25', 'Z', 'O'), ('may', 'NC', 'O'), ('(', 'Fpa', 'O'), ('EFE', 'NC', 'B-ORG'), (')', 'Fpt', 'O'), ('.', 'Fp', 'O')]
    word = sent[i][0]  # 'Melbourne'
    postag = sent[i][1]  # 'NP'

    # basic features, based on current word
    features = {
        'word.lower': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper': word.isupper(),
        'word.istitle': word.istitle(),
        'word.isdigit': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
        'word.BOS': (i == 0),
        'word.EOS': (i == len(sent) - 1)
    }

    # even more features, based on previous word(s?)
    if i > 0:  # Not the first word, so there will be a "previous" word
        word_ = sent[i - 1][0]
        postag_ = sent[i - 1][1]

        features.update({ 
            '-1:word.lower': word_.lower(),
            '-1:word.istitle': word_.istitle(),
            '-1:word.isupper': word_.isupper(),
            '-1:postag': postag_,
            '-1:postag[:2]': postag_[:2],
            '-1:word.BOS': False,
            '-1:word.EOS': (i == len(sent) - 1)
        })
        if i > 1:
            word__ = sent[i - 2][0]
            postag__ = sent[i - 2][1]

            features.update({ 
                '-2:word.lower': word__.lower(),
                '-2:word.istitle': word__.istitle(),
                '-2:word.isupper': word__.isupper(),
                '-2:postag': postag__,
                '-2:postag[:2]': postag__[:2],
                '-2:word.BOS': False,
                '-2:word.EOS': (i == len(sent) - 1)
            })
    # else:  # first word
    #     features.append("BOS")  # Begin of Sentence, but how the fuck?

    if i < len(sent) - 1:  # Not the last word, so there will be a "later" word
        word_ = sent[i + 1][0]
        # print(sent[i+1])
        postag_ = sent[i + 1][1]

        features.update({ 
            '+1:word.lower': word_.lower(),
            '+1:word.istitle': word_.istitle(),
            '+1:word.isupper': word_.isupper(),
            # '+1:postag': postag_,
            # '+1:postag[:2]': postag[:2],
            '+1:word.BOS': (i == 0),
            '+1:word.EOS': False
        })
        if i < len(sent) - 2:
            word__ = sent[i + 2][0]
            postag__ = sent[i + 2][1]

            features.update({ 
                '+2:word.lower': word__.lower(),
                '+2:word.istitle': word__.istitle(),
                '+2:word.isupper': word__.isupper(),
                # '-1:postag': postag__,
                # '-1:postag[:2]': postag__[:2],
                '+2:word.BOS': (i == 0),
                '+2:word.EOS': False
            })
    # else:  # last word
    #     features.append("EOS")  # End of Sentence, but again how the fuck?

    return features


def test_word2features(sent, i):  # sent: [('Melbourne', 'NP', 'B-LOC'), ('(', 'Fpa', 'O'), ('Australia', 'NP', 'B-LOC'), (')', 'Fpt', 'O'), (',', 'Fc', 'O'), ('25', 'Z', 'O'), ('may', 'NC', 'O'), ('(', 'Fpa', 'O'), ('EFE', 'NC', 'B-ORG'), (')', 'Fpt', 'O'), ('.', 'Fp', 'O')]
    word = sent[i][0]  # 'Melbourne'
    postag = sent[i][1]  # 'NP'

    # basic features, based on current word
    features = {
        'word.lower': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper': word.isupper(),
        'word.istitle': word.istitle(),
        'word.isdigit': word.isdigit(),
        # 'postag': postag,
        # 'postag[:2]': postag[:2],
        'word.BOS': (i == 0),
        'word.EOS': (i == len(sent) - 1)
    }

    # even more features, based on previous word(s?)
    if i > 0:  # Not the first word, so there will be a "previous" word
        word_ = sent[i - 1][0]
        postag_ = sent[i - 1][1]

        features.update({ 
            '-1:word.lower': word_.lower(),
            '-1:word.istitle': word_.istitle(),
            '-1:word.isupper': word_.isupper(),
            # '-1:postag': postag_,
            # '-1:postag[:2]': postag_[:2],
            '-1:word.BOS': False,
            '-1:word.EOS': (i == len(sent) - 1)
        })
        if i > 1:
            word__ = sent[i - 2][0]
            postag__ = sent[i - 2][1]

            features.update({ 
                '-2:word.lower': word__.lower(),
                '-2:word.istitle': word__.istitle(),
                '-2:word.isupper': word__.isupper(),
                # '-2:postag': postag__,
                # '-2:postag[:2]': postag__[:2],
                '-2:word.BOS': False,
                '-2:word.EOS': (i == len(sent) - 1)
            })
    # else:  # first word
    #     features.append("BOS")  # Begin of Sentence, but how the fuck?

    if i < len(sent) - 1:  # i is ot the last word, so there will be a "later" word
        word_ = sent[i + 1][0]
        postag_ = sent[i + 1][1]

        features.update({ 
            '+1:word.lower': word_.lower(),
            '+1:word.istitle': word_.istitle(),
            '+1:word.isupper': word_.isupper(),
            # '+1:postag': postag_,
            # '+1:postag[:2]': postag[:2],
            '+1:word.BOS': (i == 0),
            '+1:word.EOS': False
        })
        if i < len(sent) - 2:
            word__ = sent[i + 2][0]
            postag__ = sent[i + 2][1]

            features.update({ 
                '+2:word.lower': word__.lower(),
                '+2:word.istitle': word__.istitle(),
                '+2:word.isupper': word__.isupper(),
                # '-1:postag': postag__,
                # '-1:postag[:2]': postag__[:2],
                '+2:word.BOS': (i == 0),
                '+2:word.EOS': False
            })
    # else:  # last word
    #     features.append("EOS")  # End of Sentence, but again how the fuck?

    # return [feature for feature in features]


def word2features(sent, i):
    word = sent[i][0]

    features = {
        'word[-4:]': sent[i-4][0].lower() if i >= 4 else "",
        'word[-3:]': sent[i-3][0].lower() if i >= 3 else "",
        'word[-2:]': sent[i-2][0].lower() if i >= 2 else "",
        'word[-1:]': sent[i-1][0].lower() if i >= 1 else "",
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

    # print(features)
    # input("..")
    return features


def sent2features(sent, mode='train'):
    # if mode == 'train':
    #     return [train_word2features(sent, i) for i in range(len(sent)) if sent[i][0]]
    # if mode == 'test':
    #     return [test_word2features(sent, i) for i in range(len(sent)) if sent[i][0]]

    return [word2features(sent, i) for i in range(len(sent))]
