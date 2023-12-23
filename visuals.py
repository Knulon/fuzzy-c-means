import matplotlib.pyplot as plt
import input

# jede Dimension mit jeder darstellen (also alle Kombinationen in 2D)
def makePlots(dataKoords, centerKoords, wk, clusters):

    anzDimensionen = len(dataKoords[0])
    koords = []
    i, j = 0, 0

    while(i<anzDimensionen):
        while(j<anzDimensionen):
            if(i!=j):
                koords = [(k[i], k[j]) for k in dataKoords]
                centers = [(c[i], c[j]) for c in centerKoords]
                makePlot(koords, wk, clusters, centers, i, j)
                j+=1
            else:
                j+=1
        i+=1
        j=0        

   
"""
    koords:     [ (x0, y0), (x1, y1), (x2, y2), ... ]         --> Koordinaten der 2 Dimensionen
    wk:         [ 0.6, 0.6, 0.6, ... ]                        --> Cluster-Wahrscheinlichkeiten für Punkte
    clusters:   [ A0, A1, A2, ... ]                           --> zugehoerige Cluster
    centers:    [ (x0, y0), (x1, y1), (x2, y2), ... ]         --> Koordinaten der Clusterzentren der 2 Dimensionen
"""

def makePlot(koords, wk, clusters, centers, dimension1, dimension2):

    # Skalieren des Alphawertes für den Output von 0.2f bis 1.0f, um die Sichbarkeit sicherzustellen
    max_val, min_val, max_wk, min_wk = 1, 0.2, max(wk), min(wk)
    
    if(max_wk != min_wk):
        scaled_array = [(val - min_wk) / (max_wk - min_wk) * (max_val - min_val) + min_val for val in wk]
    else:
        if(max_wk > 0.2):
            scaled_array = wk
        else:
            scaled_array = [0.5 for val in wk]

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
    ax.set_xlabel("Dimension " + str(dimension1), fontsize=10)
    ax.set_ylabel("Dimension " + str(dimension2), fontsize=10)

    j = 0
    for x, y in koords:
       c = clusters[j]
       w = scaled_array[j]
       j+=1

       ax.scatter(x, y, s=20, c=(colours[c%20]), alpha=w, marker='o', edgecolors='face')

    j = 0
    for x, y in centers:
        ax.scatter(x, y, s=50, c=colours[j%20], marker='^', edgecolors="grey")
        j+=1

    plt.savefig("visual_dim" + str(dimension1) + "xdim" + str(dimension2) + ".jpg")
 

if __name__ == '__main__':
    #koords, wk, clusters = input.createSet(True)
    #makePlot(koords, wk, clusters) 
    makePlots([(1,0,0), (0,1,0),(1,0.75,0.5),(3,2,2),(2,3,2),(0,1,2), (0,1.5,2)], [(0,0,0), (2,2,2), (0, 1.5, 1.5)], [0.5, 0.5, 0.9, 0.8, 0.8, 0.6, 0.9], [0,0,0,1,1,2,2])