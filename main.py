from sklearn.datasets import load_wine

if __name__ == '__main__':
    wine_data = load_wine()

    print(type(wine_data))

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
"""
