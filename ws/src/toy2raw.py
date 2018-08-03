filename = "toy_test.iob"


def conll2raw():
    with open(filename, "r") as f:
        raw_data = f.read().strip("\n").strip(" ").split("\n\n")
        print(raw_data)

    f_out = open("raw_" + filename, "w")
    for sent in raw_data:
        # print(sent)
        f_out.write(" ".join([word.split("\t")[0] for word in sent.split("\n")[:len(sent.split("\n")) - 1]]))
        f_out.write(sent[len(sent.split("\n")) - 1] + "\n")
        input("..")
    # f_out.write(raw_data[len(raw_data)-1].split("\t")[0] + "\n")
    f_out.close()


def onelinelabeled2raw():
    raise NotImplementedError


def conll2segmented():
    # raise NotImplementedError
    sents = []
    with open(filename, "r") as f:
        raw_data = f.read().strip("\n").strip(" ").split("\n\n")
        # print(raw_data)

        for sent in raw_data:
            sents.append([xxx.split("\t") for xxx in sent.split("\n")])

    segmentated_raw_sent = ""
    for sent in sents:
        print(sent)
        for j, word in enumerate(sent):
            # print(sent[j])
            if (sent[j][1] == "B_W" or sent[j][1] == "I_W") and sent[j+1][1] == "I_W":
                segmentated_raw_sent += sent[j][0] + "_"
            else:
                segmentated_raw_sent += sent[j][0] + " "

    return segmentated_raw_sent.strip(" ")

if __name__ == "__main__":
    results = conll2segmented()
    print(len(results.split(" ")), results)