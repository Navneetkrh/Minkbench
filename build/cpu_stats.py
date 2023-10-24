import psutil
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
import numpy as np
from itertools import count
import pandas as pd
from matplotlib import style
from data import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

from itertools import count

global x
x = []
global y
y = []


def cpu_usage():
    print("cpu usage is", psutil.cpu_percent())
    return np.random.randint(0, 100)


counter = count(0, 1)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame2")


def relative_to_assets(path: str) -> Path:
    print("Assets path is", ASSETS_PATH / Path(path))
    return ASSETS_PATH / Path(path)


# window = Tk()

# window.geometry("937x693")
# window.configure(bg = "#010101")


def cpu_page(parent):
    usage = 0
    global update

    def update():
        global usage
        new_usage = psutil.cpu_percent()
        x.append(next(counter))
        y.append(new_usage)

        usage = new_usage
        canvas.itemconfig(tagOrId=usage_entry, text=str(new_usage) + "%")
        # only plot last 60 points

        plot()

        canvas.itemconfig(tagOrId=mgraph, figure=fig)

        canvas.after(500, update)

    def plot():
        # x.append(next(counter))
        # y.append(cpu_usage())
        # print("x is",x)
        # print("y is",y)
        # only plot last 30 points
        # if(len(x)>30):
        #     x.pop(0)
        #     y.pop(0)
        # print("len x",len(x))
        # print("len y",len(y))
        # print("x is",x)
        if len(x) > 30:
            x.pop(0)
            y.pop(0)
        # clear the figure
        # fig.clear()

        # ax.plot(x,y)
        ax.cla()
        ax.set_facecolor("#1A1A25")
        ax.fill_between(x, y, alpha=0.5, color="#2b8da3")
        ax.tick_params(axis="both", colors="white")
        ax.grid(color="#A8A4C3", linestyle="dashed", linewidth=0.5)
        mgraph.draw()

    canvas = Canvas(
        parent,
        bg="#010101",
        height=693,
        width=937,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )

    # adding figure badi mehnat se
    global fig
    fig = Figure(figsize=(8.5, 3.5), facecolor="#1A1A25")
    ax = fig.add_subplot()
    ax.set_facecolor("#1A1A25")
    ax.fill_between(x, y, alpha=0.5)
    ax.tick_params(axis="both", colors="white")
    ax.grid(color="#DEBDBF", linestyle="dashed", linewidth=0.5)
    mgraph = FigureCanvasTkAgg(fig, master=canvas)
    mgraph.get_tk_widget().place(x=40, y=75)

    # print path to assets
    print("output path is", OUTPUT_PATH)
    print("my path is", ASSETS_PATH)
    canvas.place(x=290, y=14)

    global image_image_1
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(469.0, 249.0, image=image_image_1)

    global image_image_2
    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(584.0, 478.0, image=image_image_2)

    canvas.create_text(
        485.0,
        466.0,
        anchor="nw",
        text="Temperature",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 20 * -1),
    )

    canvas.create_text(
        363.0,
        16.0,
        anchor="nw",
        text="CPU Stats",
        fill="#FFFFFF",
        font=("Inter Bold", 24 * -1),
    )

    canvas.create_text(
        629.0,
        466.0,
        anchor="nw",
        text="50°C",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 20 * -1),
    )

    global image_image_3
    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(814.0, 478.0, image=image_image_3)

    global image_image_4
    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(354.0, 478.0, image=image_image_4)

    canvas.create_text(
        399.0,
        466.0,
        anchor="nw",
        text="50°C",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 20 * -1),
    )

    canvas.create_text(
        253.0,
        466.0,
        anchor="nw",
        text="Temperature",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 20 * -1),
    )

    global image_image_5
    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(124.0, 478.0, image=image_image_5)

    canvas.create_text(
        169.0,
        466.0,
        anchor="nw",
        text="50°C",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 20 * -1),
    )

    canvas.create_text(
        23.0,
        466.0,
        anchor="nw",
        text="Temperature",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 20 * -1),
    )

    canvas.create_text(
        715.0,
        466.0,
        anchor="nw",
        text="Cpu usage",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 20 * -1),
    )

    usage_entry = canvas.create_text(
        859.0,
        466.0,
        anchor="nw",
        text="50°C",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 20 * -1),
    )
    # get cpu usage

    update()