import tkinter as tk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

root = ttkb.Window(themename="darkly")
root.geometry("800x600")
root.title("Mink")

my_frame=ttkb.Frame(root,bootstyle="success")
my_frame.pack(pady=10)

my_entry = ttkb.Entry(my_frame, font=("Helvetica, 18"))
my_entry.pack(pady=10, padx=10)

label=ttkb.Label(my_frame,text="Mink",bootstyle="success, inverse",font=("Arial", 30))
label.pack(pady=10)

button=ttkb.Button(my_frame,text="Mink",bootstyle="danger,outline,round, inverse",command=lambda:print("Mink"))
button.pack(pady=10)


var1=tk.IntVar()

def checker():
    if var1.get()==1:
        print("checked")
    else:

        print("unchecked")
checker=ttkb.Checkbutton(root,text="Mink",bootstyle="success",variable=var1,command=checker,onvalue=1,offvalue=0)
checker.pack(pady=10)

def starter():
    progreebar.start()  

def stopper():
    progreebar.stop()

def incrementer():
    progreebar.step(10)
    my_label.config(text=f"{progreebar.variable.get()}")

progreebar=ttkb.Floodgauge(root,bootstyle="success",mask="Pos:{}%",maximum=100 , mode = "determinate")
progreebar.pack(pady=10,fill="x",padx=30)

start_b = ttkb.Button(root, text='Start', bootstyle=PRIMARY, command=starter)
start_b.pack(pady=10)

stop_b = ttkb.Button(root, text='Stop', bootstyle=SECONDARY, command=stopper)
stop_b.pack(pady=10)

increment_b = ttkb.Button(root, text='Increment', bootstyle=SUCCESS, command=incrementer)

increment_b.pack(pady=10)

my_label = ttkb.Label(root, text="Progress ", bootstyle=WARNING)
my_label.pack(pady=10)
gola=ttkb.Meter(my_frame,bootstyle="warning",amountused=37,amounttotal=100)
gola.pack(pady=10)
root.mainloop()

