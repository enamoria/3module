from src.CONSTANT import WORD_BEGIN, WORD_INSIDE

B_W = WORD_BEGIN
I_W = WORD_INSIDE


def isMatched(sent1, sent2):
    """
    Check if 2 sentences are of the same length and are word-matched positionally
    :param sent1: [[word, tag], [word, tag], ...]
    :param sent2: [[word, tag], [word, tag], ...]
    :return: True if match, no otherwise
    """
    if len(sent1) != len(sent2):
        return False

    # Check if words in each position in 2 sentences are matched
    for i in range(len(sent1)):
        if sent1[i][0] != sent2[i][0]:
            return False

    # Good now, ready to compare 2 sent
    return True


def getLabelList(sent):
    """
    get label list of a sentence
    :param sent: [[word, tag], [word, tag], ...]
    :return: [tag, tag, tag, ...]
    """
    # TODO Take care of empty line and other exception(s)
    return [xxx[1] for xxx in sent]


def whole_word_position(label_list):
    """
    Example: A sentence which have been segmentated represented in list word-tag as below:
        B_W, B_W, I_W, B_W, I_W, B_W, B_W
    The output will be a list of tuples, which represent word position range:
        [0-0, 1-2, 3-4, 5-5, 6-6]
    :param label_list: list label: [B_W, I_W, ....]
    :return: list with format [0-0, 1-2, 3-4, 5-5, ...], each is position of a word (multi-syllables)
    """

    word_with_range = []

    i = -1
    while i < len(label_list) - 1:
        i += 1
        if label_list[i] == B_W or label_list[i] == "O":
            next_BW_pos = 0

            for j in range(i + 1, len(label_list)):
                if label_list[j] == B_W or label_list[j] == "O":
                    next_BW_pos = j
                    break

            word_with_range.append(str(i) + "-" + str(next_BW_pos - 1))

    return word_with_range


def segmentatedWordMatch(label_list_pred, label_list_true):
    """
    Return number of correct segmentated word
    :param label_list_1: list with format [0-1, 1-2, 3-3, ...], each is position of a word (multi-syllables)
    :param label_list_2: list with format [0-1, 1-2, 3-3, ...], each is position of a word (multi-syllables)
    :return: number of elements appear in both 2 lists.
    """
    sent_1_wwr = whole_word_position(label_list_pred)
    sent_2_wwr = whole_word_position(label_list_true)

    return len(set(sent_1_wwr) & set(sent_2_wwr))
    # raise NotImplementedError


def word_segmentation_accuracy(sent_pred, sent_true):
    print("==========")
    print("Calculating segmentation accuracy")

    print("==========")
    print("Check if 2 string is matched positionally ...")
    if isMatched(sents_true, sents_pred):
        print("Ok matched!")
        y_true = getLabelList(sent_pred)
        y_pred = getLabelList(sent_true)
        print(y_true)
        print(y_pred)
    else:
        print("Not matched. Exitting .... ")
        exit()

    # Evaluating
    print("==========")
    print("Start evaluating .... ")

    y_pred = getLabelList(sent_pred)
    y_true = getLabelList(sent_true)

    accuracy = segmentatedWordMatch(y_pred, y_true) / float(y_true.count(B_W) + y_true.count("O"))
    return accuracy


if __name__ == "__main__":
    filename_true = "toy_test.iob"
    fielname_pred = "pred.iob"

    sents_true = []
    with open(filename_true, "r") as ftrue:
        raw_data = ftrue.read().strip("\n").strip(" ").split("\n\n")
        for sent in raw_data:
            # print("xxx", sent)
            sents_true.append([xxx.split("\t") for xxx in sent.split("\n")])
            # print(raw_data)

    sents_pred = []

    with open(fielname_pred, "r") as fpred:
        raw_data = fpred.read().strip("\n").strip(" ").split("\n\n")
        for sent in raw_data:
            sents_pred.append([xxx.split("\t") for xxx in sent.split("\n")])

    print(sents_true)
    print(sents_pred)

    for sent_pred, sent_true in zip(sents_pred, sents_true):
        print(word_segmentation_accuracy(sent_pred=sent_pred, sent_true=sent_true))
