import numpy as np
from sklearn.datasets import load_wine
import random
from visuals import *


def fuzzyCMeans(points, clusterCount, m, metrik=(lambda x, y: sum([(a - b) ** 2 for a, b in zip(x, y)])),
                epsilon=0.0000001, init=None, max_iteration=100):
    n = len(points)
    last_u = np.zeros([clusterCount, n])

    v = np.zeros([clusterCount, len(points[0])])
    u = np.zeros([clusterCount, n])
    for i in range(clusterCount):
        for j in range(n):
            u[i][j] = random.random()

    # normalize row
    u /= u.sum(axis=1, keepdims=1)
    last_u = np.zeros_like(u)

    iteration = 0
    while np.linalg.norm(u - last_u) > epsilon and iteration < max_iteration:
        last_u = u
        u = np.zeros_like(last_u)

        # calculating v
        for i in range(clusterCount):
            sumUpper = 0
            sumLower = 0

            for k in range(n):
                uikm = last_u[i][k] ** m
                sumUpper += uikm * points[k]
                sumLower += uikm
            v[i] = sumUpper / sumLower

        # calculating u
        u = np.zeros([clusterCount, n])
        for i in range(clusterCount):
            for k in range(n):
                dik = metrik(points[k], v[i])
                sum = 0
                for j in range(clusterCount):
                    sum += (dik / metrik(points[k], v[j])) ** (2 / m - 1)
                u[i][k] = 1 / sum
        iteration += 1

    clusterNr = np.argmax(u, axis=0)
    wahrscheinlichkeiten = np.max(u, axis=0)

    links = makePlots(points, v,  wahrscheinlichkeiten, clusterNr)
    return points, clusterNr, links


# ---- Beispieltests ---- #

if __name__ == '__main__':

    wine_data = load_wine()
 
    different_metrics = {
        "squared_eucledian": lambda x, y: sum([(a - b) ** 2 for a, b in zip(x, y)]),
        "eucledian": lambda x, y: sum([(a - b) ** 2 for a, b in zip(x, y)]) ** (1 / 2),
        "manhattan": lambda x, y: sum([abs(a - b) for a, b in zip(x, y)]),
        "inverse_eucleadian": lambda x, y: 1 / (sum([(a - b) ** 2 for a, b in zip(x, y)]) ** (1 / 2))
    }

    inData = np.array(wine_data.get("data"))
    fuzzyCMeans(inData, clusterCount=3, m=1.1, epsilon=0.01)