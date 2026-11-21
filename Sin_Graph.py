"""A file to hold the code for creating the sin graph while not using the sin function. My plan is to
use the derivative of sin which is cos and just add cos to the x value mod 2pi"""

import matplotlib.pyplot as plt
from math import *

x_values = range(0, 400)
x_values = [(i/10) for i in x_values]
y_values = [x*x*sqrt(3)/2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=3)

#set chart title and label axes.
ax.set_title("Area of an equilateral triangle", fontsize=24)
ax.set_xlabel("Base Length", fontsize=14)
ax.set_ylabel("Area", fontsize=14)

#set the range for each axis.
ax.axis([0, 30, -1, 100])

plt.show()