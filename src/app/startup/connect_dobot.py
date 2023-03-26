import PySimpleGUI as sg
from serial.tools import list_ports
import pydobot
import sys

sg.theme("SystemDefaultForReal")
sg.popup("Bem-vindo!", "Certifique-se que o Dobot e o módulo controlador estão ligados e conectados ao computador. Ao clicar em OK, iniciaremos o processo de conexão...")

available_ports = list_ports.comports()
print(f'\n-- portas disponiveis: {[x.device for x in available_ports]}\n')


for i in available_ports:
    print("-- conectando na porta -> ", i.device)
    try:
        dobot = pydobot.Dobot(port=i.device, verbose=False)
        pose = dobot.get_pose()
        if type(pose) == list and pose[0]:
            print("PORT=="+i.device+"==")
            exit(i.device)
        else:
            print("[X] sem resposta na porta \n")

    except:
        print("[X] erro ao conectar na porta \n")
        continue

print("Nao foi possivel identificar o robo em nenhuma das portas disponiveis")

sg.theme("DarkRed1")
layout = [  [sg.Text("Não foi possivel identificar o Dobot!")],
            [sg.Text('certifique-se que ele está ligado e conectado ao computador.')],
            [sg.Button('Continuar mesmo assim'), sg.Button('OK')] ]

window = sg.Window('Oops!', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'OK':
        sys.exit(0)
    elif event == 'Continuar mesmo assim':
        sys.exit(1)

