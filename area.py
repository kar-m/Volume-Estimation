import numpy as np


def area(x, y):
    x -= np.average(x)
    y -= np.average(y)

    # sort the points, assuming the curve can be projected
    # onto a circle bijectively on almost all points
    phi = np.arctan2(y, x)
    mask = np.argsort(phi)
    x = x[mask]
    y = y[mask]

    def triangle_area(p1, p2, p3):
        p1 = np.array(p1)
        p2 = np.array(p2)
        p3 = np.array(p3)

        # calculating the area of the triangle according to Heron's formula
        a = np.linalg.norm(p1 - p2)
        b = np.linalg.norm(p2 - p3)
        c = np.linalg.norm(p3 - p1)
        s = (a + b + c) / 2

        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        return area

    def total_area(x, y):
        area = 0
        center = np.average(x), np.average(y)

        # divide the shape into triangles and add up
        # their areas to get the total area of the shape

        for i in range(len(x)):
            p1 = x[i - 1], y[i - 1]
            p2 = x[i], y[i]
            p3 = center
            area += triangle_area(p1, p2, p3)

        return area

    return total_area(x, y)
