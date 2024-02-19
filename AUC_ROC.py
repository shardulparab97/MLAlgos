import numpy as np

np.random.seed(42)

data_size = 100
predictions = np.random.random(100)
labels = np.random.randint(2, size=data_size)

print(predictions)
print(labels)


def get_roc(predictions, labels, threshold):
    tpr = 0
    fpr = 0
    tp, fp = 0, 0
    positives = len(labels[labels == 1])
    negatives = len(labels[labels == 0])

    for p, l in zip(predictions, labels):
        pred = 1 if p >= threshold else 0

        if pred == 1 and l == 1:
            tp += 1
        elif pred == 1 and l == 0:
            fp += 1

    tpr = tp / positives
    fpr = fp / negatives
    return (tpr, fpr)

def get_pr(predictions, labels, threshold):
    tp, fp, tn, fn = 0, 0, 0, 0
    epsilon = 0.0000001
    for p, l in zip(predictions, labels):
        pred = 1 if p>=threshold else 0
        if pred==1 and l == 1:
            tp+=1
        elif pred==1 and l==0:
            fp += 1
        elif pred==0 and l==1:
            fn += 1
        elif pred==0 and l==0:
            tn += 1
    precision = tp/(tp + fp + epsilon)
    recall = tp/(tp+fn + epsilon)
    return  (precision, recall)


def get_auc_roc(rocs):
    area = 0
    for i in range(1, len(rocs)):
        area += (roc[i-1][1] - roc[i][1]) * (roc[i][0] + roc[i - 1][0]) / 2
    return area


roc = []

thresholds = [0.1 * i for i in range(11)]

for t in thresholds:
    roc.append(get_roc(predictions, labels, t))

print(roc)
print(get_auc_roc(roc))

prs = []
for t in thresholds:
    prs.append(get_pr(predictions, labels, t))

print(prs)
