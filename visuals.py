import matplotlib.pyplot as plt

# jede Dimension mit jeder darstellen (also alle Kombinationen in 2D)
def makePlots(dataKoords, centerKoords, wk, clusters):

    anzDimensionen = len(dataKoords[0])
    koords = []
    links = []
    i, j = 0, 0

    while(i<anzDimensionen):
        while(j<anzDimensionen):
            if(i!=j):
                koords = [(k[i], k[j]) for k in dataKoords]
                centers = [(c[i], c[j]) for c in centerKoords]
                links.append(makePlot(koords, wk, clusters, centers, i, j))
                j+=1
            else:
                j+=1
        i+=1
        j=0
    return links

   
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

    # Farben fuer Cluster   (20 Farben, ab der 21. wieder oben anfangen) NUR MIT DIEEEESEN FARBEN!!!!111!!11ELF!
    colours = [
        "#6495ED",          # corn flower blue
        "#9400D3",          # dark violet
        "#FFA500",          # orange
        "#3CB371",          # medium sea green
        "#00FF00",          # lime
        "#8B4513",          # saddle brown
        "#87CEFA",          # light sky blue
        "#FF0000",          # red
        "#000080",          # navy
        "#FF00FF",          # fuchsia
        "#0000FF",          # blue
        "#008000",          # green
        "#4B0082",          # indigo
        "#6A5ACD",          # slate blue
        "#FF1493",          # deep pink
        "#800080",          # purple
        "#D2691E",          # chocolate
        "#00FFFF",          # cyan
        "#F4A460",          # sandy brown
        "#FFFF00"           # yellow
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

    name = "visual_dim" + str(dimension1) + "xdim" + str(dimension2) + ".jpg"
    plt.savefig(name)
    plt.close()
    return name