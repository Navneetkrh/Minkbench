import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from itertools import count 
import pandas as pd
from matplotlib import style

df=pd.read_csv('data.csv')
x=[]
y=[]

fig, ax = plt.subplots()

# ax.plot(x,y)

counter=count(0,1)

def cpu_usage():

    return np.random.randint(0,100)
def update(i):
    # idx=next(counter)
#    append time and cpu usage to x and y
    x.append(next(counter))
    y.append(cpu_usage())
    if(len(x)>20):
            x.pop(0)
            y.pop(0)
    plt.cla()
    ax.plot(x,y)
    plt.pause(0.001)
ani=FuncAnimation(fig=fig,func=update,interval=200,frames=10)
plt.show() 