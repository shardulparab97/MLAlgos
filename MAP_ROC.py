def auc_roc(true_labels, predictions):
    data = zip(predictions, true_labels)
    data = sorted(data, key=lambda k: k[0])

    positives = sum([1 for x, y in data if y == 1])
    negatives = sum([1 for x, y in data if y == 0])

    tp, fp = 0, 0

    prev_tpr, prev_fpr = 0, 0
    area = 0

    for i in range(len(data) - 1, -1, -1):
        if data[i][1] == 1:
            tp += 1
        if data[i][1] == 0:
            fp += 1

        tpr = tp / positives if positives > 0 else 0
        fpr = fp / negatives if negatives > 0 else 0

        if prev_fpr is not None and prev_tpr is not None:
            area += 0.5 * (fpr - prev_fpr) * (prev_tpr + tpr)

        prev_fpr = fpr
        prev_tpr = tpr

    return area


def auc_roc(true_labels, predictions):
    data = zip(predictions, true_labels)
    data = sorted(data, key=lambda k: k[0])

    positives = sum([1 for x, y in data if y == 1])
    negatives = sum([1 for x, y in data if y == 0])

    tp, fp = 0, 0

    prev_tpr, prev_fpr = 0, 0
    area = 0

    for i in range(len(data) - 1, -1, -1):
        if data[i][1] == 1:
            tp += 1
        if data[i][1] == 0:
            fp += 1

        tpr = tp / positives if positives > 0 else 0
        fpr = fp / negatives if negatives > 0 else 0

        if prev_fpr is not None and prev_tpr is not None:
            area += 0.5 * (fpr - prev_fpr) * (prev_tpr + tpr)

        prev_fpr = fpr
        prev_tpr = tpr

    return area
