


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from app import main_page



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets//frame6")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

splashroot= Tk()
splashroot.title("Mink")
splashroot.geometry("1280x720")
splashroot.configure(bg = "#010101")


canvas = Canvas(
    splashroot,
    bg="#010101",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
global button_image_1
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: main_page(splashroot= splashroot),
    relief="flat",
)
button_1.place(x=495.0, y=597.0, width=304.0, height=73.0)

canvas.create_text(
    278.0,
    392.0,
    anchor="nw",
    text="Your one-stop solution for CPU monitoring and benchmarking",
    fill="#99999B",
    font=("Inter Bold", 24 * -1),
)

canvas.create_text(
    467.0,
    302.0,
    anchor="nw",
    text="MinkBench",
    fill="#B49497",
    font=("Inter ExtraBold", 64 * -1),
)

global image_image_1
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(647.0, 251.0, image=image_image_1)

splashroot.resizable(False, False)
mainloop()
