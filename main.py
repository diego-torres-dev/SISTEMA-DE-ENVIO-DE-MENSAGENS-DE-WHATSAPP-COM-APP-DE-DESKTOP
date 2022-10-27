# Importa todos os objetos do tkinter
from tkinter import *

# Importa o módulo os
import os

# Importa a bibliotaca time
import time

# Import o módulo python-dotenv
from dotenv import load_dotenv

# Importações do Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Importa o urllib para codificar textos enviados na URL
import urllib

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém o caminho do diretório que armazena o perfil do Google Chrome
caminho_perfil_google_chrome = os.getenv("DIR_PERFIL_GOOGLE_CHROME")

# Instala o Chrome Driver e fornece o caminho do executável
servico = Service(ChromeDriverManager().install())

# Opções do Google Chrome
options = webdriver.ChromeOptions()

# Especifica o diretório do perfil
# Caso não exista, cria um novo perfil do Google Chrome
options.add_argument(f"user-data-dir={caminho_perfil_google_chrome}")

# Adiciona um sinalizador para realizar a automação com navegador oculto
# options.add_argument('--headless')


def enviar_mensagem():
    # Obtém o número de telefone digitado no campo entry0
    telefone = entry0.get()

    # Obtém a mensagem digitada no campo entry1
    mensagem = entry1.get("1.0", END)

    # Codifica o texto para enviar na URL
    mensagem = urllib.parse.quote(mensagem)

    # Cria um navegador Google Chrome
    navegador = webdriver.Chrome(service=servico, options=options)

    # Abre a URL especificada (WhatsApp Web)
    # navegador.get("https://web.whatsapp.com/")

    # Link da conversa para a qual desejamos enviar a mensagem
    navegador.get(f"https://web.whatsapp.com/send?phone={telefone}&text={mensagem}")

    # Localiza o campo da mensagem pelo XPATH
    campo_mensagem = navegador.find_elements(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'
    )

    while len(campo_mensagem) < 1:
        # Aguarda 0.5s
        time.sleep(0.5)

        # Localiza o campo da mensagem pelo XPATH
        campo_mensagem = navegador.find_elements(
            By.XPATH,
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'
        )

    # Aguarda 1s
    time.sleep(1)


    # Envia a mensagem
    campo_mensagem[0].send_keys(Keys.ENTER)


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
    command=enviar_mensagem,
    relief="flat")

b0.place(
    x=475, y=343,
    width=100,
    height=33)

# Define que a janela não poderá ser redimensionada
window.resizable(False, False)

# Coloca a janela em loop
window.mainloop()
