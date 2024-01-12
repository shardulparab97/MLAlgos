
# last element is the true class
# all float values
import math

# Step 1: get euclidean distance
def euclidean_distance(val1, val2):
    assert len(val1) == len(val2)
    # return sum(abs((val1-val2)**2)) ** 0.5
    return sum([(val1[i] - val2[i]) ** 2 for i in range(len(val1))])** 0.5

# step 2: find the neighbours for each test case
def get_k_neighbors(train_data, test_case, k):
    dists = []
    for train_pt in train_data:
        dists.append(euclidean_distance(test_case, train_pt[:-1], train_pt), train_pt)
    dists.sort(key=lambda x: x[0])
    dists = dists[:k]
    return [i[1] for i in dists]

# get labels by majority count
def get_labels(train_data, test_case, k):
    neighbors = get_k_neighbors(train_data, test_case, k)
    labels = [pt[-1] for pt in neighbors]
    max_label = max(labels, key=labels.count)

    return max_label

def solution(train_data, test_data, k):
    final_labels = list()
    for test_pt in test_data:
        final_labels.append(get_labels(train_data, test_pt, k))
    return  final_labels



train_data = [[0.40145672, 0.23325969, 0.11457933, 0.31289797, 0.3872147 ,
        0.84975022, 0.33948578, 0.8769761 ],
       [0.25250704, 0.5394347 , 0.46253534, 0.18695039, 0.31153739,
        0.42475639, 0.87842481, 0.13222934],
       [0.22196718, 0.4737825 , 0.01938843, 0.72986941, 0.17723646,
        0.79630187, 0.36651221, 0.53246385],
       [0.87776313, 0.70092249, 0.66674826, 0.39066688, 0.43247307,
        0.22506983, 0.51213956, 0.32700443],
       [0.5284344 , 0.46025279, 0.73558956, 0.77605705, 0.89680743,
        0.97088546, 0.65692402, 0.35864298],
       [0.46244709, 0.42772829, 0.65984236, 0.86943405, 0.91255555,
        0.2525491 , 0.98276608, 0.11250653],
       [0.88481024, 0.91629702, 0.72241864, 0.95434682, 0.55887534,
        0.93732869, 0.07947003, 0.20486512],
       [0.90004495, 0.77847567, 0.26682971, 0.03289147, 0.68639613,
        0.81540798, 0.59801094, 0.31382728],
       [0.60400659, 0.05539674, 0.09337197, 0.97402619, 0.60437405,
        0.03283176, 0.16303488, 0.23390551],
       [0.22827684, 0.80074973, 0.31436037, 0.22341328, 0.34546472,
        0.92904086, 0.41294095, 0.67623982]]

for i in range(1, len(train_data)):
    res = euclidean_distance(train_data[i-1], train_data[i])
    print(res)

