# -*- coding: utf-8 -*-
"""LR_8_task_7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/190w5LbIaxnN6t4Kk3Z2NN6sKTg5HRjkq
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Зчитування зображення
img = cv2.imread('coins.jpg')

# Додавання контрастності
img = cv2.convertScaleAbs(img, alpha=0.8, beta=20)

# Перетворення в градації сірого
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Бінаризація та видалення шуму
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Знаходження контурів монет
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Визначення мінімальної площі контуру для фільтрації
min_contour_area = 30

# Фільтрація за розміром монет
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

# Визначення діаметрів
diameters = []

# Прохід по кожному контуру і визначення діаметра
for contour in filtered_contours:
    # Отримання прямокутника, що обрамлює контур
    x, y, w, h = cv2.boundingRect(contour)

    # Визначення діаметра (може бути адаптовано до реального розміру монет)
    diameter = max(w, h)
    diameters.append(diameter)

# Знаходження найбільш схожих діаметрів
similar_diameters = []
for i in range(len(diameters)):
    for j in range(i + 1, len(diameters)):
        if abs(diameters[i] - diameters[j]) < 10:  # Адаптувати поріг відповідно до потреб
            similar_diameters.append((i, j))

# Створення чорного зображення для відображення монет
segmented_coins = np.zeros_like(img)

# Фарбування пар монет у спільний колір
for pair in similar_diameters:
    color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
    cv2.drawContours(segmented_coins, [filtered_contours[pair[0]], filtered_contours[pair[1]]], -1, color, -1)

# Відображення результату та оригінального зображення
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(segmented_coins)
plt.title('Segmented Coins')

plt.show()