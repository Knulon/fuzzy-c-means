import numpy as np
from sklearn.datasets import load_wine
import random
from visuals import *

""" function fuzzyCMeans
    points:         2D numpy array with coordianates of points
    cluster_count:  count of clusters
    m:              fuzzy factor > 1 
    metric:         distance metric as lambda expression
    epsilon:        error value > 0 to terminate
    init:           way of initializing the u matrix => currently not used (=random)
    max_iterations: maximum count of possible iterations before terminating
"""
def fuzzyCMeans(points, cluster_count, m, metric=(lambda x, y: sum([(a - b) ** 2 for a, b in zip(x, y)])),
                epsilon=0.001, init=None, max_iterations=100):
    n = len(points)
    v = np.zeros([cluster_count, len(points[0])])
    u = np.zeros([cluster_count, n])

    # random initialize u matrix
    for i in range(cluster_count):
        for j in range(n):
            u[i][j] = random.random()

    # normalize row
    u /= u.sum(axis=1, keepdims=1)
    last_u = np.zeros_like(u)

    iteration = 0
    while np.linalg.norm(u - last_u) > epsilon and iteration < max_iterations:
        last_u = u

        # calculating v
        for i in range(cluster_count):
            sumUpper = 0
            sumLower = 0

            for k in range(n):
                uikm = last_u[i][k] ** m
                sumUpper += uikm * points[k]
                sumLower += uikm
            v[i] = sumUpper / sumLower

        # calculating u
        u = np.zeros([cluster_count, n])
        for i in range(cluster_count):
            for k in range(n):
                dik = metric(points[k], v[i])
                sum = 0
                for j in range(cluster_count):
                    sum += (dik / metric(points[k], v[j])) ** (2 / m - 1)
                u[i][k] = 1 / sum
        iteration += 1

    cluster_no = np.argmax(u, axis=0)
    probabilities = np.max(u, axis=0)

    links = makePlots(points, v, probabilities, cluster_no)
    return points, cluster_no, links


# ---- Beispieltests ---- #

if __name__ == '__main__':
    different_metrics = {
        "squared_eucledian": lambda x, y: sum([(a - b) ** 2 for a, b in zip(x, y)]),
        "eucledian": lambda x, y: sum([(a - b) ** 2 for a, b in zip(x, y)]) ** (1 / 2),
        "manhattan": lambda x, y: sum([abs(a - b) for a, b in zip(x, y)]),
        "inverse_eucleadian": lambda x, y: 1 / (sum([(a - b) ** 2 for a, b in zip(x, y)]) ** (1 / 2))
    }

    # example call of function
    wine_data = load_wine()
    inData = np.array(wine_data.get("data"))
    # ATTENTION: Wine dataset has 13 Dimensions => many 13*12 pictures will be generated #
    fuzzyCMeans(inData, cluster_count=3, m=1.1, epsilon=0.01)