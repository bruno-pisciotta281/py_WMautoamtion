# 1. Importar bibliotecas necessárias
import pywhatkit
import keyboard
import time

from datetime import datetime

# 2. Definir para quais contatos iremos enviar as msgs
contatos = ["number"]

# 3. Definir intervalo de envio
intervalo = 60

# 4. Enviar mensagens
while len(contatos) >= 1:

    # Enviar mensagem
    pywhatkit.sendwhatmsg(contatos[0], "teste 01!", datetime.now().hour, datetime.now().minute + 2)

    # Remover contato da lista
    del contatos[0]

    # Aguardar intervalo
    time.sleep(intervalo)

    # Pressionar tecla
    keyboard.press_and_release("ctrl + w")
