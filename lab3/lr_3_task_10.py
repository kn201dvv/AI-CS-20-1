# -*- coding: utf-8 -*-
"""LR_3_task_10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kr1Lc0BgozqybM2H1z8nRD60QPJUTXm5
"""

import datetime
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.covariance import GraphicalLassoCV
from sklearn import cluster
import yfinance as yf


# Вхідний файл із символічними позначеннями компаній
input_file = 'company_symbol_mapping.json'

# Завантаження прив'язок символів компаній до їх повних назв
with open(input_file, 'r') as f:
    company_symbols_map = json.loads(f.read())
symbols, names = np.array(list(company_symbols_map.items())).T

# Вказані дати
start_date = datetime.datetime(2003, 7, 3)
end_date = datetime.datetime(2007, 5, 4)

# Вибір котирувань
quotes = [yf.download(symbol, start=start_date, end=end_date) for symbol in symbols]
# Вилучення котирувань, що відповідають відкриттю та закриттю біржі
opening_quotes = np.array([quote['Open'] for quote in quotes]).astype(float)
closing_quotes = np.array([quote['Close'] for quote in quotes]).astype(float)

# Обчислення різниці між двома видами котирувань
quotes_diff = closing_quotes - opening_quotes

# Нормалізація даних
X = quotes_diff.copy().T
X /= X.std(axis=0)

# Створення моделі графа
edge_model = GraphicalLassoCV()

# Навчання моделі
with np.errstate(invalid="ignore"):
    edge_model.fit(X)

# Створення моделі кластеризації на основі поширення подібності, використовуючи щойно навчену крайову модель
_, labels = cluster.affinity_propagation(edge_model.covariance_)
num_labels = labels.max()

# Виведення результатів
for i in range(num_labels + 1):
    print("Cluster", i + 1, ',', ', '.join(names[labels == i]))