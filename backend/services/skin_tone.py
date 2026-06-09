import numpy as np
from sklearn.cluster import KMeans

def detect_skin_tone(img):
    pixels = img.reshape(-1, 3)
    kmeans = KMeans(n_clusters=3).fit(pixels)
    dominant = np.mean(kmeans.cluster_centers_, axis=0)

    if dominant[0] > 200:
        return "Fair"
    elif dominant[0] > 120:
        return "Medium"
    else:
        return "Dark"
