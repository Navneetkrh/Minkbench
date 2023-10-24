import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generate_pie_chart():
    # Sample data for the pie chart
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]

    # Create a new figure
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)

    # Create the pie chart
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

    # Create a Tkinter canvas for the figure
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=1, column=0)
    
# Create the main window
window = tk.Tk()
window.title("Pie Chart in Tkinter")

# Create a button to generate the pie chart
generate_button = ttk.Button(window, text="Generate Pie Chart", command=generate_pie_chart)
generate_button.grid(row=0, column=0)

# Start the Tkinter main loop
window.mainloop()