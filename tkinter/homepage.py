import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()
style = ttk.Style("darkly")

root.geometry("800x600")

# create a sidebar
sidebar = ttk.Labelframe(root, text="Sidebar", bootstyle="info")
sidebar.pack(side="left", fill="y", padx=10, pady=10)

# add buttons to the sidebar
button1 = ttk.Button(sidebar, text="Button 1", bootstyle=PRIMARY)
button1.pack(pady=10)

button2 = ttk.Button(sidebar, text="Button 2", bootstyle=SECONDARY)
button2.pack(pady=10)

# create a main content area
content = ttk.Frame(root, bootstyle="secondary")
content.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# add widgets to the content area
label = ttk.Label(content, text="Main content area", font=("Arial", 16), bootstyle="warning")
label.pack(pady=50)

root.mainloop()