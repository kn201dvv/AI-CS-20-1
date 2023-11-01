# -*- coding: utf-8 -*-
"""LR_6_task_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tZrwssh1-niwA-Fq5sWR1fypyOleKQVX
"""

!pip install neurolab

import numpy as np
import neurolab as nl
target = [[-1, 1, -1, -1, 1, -1, -1, 1, -1],
 [1, 1, 1, 1, -1, 1, 1, -1, 1],
 [1, -1, 1, 1, 1, 1, 1, -1, 1],
 [1, 1, 1, 1, -1, -1, 1, -1, -1],
 [-1, -1, -1, -1, 1, -1, -1, -1, -1]]
input = [[-1, -1, 1, 1, 1, 1, 1, -1, 1],
 [-1, -1, 1, -1, 1, -1, -1, -1, -1],
 [-1, -1, -1, -1, 1, -1, -1, 1, -1]]
# Створення та тренування нейромережі
net = nl.net.newhem(target)
output = net.sim(target)
print("Test on train samples (must be [0, 1, 2, 3, 4])")
print(np.argmax(output, axis=0))
output = net.sim([input[0]])
print("Outputs on recurent cycle:")
print(np.array(net.layers[1].outs))
output = net.sim(input)
print("Outputs on test sample:")
print(output)