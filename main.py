import numpy as np
from sklearn.datasets import load_wine,load_iris, load_digits
import random


def npArrToString(arr):
    return "[" + ",".join([str(i) for i in arr]) + "]"


def visualisieren(points: np.array, wahrscheinlichkeiten: np.array, clusterNr: np.array, clusterMittelpunkte: np.array) -> [str]:
    return ["toller/link.png"]


def fuzzyCMeans(points, clusterCount, m, metrik=(lambda x, y: sum([(a - b) ** 2 for a, b in zip(x, y)])),
                epsilon=0.0000001, init=None, max_iteration=100):
    # np.linalg.norm()
    # u matrix
    # v matrix
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
    # https://stackoverflow.com/questions/43644320/how-to-make-numpy-array-column-sum-up-to-1

    while np.linalg.norm(u - last_u) > epsilon:
        print("--------------------")
        # print(np.linalg.norm(u - last_u))
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

    print(f"Iterationen: {iteration}")
    # u /= u.sum(axis=1, keepdims=1)
    print(u.sum(axis=1, keepdims=1))
    clusterNr = np.argmax(u, axis=0)
    wahrscheinlichkeiten = np.max(u, axis=0)

    #print(len(clusterNr))
    #print(npArrToString( clusterNr))
    print(v)
    #print(u)
    # return something
    links = visualisieren(points, clusterNr, wahrscheinlichkeiten)
    print("clusternummern:")
    print(clusterNr)
    print("Wahrscheinlichkeiten:")
    print(wahrscheinlichkeiten)
    """
    return points, clusterNr, links


"""
grober Aufbau:
def fuzzyCMeans(data, K_elemente=DEFAULT, metrik=DEFAULT, initialisierungsart=DEFAULT):
    np_array_mit_Clusterzugehörigkeiten = # some hard calculation
    gefilterte_daten = [für jeden Punkt Koordianten + eine die Nr. des Clusters und die WK dafür] # (3 Einträge pro Zeile)
    links_zu_den_Bildern = speicher(visualisieren(gefilterte_daten), name_des_bilds)
    return np_array_mit_Clusterzugehörigkeiten (Koordinaten + Cluster), links_zu_den_Bildern

def visualisieren(gefilterte_daten):
    k Farben wählen (Anzahl an Clustern)
    für jeden Punkt einen Punkt aus gefilterte_daten:
        plotten mit wk als Stärke der Farbe
    return links

https://hackernoon.com/de/Die-16-besten-Sklearn-Datens%C3%A4tze-zum-Erstellen-von-Modellen-f%C3%BCr-maschinelles-Lernen
https://de.wikipedia.org/wiki/Fuzzy-c-Means-Algorithmus#cite_note-2
"""

if __name__ == '__main__':

    wine_data = load_wine()
    """
    print(type(wine_data.get('data')))
    print(wine_data.get('data')[0])

    print(type(wine_data))
    """
    different_metrics = {
        "squared_eucledian": lambda x, y: sum([(a - b) ** 2 for a, b in zip(x, y)]),
        "eucledian": lambda x, y: sum([(a - b) ** 2 for a, b in zip(x, y)]) ** (1 / 2),
        "manhattan": lambda x, y: sum([abs(a - b) for a, b in zip(x, y)]),
        "inverse_eucleadian": lambda x, y: 1 / (sum([(a - b) ** 2 for a, b in zip(x, y)]) ** (1 / 2)),
        "minkowski": lambda x, y, p: sum([(a - b) ** p for a, b in zip(x, y)]) ** (1 / p)
    }

    #print(wine_data.get("target_names"))
    #print(wine_data.get("target"))
    banknoten = [[float(i) for i in line.split(" ")] for line in open("data.txt").readlines()]
    # print(banknoten)
    inData = np.array(banknoten)

    inArr = np.array(
        [[195, 170], [163, 210], [229, 203], [487, 443], [439, 486], [514, 483], [380, 287], [343, 312], [309, 353],
         [199, 195], [480, 467]])
    # fuzzyCMeans(inData, clusterCount=2, m=1.1, epsilon=0.01)
    fuzzyCMeans(inArr, clusterCount=2, m=1.1, epsilon=0.01)
    # digits = load_digits()
    # print(npArrToString(digits.get("target")))
    # fuzzyCMeans(digits.get("data"), clusterCount=10, m=1.1, epsilon=0.01)



