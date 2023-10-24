
from cpu_stats import cpu_page

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def handle_button_press(btn_name):
    global current_window
    if btn_name == "cpu":
        cpu_btn_clicked()
        current_window = cpu_page(window)
        
def cpu_btn_clicked():
    print("cpu button clicked")
    canvas.itemconfig(page_navigator, text="cpu")
    sidebar_navigator.place(x=0, y=133)

window = Tk()
window.title("Mink")
window.geometry("1280x720")
window.configure(bg = "#010101")

canvas = Canvas(
    window,
    bg = "#010101",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    152.0,
    360.0,
    image=image_image_1
)

current_window = cpu_page(window)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)

button_1.place(
    x=65.0,
    y=641.0,
    width=175.0,
    height=51.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_button_press("cpu"),
    relief="flat"
)

button_2.place(
    x=37.0,
    y=362.0,
    width=225.0,
    height=40.0
)

canvas.create_rectangle(
    38.0,
    356.0,
    264.0000305175781,
    357.4787292480469,
    fill="#3C3C45",
    outline="")

canvas.create_rectangle(
    78.0,
    403.0,
    249.0,
    404.0,
    fill="#DFBAC7",
    outline="") ##Underline

canvas.create_rectangle(
    125.0,
    689.0,
    205.99981689453125,
    690.1702117919922,
    fill="#DFBAC7",
    outline="") ##Underline

canvas.create_rectangle(
    102.0,
    300.0,
    157.9998779296875,
    301.1170196533203,
    fill="#DFBAC7",
    outline="")   ##Underline

canvas.create_rectangle(
    101.99526977539062,
    343.5104217529297,
    158.00430297851562,
    346.4389419555664,
    fill="#DFBAC7",
    outline="")  ##Underline

canvas.create_rectangle(
    102.00006103515625,
    251.87872314453125,
    160.00003051757812,
    253.12127685546875,
    fill="#DFBAC7",
    outline="") ##Underline

canvas.create_rectangle(
    101.995849609375,
    200.69244384765625,
    154.73220825195312,
    203.71759033203125,
    fill="#DFBAC7",
    outline="") ##Underline

canvas.create_rectangle(
    78.0,
    157.0,
    219.0,
    158.0,
    fill="#DFBAC7",
    outline="") ##Underline

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)

button_3.place(
    x=39.0,
    y=307.0,
    width=225.0,
    height=36.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=37.0,
    y=255.0,
    width=225.0,
    height=40.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=39.0,
    y=209.0,
    width=225.0,
    height=36.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=39.0,
    y=160.0,
    width=225.0,
    height=40.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=37.0,
    y=112.0,
    width=225.0,
    height=40.0
)

canvas.create_text(
    52.0,
    32.0,
    anchor="nw",
    text="MinkBench",
    fill="#DFBAC7",
    font=("Inter ExtraBold", 36 * -1)
)

canvas.create_rectangle(
    326.0,
    14.0,
    1263.0,
    707.0,
    fill="#010101",
    outline="")

# sidebar_navigator
sidebar_navigator = Frame(background="#FFFFFF")
sidebar_navigator.place(x=0, y=133, height=47, width=7)

# page_navigator
page_navigator = canvas.create_text(
    52.0, 80.0, anchor="nw", text="cpu", fill="#FFFFFF", font=("Inter Bold", 24 * -1)
)

window.resizable(False, False)
window.mainloop()
