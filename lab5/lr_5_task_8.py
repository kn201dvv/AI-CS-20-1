# -*- coding: utf-8 -*-
"""LR_5_task_8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UhzrMYPgOFVkblNrGIR-PsBCBO-1qXz7
"""

!pip install neurolab

import numpy as np
import neurolab as nl
import numpy.random as rand

# Задання центрів кластерів
centr = np.array([[0.2, 0.2], [0.4, 0.4], [0.3, 0.3], [0.2, 0.6], [0.5, 0.7]])

# Стандартне відхилення для генерації даних
skv = 0.03

# Генерація даних навколо центрів кластерів
rand_norm = skv * rand.randn(100, centr.shape[0], 2)
inp = np.array([centr + r for r in rand_norm])
inp.shape = (100 * centr.shape[0], 2)
rand.shuffle(inp)

# Створення нейронної мережі з 2 входами та 4 нейронами
net = nl.net.newc([[0.0, 1.0], [0.0, 1.0]], 4)

# Навчання мережі за допомогою методу CWTA
error = net.train(inp, epochs=200, show=20)

# Побудова графіків
import pylab as pl
pl.title('Classification Problem')
pl.subplot(211)
pl.plot(error)
pl.xlabel('Номер епохи')
pl.ylabel('Помилка (за замовчуванням MAE)')
w = net.layers[0].np['w']
pl.subplot(212)
pl.plot(inp[:, 0], inp[:, 1], '.', \
        centr[:, 0], centr[:, 1], 'yv', \
        w[:, 0], w[:, 1], 'p')
pl.legend(['Навчальні приклади', 'Справжні центри', 'Центри мережі'])
pl.show()

import numpy as np
import neurolab as nl
import numpy.random as rand

# Задання центрів кластера
centr = np.array([[0.2, 0.2], [0.4, 0.4], [0.3, 0.3], [0.2, 0.6], [0.5, 0.7]])

# Стандартне відхилення для генерації даних
skv = 0.03

# Генерація даних навколо центрів кластера
rand_norm = skv * rand.randn(100, centr.shape[0], 2)
inp = np.array([centr + r for r in rand_norm])
inp.shape = (100 * centr.shape[0], 2)
rand.shuffle(inp)

# Створення нейронної мережі з 2 входами та 5 нейронами
net = nl.net.newc([[0.0, 1.0], [0.0, 1.0]], 5)

# Навчання мережі за допомогою методу CWTA
error = net.train(inp, epochs=200, show=20)

# Побудова графіків
import pylab as pl
pl.title('Classification Problem')
pl.subplot(211)
pl.plot(error)
pl.xlabel('Номер епохи')
pl.ylabel('Помилка (за замовчуванням MAE)')
w = net.layers[0].np['w']
pl.subplot(212)
pl.plot(inp[:, 0], inp[:, 1], '.', \
        centr[:, 0], centr[:, 1], 'yv', \
        w[:, 0], w[:, 1], 'p')
pl.legend(['Навчальні приклади', 'Справжні центри', 'Центри мережі'])
pl.show()