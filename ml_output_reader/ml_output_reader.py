# COMPARE BY STRICT OR VALIDATION - only comment one out below
validation_bool = True


# validation_bool = False

class Result:
    def __init__(self, lr, dropout, epoch=1, scores=None):
        if scores is None:
            scores = {
                "loss": 99.99,
                "f1": 0.0,
                "precision": 0.0,
                "recall": 0.0
            }
        self.lr = lr
        self.dropout = dropout
        self.epoch = epoch
        self.scores = scores

    def name(self):
        return "lr: %f, dropout: %f" % (self.lr, self.dropout)

    def update(self, epoch, loss, f1, precision=0, recall=0):
        if f1 > self.scores["f1"]:
            self.epoch = epoch
            self.scores["f1"] = f1
            self.scores["loss"] = loss
            self.scores["precision"] = precision
            self.scores["recall"] = recall

    def output(self):
        return "Epoch: " + str(self.epoch), "Results:", self.scores

    def __gt__(self, other):
        return self.scores["f1"] > other.scores["f1"]


if __name__ == "__main__":
    if validation_bool:
        prefix = "val_"
        print("comparing validation results")
    else:
        prefix = ""
        print("comparing non-validation results")

    # outputfile = "nohup_run_hyperparam_tuning"
    outputfile = "../ml_approach/out/1:2.txt"
    outputread = []
    with open(outputfile, "rt") as file:
        for line in file:
            g = line.strip()
            if g.split()[0] == "Classifier":
                outputread.append([])
            if g.split()[0] in ["Classifier", "Epoch", "2/2"]:
                outputread[-1].append(g)

    for index, sublist in enumerate(outputread):
        for subindex, item in enumerate(sublist):
            print(item.split())
            if item.split()[0] not in ["Classifier", "Epoch", "2/2"]:
                print("\t\t", outputread[index][subindex])
                outputread[index].pop(subindex)

    results = []
    for i in outputread:

        init = i.pop(0).split()
        results.append(Result(float(init[4][:-1]), float(init[-1].upper())))
        while i:  # remainder of strings in list are pairs of 2, Epoch string and scores string
            epoch = int(i.pop(0).split()[1][:-4])
            scores = i.pop(0).split()
            loss = float(scores[scores.index(prefix + "loss:") + 1])
            f1 = float(scores[scores.index(prefix + "f1_score:") + 1])
            precision, recall = "did not find", "did not find"
            for s in scores:
                if s[:9] == "precision":
                    precision = scores[scores.index(s)+1]
                if s[0:6] == "recall":
                    recall = scores[scores.index(s)+1]
            results[-1].update(epoch, loss, f1, precision, recall)

    print("RESULTS:")
    for i in results:
        print(i.name(), i.output())

    bestf1 = results[0]
    for i in results:
        if i > bestf1:
            bestf1 = i
    print("Best F1 performance below:\n", bestf1.name(), bestf1.output())

