#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plot

def softmap(x):
    c = x.max()
    i = x - c
    k = np.exp(i)
    s = k.sum()
    return k / s

x = np.arange(-10, 10, 0.1)
m = 0 - x * x
plot.plot(x, m)
plot.show()

y = softmap(m)

plot.plot(x, y)
plot.show()
