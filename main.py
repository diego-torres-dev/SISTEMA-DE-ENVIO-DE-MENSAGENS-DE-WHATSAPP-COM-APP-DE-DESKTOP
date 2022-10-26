# Importa todos os objetos do tkinter
from tkinter import *


def btn_clicked():
    print("Button Clicked")


# Cria uma janela do tkinter
window = Tk()

# Define as dimensões da janela
window.geometry("700x400")

# Define a cor do plano de fundo da janela
window.configure(bg="#ffffff")

# Cria um quadro com as especificações dadas
canvas = Canvas(
    window,
    bg="#ffffff",
    height=400,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge")

# Posiciona o quadro na janela
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    355.0, 200.0,
    image=background_img)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    525.0, 164.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry0.place(
    x=402.0, y=147,
    width=246.0,
    height=33)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    525.0, 275.0,
    image=entry1_img)

entry1 = Text(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry1.place(
    x=402.0, y=230,
    width=246.0,
    height=88)

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=475, y=343,
    width=100,
    height=33)

# Define que a janela não poderá ser redimensionada
window.resizable(False, False)

# Coloca a janela em loop
window.mainloop()
