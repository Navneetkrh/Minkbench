import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
     FigureCanvasTkAgg)
import tkinter as tk
import numpy as np
from itertools import count 
x=[]
y=[]
def cpu_usage():

    return np.random.randint(0,100)
counter=count(0,1)
def plot():
    x.append(next(counter))
    y.append(cpu_usage())
    ax.plot(x,y)
    canvas.draw()


# initialize tkinter
root= tk.Tk()
fig,ax=plt.subplots()


# tkinter app
frame=tk.Frame(root)
label=tk.Label(frame,text="CPU Usage")
label.config(font=("Courier", 44))
label.pack()


canvas=FigureCanvasTkAgg(fig,master=frame)
canvas.get_tk_widget().pack()
frame.pack()

tk.Button(frame,text="plot graph",command=lambda: plot()).pack()
root.mainloop()