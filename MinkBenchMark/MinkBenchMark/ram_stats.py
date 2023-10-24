


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame2")


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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    469.0,
    249.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    469.0,
    578.0,
    image=image_image_2
)

canvas.create_text(
    29.0,
    529.0,
    anchor="nw",
    text="Base Speed",
    fill="#99999B",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    731.0,
    524.0,
    anchor="nw",
    text="Logical\nProcessors",
    fill="#99999B",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    29.0,
    568.0,
    anchor="nw",
    text="Sockets",
    fill="#99999B",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    29.0,
    607.0,
    anchor="nw",
    text="Cores",
    fill="#99999B",
    font=("MontserratRoman Medium", 20 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    584.0,
    478.0,
    image=image_image_3
)

canvas.create_text(
    487.0,
    466.0,
    anchor="nw",
    text="CPU Voltage",
    fill="#DFBAC7",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    363.0,
    16.0,
    anchor="nw",
    text="RAM Statistics",
    fill="#DFBAC7",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    630.0,
    466.0,
    anchor="nw",
    text="25W",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    814.0,
    478.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    354.0,
    478.0,
    image=image_image_5
)

canvas.create_text(
    372.0,
    466.0,
    anchor="nw",
    text="3.5GHz",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    261.0,
    466.0,
    anchor="nw",
    text="Speed",
    fill="#DFBAC7",
    font=("MontserratRoman Medium", 20 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    124.0,
    478.0,
    image=image_image_6
)

canvas.create_text(
    169.0,
    466.0,
    anchor="nw",
    text="50°C",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    23.0,
    466.0,
    anchor="nw",
    text="Temperature",
    fill="#DFBAC7",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    724.0,
    466.0,
    anchor="nw",
    text="CPU Usage",
    fill="#DFBAC7",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    859.0,
    466.0,
    anchor="nw",
    text="50°C",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    161.0,
    529.0,
    anchor="nw",
    text="3.2GHz",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    192.0,
    568.0,
    anchor="nw",
    text="1",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    190.0,
    607.0,
    anchor="nw",
    text="8",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    274.0,
    529.0,
    anchor="nw",
    text="L1 Cache",
    fill="#99999B",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    274.0,
    568.0,
    anchor="nw",
    text="L2 Cache",
    fill="#99999B",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    274.0,
    607.0,
    anchor="nw",
    text="L3 Cache",
    fill="#99999B",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    400.0,
    529.0,
    anchor="nw",
    text="512KB",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    397.0,
    568.0,
    anchor="nw",
    text="4.0MB",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    394.0,
    607.0,
    anchor="nw",
    text="16.0MB",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    491.0,
    529.0,
    anchor="nw",
    text="Processes",
    fill="#99999B",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    501.0,
    568.0,
    anchor="nw",
    text="Threads",
    fill="#99999B",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    499.0,
    607.0,
    anchor="nw",
    text="Handles ",
    fill="#99999B",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    635.0,
    529.0,
    anchor="nw",
    text="369",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    627.0,
    568.0,
    anchor="nw",
    text="6040",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    619.0,
    607.0,
    anchor="nw",
    text="158479",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)

canvas.create_text(
    888.0,
    536.0,
    anchor="nw",
    text="16",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
