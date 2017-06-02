#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as pp

def relu(x):
    return np.maximum(0, x)

x = np.arange(-20, 20, 0.1)
y = relu(x)

pp.plot(x, y)
pp.show()
