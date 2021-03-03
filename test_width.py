import numpy as np
from volume import volume
from area import area
import pandas as pd
import matplotlib.pyplot as plt


def optimal_number(number_points, low, high):
    x = np.random.normal(0, 1, size=(number_points,))
    y = np.random.normal(0, 1, size=(number_points,))
    z = np.random.normal(0, 1, size=(number_points,))
    a = x/np.sqrt((x**2+y**2+z**2))
    b = y/np.sqrt((x**2+y**2+z**2))
    c = z/np.sqrt((x**2+y**2+z**2))
    x = a
    y = b
    z = c
    v = np.array([volume(x, y, z, n_layers=i) for i in range(low, high)])
    return np.argmin(np.abs(v-4.18879))+low


optimal_values = np.array([])
for i in range(100, 2000, 100):
    value = np.array([])
    for j in range(30):
        value = np.append(value, optimal_number(i, 10, int(i/2)))
        print(i/20 + j/600, '%')
    value = np.average(value)
    optimal_values = np.append(optimal_values, value)
    s = pd.Series(optimal_values)
    s.to_csv('values{}.csv'.format(i))
    print(i)
s = pd.Series(optimal_values)
s.to_csv('values1.csv')
