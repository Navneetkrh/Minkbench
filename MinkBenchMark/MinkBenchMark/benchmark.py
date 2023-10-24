

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("937x693")
window.configure(bg = "#010101")


canvas = Canvas(
    window,
    bg = "#010101",
    height = 693,
    width = 937,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    363.0,
    16.0,
    anchor="nw",
    text="Benchmark",
    fill="#DFBAC7",
    font=("Inter Bold", 24 * -1)
)

canvas.create_rectangle(
    322.0,
    198.0,
    666.0,
    325.0,
    fill="#000000",
    outline="")

canvas.create_text(
    335.0,
    216.0,
    anchor="nw",
    text="RUN Benchmark",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    494.0,
    116.0,
    image=image_image_1
)

canvas.create_rectangle(
    556.0,
    211.0,
    657.0,
    313.0,
    fill="#000000",
    outline="")

canvas.create_text(
    363.0,
    252.0,
    anchor="nw",
    text="Completed",
    fill="#99999B",
    font=("MontserratRoman Medium", 16 * -1)
)

canvas.create_rectangle(
    572.0,
    221.0,
    641.0,
    283.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    586.0,
    283.0,
    anchor="nw",
    text="Run",
    fill="#FFFFFF",
    font=("MontserratRoman SemiBold", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    468.0,
    508.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
