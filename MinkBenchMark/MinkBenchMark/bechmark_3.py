import time
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from backend2.Benchmark_backend import Main_benchmark



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets//benchmark3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# window = Tk()

# window.geometry("937x693")
# window.configure(bg = "#010101")
# b_score, ml_score, ar_score, dt_score
global b_score, ml_score, ar_score, dt_score
b_score = ''
ml_score = ''
ar_score = ''
dt_score = ''



    

def benchmark_page(parent):
    
    canvas = Canvas(
        parent,
        bg = "#010101",
        height = 693,
        width = 937,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    def start_benchmark():
        print("Benchmarking button clicked")
        canvas.itemconfig(remark, text="Benchmarking \nin progress", fill="#DFBAC7")
        canvas.itemconfig(result, text="Benchmarking in Progress!\nPlease ,don't try to quit or close the program", fill="#FF6347")
        canvas.update()
    def done_benchmark():
        canvas.itemconfig(remark, text="Benchmarking \ncompleted", fill="#AAFF00")
        string_result = f"Benchmarking completed!\n\nBenchmark Score: {b_score}\nMachine Learning Score: {ml_score}\nAugmented Reality Score: {ar_score}\nData Transfer Score: {dt_score}"
        canvas.itemconfig(result, text=string_result, fill="#AAFF00")
        print(b_score, ml_score, ar_score, dt_score)
    def get_score():
        # start_benchmark()
        # b_score, ml_score, ar_score, dt_score = Main_benchmark()
        time.sleep(5)
        # done_benchmark()
        # fill green 
        
    # def update():
    #     canvas.after(1000, update)
    canvas.place(x = 300, y = 14)
    canvas.create_text(
        363.0,
        16.0,
        anchor="nw",
        text="Benchmark",
        fill="#DFBAC7",
        font=("MontserratRoman Bold", 24 * -1)
    )

    global image_image_1
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        494.0,
        261.0,
        image=image_image_1
    )

    canvas.create_text(
        335.0,
        216.0,
        anchor="nw",
        text="RUN Benchmark",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 20 * -1)
    )

    global image_image_2
    image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        494.0,
        116.0,
        image=image_image_2
    )

    remark=canvas.create_text(
        363.0,
        252.0,
        anchor="nw",
        text="start ",
        fill="#99999B",
        font=("MontserratRoman Medium", 16 * -1)
    )

    global button_image_1
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [f() for f in [start_benchmark, get_score, done_benchmark]],
        relief="flat"
    )
    button_1.place(
        x=846.0,
        y=231.0,
        width=101.0,
        height=102.0
    )

    global image_image_3
    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        468.0,
        508.0,
        image=image_image_3
    )
    result=canvas.create_text(
        100,
        400,
        anchor="nw",
        text="Results",
        fill="#99999B",
        font=("MontserratRoman Medium", 20 * -1)
    )
# window.resizable(False, False)
# window.mainloop()
