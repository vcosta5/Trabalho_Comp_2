
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


#OUTPUT_PATH = Path(__file__).parent
#ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\vcost\OneDrive\Área de Trabalho\Tkinter-Designer-master\build\assets\frame0")
script_directory = Path(os.path.dirname(os.path.abspath(__file__)))
ASSETS_PATH = script_directory / "build" / "assets" / "frame6"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
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
    x=413.0,
    y=490.0,
    width=155.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=226.0,
    y=490.0,
    width=155.0,
    height=60.0
)

canvas.create_text(
    462.0,
    438.0,
    anchor="nw",
    text="{ano}",
    fill="#000000",
    font=("MontserratRoman Regular", 24 * -1)
)

canvas.create_text(
    227.0,
    438.0,
    anchor="nw",
    text="Matéria ministrada",
    fill="#000000",
    font=("MontserratRoman Regular", 24 * -1)
)

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
    x=412.0,
    y=357.0,
    width=155.0,
    height=60.0
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
    x=226.0,
    y=357.0,
    width=155.0,
    height=60.0
)

canvas.create_text(
    462.0,
    306.0,
    anchor="nw",
    text="{ano}",
    fill="#000000",
    font=("MontserratRoman Regular", 24 * -1)
)

canvas.create_text(
    227.0,
    306.0,
    anchor="nw",
    text="Matéria ministrada",
    fill="#000000",
    font=("MontserratRoman Regular", 24 * -1)
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
    x=413.0,
    y=223.0,
    width=155.0,
    height=60.0
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
    x=226.0,
    y=223.0,
    width=155.0,
    height=60.0
)

canvas.create_text(
    462.0,
    180.0,
    anchor="nw",
    text="{ano}",
    fill="#000000",
    font=("MontserratRoman Regular", 24 * -1)
)

canvas.create_text(
    227.0,
    180.0,
    anchor="nw",
    text="Matéria ministrada",
    fill="#000000",
    font=("MontserratRoman Regular", 24 * -1)
)

canvas.create_text(
    235.0,
    91.0,
    anchor="nw",
    text="{PROFESSOR}",
    fill="#000000",
    font=("MontserratRoman Regular", 48 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    60.0,
    fill="#FFBA53",
    outline="")

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
    x=0.0,
    y=0.0,
    width=58.0,
    height=60.0
)
window.resizable(False, False)
window.mainloop()
