## 1. Why Learn Calculus? ##

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,3,301)
y = -(x**2)+3*x-1
plt.plot(x,y)

## 4. Math Behind Slope ##

def slope(x1,x2,y1,y2):
    delta_x = x2-x1
    delta_y = y2-y1
    return delta_y/delta_x

slope_one = slope(0,4,1,13)
slope_two = slope(5,-1,16,-2)



## 6. Secant Lines ##

import seaborn
seaborn.set(style='darkgrid')

def draw_secant(x_values):
    x = np.linspace(-20,30,100)
    y = -1*(x**2) + x*3 - 1
    plt.plot(x,y)
    x2 = x_values[1]
    x1 = x_values[0]
    y2 = -1*(x2**2) + x2*3 - 1
    y1 = -1*(x1**2) + x1*3 - 1
    m = (y2-y1)/(x2-x1)
    b = y2-m*x2
    y_secant = m*x+b
    plt.plot(x,y_secant,color="g")
    plt.show()

x_values1 = [3,5]
x_values2 = [3,10]
x_values3 = [3,15]

draw_secant(x_values1)
draw_secant(x_values2)
draw_secant(x_values3)
