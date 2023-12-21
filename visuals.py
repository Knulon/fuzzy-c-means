import numpy as np
import pygame 
import matplotlib.pyplot as plt
import input

# Eingabe:
#      Array 1 = [ (x0, y0), (x1, y1), (x2, y2), ... ]         --> Koordinaten
#      Array 2 = [ 0.6, 0.6, 0.6, ... ]                        --> Cluster-Wahrscheinlichkeiten
#      Array 3 = [ A0, A1, A2, ... ]                           --> zugehoerige Cluster


def makePlot(koords, wk, clusters):
#     print("Koordinaten: \n", koords, "\n")
#     print("Cluster: \t", clusters, "\n")
#     print("Wahrscheinlichkeiten: \t", wk)


    # Farben fuer Cluster   (20 Farben, ab der 21. wieder oben anfangen)
    colours = [
        "#FF0000",          # rot
        "#FFA500",          # orange
        "#FFFF00",          # gelb
        "#008000",          # gruen
        "#00FF00",          # lime
        "#3CB371",          # medium sea green
        "#00FFFF",          # cyan
        "#6495ED",          # corn flower blue
        "#87CEFA",          # light sky blue
        "#000080",          # navy
        "#0000FF",          # blue
        "#4B0082",          # indigo
        "#6A5ACD",          # slate blue
        "#9400D3",          # dark violet
        "#800080",          # purple
        "#FF00FF",          # fuchsia
        "#FF1493",          # deep pink
        "#8B4513",          # saddle brown
        "#D2691E",          # chocolate
        "#F4A460"           # sandy brown
    ]
        
    fig, ax = plt.subplots()
    ax.set_title("Fuzzy c-Means")

    j = 0
    for i in koords:
       x, y = i[0], i[1]
       c = clusters[j]
       w = wk[j]
       j+=1

       ax.scatter(x,y, c=(colours[c%20], w))

    plt.savefig("output_visuals.jpg")


if __name__ == '__main__':
    koords, wk, clusters = input.createSet(True)
    makePlot(koords, wk, clusters) 