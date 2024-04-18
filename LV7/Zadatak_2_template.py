import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("imgs\\test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w, h, d = img.shape
img_array = np.reshape(img, (w * h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

# a)
unique_colors = np.unique(img_array_aprox, axis=0)
print('Broj razlicitih boja: ', len(unique_colors))

# b), c), d), e)
km = KMeans(n_clusters=2, init='random', n_init=5, random_state=0)
km.fit(img_array)

cluster_centers = km.cluster_centers_
labels = km.predict(img_array)

img_array_aprox = cluster_centers[labels]
img_aprox = np.reshape(img_array_aprox, (w, h, d))

plt.figure()
plt.title("Druga slika")
plt.imshow(img_aprox)
plt.tight_layout()
plt.show()

'''
KOMENTAR:
Kada je K=2 na slici mozemo vidjeti samo jednu nijansu plave i zute boje.
K=2 je takodjer i najbolji odabir koji mozemo uzeti, sto mozemo vidjeti i potvrditi iz grafickog prikaza u zadatku f)
'''

# f)
max_clusters = range(1, 10)
distortions = []

for k in (max_clusters):
    kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)
    kmeans.fit(img_array)
    distortions.append(kmeans.inertia_)

plt.figure()
plt.xlabel('Broj grupa K')
plt.ylabel('J')
plt.plot(max_clusters, distortions)
plt.grid(True)
plt.show()

# g)
labels = km.labels_

for cluster_id in range(2):
    cluster_mask = labels.reshape(w, h) == cluster_id

    binary_image = np.zeros((w, h), dtype=np.uint8)
    binary_image[cluster_mask] = 255

    plt.figure()
    plt.title("Binary Image for Cluster {}".format(cluster_id))
    plt.imshow(binary_image, cmap='gray')
    plt.tight_layout()
    plt.show()
