#!/usr/bin/env /home/nwh/.pyenv/shims/python

import numpy as np
import matplotlib.pyplot as pp

def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y

x = np.arange(-10, 10, 0.1)
y = sigmoid(x)

pp.plot(x, y)
pp.show()
