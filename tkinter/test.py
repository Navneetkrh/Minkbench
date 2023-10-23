import tkinter as tk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

root = ttkb.Window(themename="darkly")
# root.geometry("800x600")
root.title("Mink")


sidebar = ttkb.Frame(root, bootstyle="secondary", width=500)
sidebar.pack(side="left", fill="y", padx=10, pady=10)

content = ttkb.Frame(root, bootstyle="secondary")
content.pack(side="right", fill="both", expand=True, padx=10, pady=10)

topbar = ttkb.Frame(content, bootstyle="dark")
topbar.pack(side="top", fill="x", padx=10, pady=10)

label = ttkb.Label(topbar, text="Welcome to MINK", font=("Arial", 16), bootstyle="SUCCESS", background="#303030")
label.pack(pady=10)

content2 = ttkb.Frame(content, bootstyle="dark")
content2.pack(side="right", fill="both", expand=True, padx=10, pady=10)
button1 = ttkb.Button(sidebar, text="Button 1", bootstyle=SUCCESS, width=30)
button1.pack(pady=10, padx=10)

content3 = ttkb.Frame(content2, bootstyle="dark")
content3.pack(  pady=10 , anchor="w")
content4 = ttkb.Frame(content2, bootstyle="dark")
content4.pack(anchor="w")

gola=ttkb.Meter(content3,bootstyle="warning",amountused=37,amounttotal=100, metersize=300,stripethickness=2,meterthickness=50)
gola.pack( padx=10, side="left", anchor="nw")
gola2=ttkb.Meter(content3,bootstyle="info",amountused=37,amounttotal=100, metersize=300,stripethickness=10,meterthickness=50)
gola2.pack( padx=10, side="right", anchor="ne")
gola3=ttkb.Meter(content4,bootstyle="success",amountused=37,amounttotal=100, metersize=300,stripethickness=10,meterthickness=50)
gola3.pack( padx=10, side="left", anchor="sw")
gola4=ttkb.Meter(content4,bootstyle="danger",amountused=37,amounttotal=100, metersize=300,stripethickness=10,meterthickness=50)
gola4.pack( padx=10, side="right", anchor="se")

# gola.grid(row=0, column=0, sticky="w", pady=10, padx=10)
# gola2.grid(row=0, column=1, sticky="e", pady=10, padx=10)
# gola3.grid(row=1, column=0, sticky="w", pady=10, padx=10)
# gola4.grid(row=1, column=1, sticky="e", pady=10, padx=10)
root.mainloop()