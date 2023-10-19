# -*- coding: utf-8 -*-
"""lr_4_task_7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GSyo4xlXsJW9XMdwpi7uLyPAadppdPHI
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

# Вхідні дані
import numpy as np

X = np.array([
    [2.1, 1.3],  [1.3, 3.2],  [2.9, 2.5],
    [2.7, 5.4],  [3.8, 0.9],  [7.3, 2.1],
    [4.2, 6.5],  [3.8, 3.7],  [2.5, 4.1],
    [3.4, 1.9],  [5.7, 3.5],  [6.1, 4.3],
    [5.1, 2.2],  [6.2, 1.1]
])

#кількість найближчих сусідів, котрі хочемо витягти.
k=5

# Тестова точка даних
test_datapoint = [4.3,2.7]

# Відображення вхідних даних на графіку
plt.figure()
plt.title('Вхідні дані')
plt.scatter(X[:, 0], X[:, 1], marker='o', s=75, color="black")

# Побудова моделі на основі методу k найближчих сусідів
from sklearn.neighbors import NearestNeighbors

knn_model = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(X)
distances, indices = knn_model.kneighbors(X)

# Виведемо 'k' найближчих сусідів
print("\nK Nearest Neighbors: ")
for rank, index in enumerate(indices[0][:k], start=1):
    print(str(rank) + " ==> " + str(X[index]))

import matplotlib.pyplot as plt

plt.figure()
plt.title('Найближчі сусіди')

# Виведемо всі точки
plt.scatter(X[:, 0], X[:, 1], marker='o', s=75, color='k', label='Навчальні точки')

# Виведемо найближчі сусіди для тестової точки
plt.scatter(X[indices][0][:, 0], X[indices][0][:, 1], marker='o', s=250, color='k', facecolors='none', label='Найближчі сусіди')

# Виведемо тестову точку
plt.scatter(test_datapoint, test_datapoint, marker='x', s=75, color='r', label='Тестова точка')

# Додамо легенду для пояснень
plt.legend()

plt.show()