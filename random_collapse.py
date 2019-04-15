import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from numpy.random import choice



nt = np.linspace(1,10,10)
pn = [0, 0, 0, 0.1, 0.2, 0.4, 0.2, 0.1, 0, 0]

print(nt)
print(pn)

draw = choice(nt, 9, p=pn)
print(draw)
