
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
from Professores import Professores
from BancoDeDados import BancoDeDados
from usuario import Usuario, Admnistrador
from Materia import Materia
from Periodo import Periodo
import os
from pathlib import Path
import tkinter as tk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

BancoDeDados.criar_materias()
BancoDeDados.criar_professores_instancia()
BancoDeDados.criar_periodos()
BancoDeDados.listas_periodos()

#OUTPUT_PATH = Path(__file__).parent
#ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\vcost\OneDrive\Área de Trabalho\dev\Tkinter-Designer-master\build\assets\frame0")
script_directory = Path(os.path.dirname(os.path.abspath(__file__)))
ASSETS_PATH = script_directory / "build" / "assets" / "FrameGeral"

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

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1_f1.png"))
entry_bg_1 = canvas.create_image(
    400.0,
    382.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    font= ('arial, 12'),
    highlightthickness=0
)
entry_1.place(
    x=283.0,
    y=253.0,
    width=228.0,
    height=35
)

canvas.create_text(
    284.0,
    372.0,
    anchor="nw",
    text="****************",
    fill="#B2B2B2",
    font=("MontserratRoman Regular", 18 * -1)
)

canvas.create_text(
    283.0,
    332.0,
    anchor="nw",
    text="Senha",
    fill="#000000",
    font=("MontserratRoman Regular", 12 )
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2_f1.png"))
entry_bg_2 = canvas.create_image(
    400.0,
    270.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    font=('arial 12'),
    show='*',
    highlightthickness=0
)
entry_2.place(
    x=283.0,
    y=365.0,
    width=228.0,
    height=35.0
)

def logar(nome,senha):
    login = Usuario.entrar_conta(nome,senha)
    if login == True:
        pass
    else:
        tk.messagebox.showerror('Login Error','Login inválido')
    
def frame2():
    import Frame2

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1_f1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: frame2(),
    relief="flat"
)
button_1.place(
    x=415.0,
    y=447.0,
    width=129.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2_f1.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: logar(entry_1.get(),entry_2.get()),
    relief="flat"
)
button_2.place(
    x=249.0,
    y=447.0,
    width=129.0,
    height=60.0
)

canvas.create_text(
    283.0,
    260.0,
    anchor="nw",
    text="omanodaspadoca",
    fill="#B2B2B2",
    font=("MontserratRoman Regular", 14 * -1)
)

canvas.create_text(
    283.0,
    220.0,
    anchor="nw",
    text="Usuario",
    fill="#000000",
    font=("MontserratRoman Regular", 12 )
)

canvas.create_text(
    313.0,
    130.0,
    anchor="nw",
    text="LOGIN",
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



window.resizable(False, False)
window.mainloop()
