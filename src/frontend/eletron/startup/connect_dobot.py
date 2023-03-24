import PySimpleGUI as sg
from serial.tools import list_ports


# sg.popup("Bem-vindo! Certifique-se que o Dobot está ligado e conectado ao computador. Ao clicar em OK, iniciaremos o processo de conexão...")
available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
# print(f'available ports: {[x.device for x in available_ports]}')
''' 

AQUI FICA O SCRIPT QUE ESCOLHE A PORTA ONDE O ROBO VAI RODAR
A PORTA TEM QUE SER DEVOLVIDA NA FUNCAO ABAIXO
SE A PORTA CERTA É A COM8, A VARIAVEL port DEVE SER 8


''' 

port = 1
print("PORT=="+str(port)+"==")