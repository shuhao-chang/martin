import matplotlib.pyplot as plt
import numpy as np
import math
x= np.linspace(-10,10)
a=[]
for i in range(50):  
    a.append(x[i]-1-(math.sin(x[i])))
plt.plot(x,a, color ="red")
plt.title("函數圖形")
plt.xlabel("x")
plt.ylabel("f(x)")
