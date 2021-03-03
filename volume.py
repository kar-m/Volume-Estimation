import numpy as np
from sklearn.decomposition import PCA
from area import area

def volume(x, y, z, projection, n_layers=12, n_points=20):
    # find the principal component (use sklearn PCA)
    A = np.concatenate((x, y, z))
    A = A.reshape((-1, 3))
    pca = PCA(3)
    pca.fit(A)
    B = pca.transform(A)
    dir = pca.components_[0]
    first = A[np.argmax(B[:, 0])]
    last = A[np.argmin(B[:, 0])]
    vect = A[np.argmax(B[:, 1])]

    width = np.linalg.norm(first - last) / n_layers

    # set basis vectors of the planes
    a = np.cross(dir, vect)
    b = np.cross(dir, a)
    a /= np.linalg.norm(a)
    b /= np.linalg.norm(b)

    # find the points within distance of threshold
    def points_near_plane(points, direction, c, threshold):
        distances = (points @ direction - c) / np.linalg.norm(direction)
        mask = distances < 0
        distances = distances[mask]
        distances = np.abs(distances)
        points = points[mask]
        if projection == 'layers':
            return points[distances < threshold], threshold
        elif projection == 'points':
            mask = np.argsort(distances)
            mask = mask[:n_points]
            return points[mask], np.max(distances[mask])

    def project_points(points, direction, b1, b2):
        v = points
        x = (v @ b1) / np.linalg.norm(b1) ** 2
        y = (v @ b2) / np.linalg.norm(b2) ** 2
        return x, y

    volume = 0
    s = 0
    c = np.dot(first, dir)
    if projection=='layers': loop_length = n_layers
    elif projection=='points': loop_length = int(len(x)/n_points)
    for i in range(loop_length):
        points, step = points_near_plane(A, dir, c, width)
        x, y = project_points(points, dir, a, b)
        #plt.scatter(x, y)
        #plt.show()
        if i == int(loop_length//2):
          plt.scatter(x, y)
          plt.show()
        if len(x) > 3:
            s = area(x, y)
        volume += s * step
        c -= step
    return volume
