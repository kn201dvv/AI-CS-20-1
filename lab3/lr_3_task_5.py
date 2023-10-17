# -*- coding: utf-8 -*-
"""LR_3_task_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RhAyhqTpVBU_ufnNDCfPOzQdclPBg27g
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Генеруємо випадкові дані
m = 100
X = 6 * np.random.rand(m, 1) - 5
y = 0.7 * X**2 + X + 3 + np.random.randn(m, 1)

# Побудова моделі лінійної регресії
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Побудова моделі поліноміальної регресії
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)

# Виведення коефіцієнтів лінійної регресії
print("Лінійна регресія:")
print("Перехоплення:", lin_reg.intercept_)
print("Коефіцієнт регресії:", lin_reg.coef_)

# Виведення коефіцієнтів поліноміальної регресії
print("Поліноміальна регресія:")
print("Перехоплення:", poly_reg.intercept_)
print("Коефіцієнти регресії:", poly_reg.coef_)


# Виведення даних на графіку
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(X, y, c='b', label='Дані')
plt.plot(X, lin_reg.predict(X), 'r-', linewidth=2, label='Лінійна регресія')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper left')
plt.title('Лінійна регресія')

plt.subplot(1, 2, 2)
X_new = np.linspace(-5, 1, 100).reshape(100, 1)
X_new_poly = poly_features.transform(X_new)
y_new = poly_reg.predict(X_new_poly)
plt.scatter(X, y, c='b', label='Дані')
plt.plot(X_new, y_new, 'r-', linewidth=2, label='Поліноміальна регресія')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper left')
plt.title('Поліноміальна регресія')

plt.show()