# -*- coding: utf-8 -*-
"""LR_4_task_1_rf.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h-G0lYKLZzfJwsS30PUOyj75_cyI_0IY
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report
from sklearn import model_selection

from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier

from sklearn.metrics import classification_report
from utilities import visualize_classifier

#Парсер аргументів
import argparse

def build_arg_parser():
    parser = argparse.ArgumentParser(description='Classify data using Ensemble Learning techniques')

    parser.add_argument('--classifier-type',
                        dest='classifier_type',
                        required=True,
                        choices=['rf', 'erf'],
                        help="Type of classifier to use; can be either 'rf' or 'erf'")

    return parser

if __name__ == "__main__":
    import argparse
    import sys

    sys.argv = [sys.argv[0], '--classifier-type', 'rf']
    # Вилучення вхідних аргументів
    args = build_arg_parser().parse_args()
    classifier_type = args.classifier_type

# Завантаження вхідних даних
import numpy as np

input_file = 'data_random_forests.txt'

data = np.loadtxt(input_file, delimiter=',')

X, y = data[:, :-1], data[:, -1]

# Розбиття вхідних даних на три класи
class_0 = np.array(X[y == 0])
class_1 = np.array(X[y == 1])
class_2 = np.array(X[y == 2])

# Візуалізація вхідних даних
import matplotlib.pyplot as plt

plt.figure()

plt.scatter(class_0[:, 0], class_0[:, 1], s=75,
            facecolors='white', edgecolors='black',
            linewidth=1, marker='s')

plt.scatter(class_1[:, 0], class_1[:, 1], s=75,
            facecolors='white', edgecolors='black',
            linewidth=1, marker='o')

plt.scatter(class_2[:, 0], class_2[:, 1], s=75,
            facecolors='white', edgecolors='black',
            linewidth=1, marker='*')

plt.title('Вхідні дані')
plt.show()

# Розбивка даних на навчальний та тестовий набори
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=5)

# Класифікатор на основі ансамблевого навчання
params = {'n_estimators': 100, 'max_depth': 10, 'random_state': 0}

# Навчання та візуалізація класифікатора на тренувальних та тестових даних
if classifier_type == 'rf':
    classifier = RandomForestClassifier(**params)
else:
    classifier = ExtraTreesClassifier(**params)

classifier.fit(X_train, y_train)
visualize_classifier(classifier, X_train, y_train)
y_test_pred = classifier.predict(X_test)
visualize_classifier(classifier, X_test, y_test)

# Перевірка роботи класифікатора
class_names = ['Class-0', 'Class-1', 'Class-2']
print("\n" + "#" * 40)
print("\nClassifier performance on training dataset\n")
print(classification_report(y_train, classifier.predict(X_train), target_names=class_names))
print("#" * 40 + "\n")

print("#" * 40)
print("\nClassifier performance on test dataset\n")
print(classification_report(y_test, y_test_pred, target_names=class_names))
print("#" * 40 + "\n")

# Обчислення параметрів довірливості
test_datapoints = np.array([[5, 5], [3, 6], [6, 4], [7, 2], [4, 4], [5, 11]])

# Визначення довірливості класифікатора для тестових даних та виведення результатів
print("\nConfidence measure:")
for datapoint in test_datapoints:
    probabilities = classifier.predict_proba([datapoint])[0]
    predicted_class = 'Class-' + str(np.argmax(probabilities))
    print('\nDatapoint:', datapoint)
    print('Predicted class:', predicted_class)

# Візуалізація точок даних
visualize_classifier(classifier, test_datapoints, [0, 0, 1, 1, 2, 0])
plt.show()