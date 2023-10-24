



from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame5")


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
    338.0,
    14.0,
    anchor="nw",
    text="About",
    fill="#DFBAC7",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    166.0,
    172.0,
    anchor="nw",
    text="Your one-stop solution for CPU monitoring and benchmarking",
    fill="#99999B",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    393.0,
    125.0,
    anchor="nw",
    text="MinkBench",
    fill="#B49497",
    font=("Inter ExtraBold", 36 * -1)
)

canvas.create_text(
    71.0,
    288.0,
    anchor="nw",
    text="A benchmarking and system monitoring software created as a course project for CSL30x0:Operationg Systems.\n\nIt uses\n\nCreated By:\nNavneet Kumar (B21CS050)\nManish (B21CS044)\nSoham Parikh (B21CS074)\nTarun Raj Singh (B21CS076)",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    482.0,
    101.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
