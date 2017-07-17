import numpy as np
import operator
import matplotlib as plot


def creatDataSet():
    group = [[1., 1.1], [1., 1.], [0., .0], [.0, .1]]
    label = ['A', 'A', 'B', 'B']
    return group, label


group, label = creatDataSet()


def classify0(inX, dataSet, labels, K):
    dataSetSize = len(dataSet)
    diffMat = np.tile(inX, (len(dataSet), 1)) - dataSet
    sqdiff = diffMat ** 2
    squareDist = np.sum(sqdiff, axis=1)
    sorteDistIndex = np.argsort(squareDist)
    classCount = {}
    for i in range(K):
        votelabel = label[sorteDistIndex[i]]
        classCount[votelabel] = classCount.get(votelabel, 0) + 1
    max = 0
    key0 = ""
    for key, value in classCount.items():
        if value > max:
            max = key
            key0 = key

    return key0


print classify0([0., 0.], group, labels=label, K=3)
