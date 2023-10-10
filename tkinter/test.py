import tkinter as tk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

root = ttkb.Window(themename="darkly")
root.geometry("800x600")
root.title("Mink")


sidebar = ttkb.Frame(root, bootstyle="secondary", width=200)
sidebar.pack(side="left", fill="y", padx=10, pady=10)

content = ttkb.Frame(root, bootstyle="secondary")
content.pack(side="right", fill="both", expand=True, padx=10, pady=10)

topbar = ttkb.Frame(content, bootstyle="dark")
topbar.pack(side="top", fill="x", padx=10, pady=10)

label = ttkb.Label(topbar, text="Welcome to MINK", font=("Arial", 16), bootstyle="SUCCESS", background="#303030")
label.pack(pady=10)

content2 = ttkb.Frame(content, bootstyle="dark")
content2.pack(side="right", fill="both", expand=True, padx=10, pady=10)
button1 = ttkb.Button(sidebar, text="Button 1", bootstyle=SUCCESS)
button1.pack(pady=10, padx=10)

root.mainloop()