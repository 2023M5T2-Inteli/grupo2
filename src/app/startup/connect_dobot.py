import PySimpleGUI as sg
from serial.tools import list_ports
import pydobot
import sys

# Utilizamos o pysimpleGUI para criar interfaces gráficas que auxiliam o 
# usuário na configuração do programa.
sg.theme("SystemDefaultForReal")
# Popup que pede para o usuário conecte o dobot e o rasp
# O código só continua rodando quando o usuário fecha a janela
sg.popup("Bem-vindo!", "Certifique-se que o Dobot e o módulo controlador estão ligados e conectados ao computador. Desligue o Bluetooth do seu computador. Ao clicar em OK, iniciaremos o processo de conexão...")

# lista as portas disponiveis
available_ports = list_ports.comports()
print(f'\n-- portas disponiveis: {[x.device for x in available_ports]}\n')

# Faz um loop por todas as portas disponiveis para tentarmos nos conectar ao dobot
for i in available_ports:
    print("-- conectando na porta -> ", i.device)
    try:
        # Para cada uma das portas disponiveis, tenta se conectar pedindo que o dobot envie sua posição atual 
        dobot = pydobot.Dobot(port=i.device, verbose=False)
        pose = dobot.pose()
        print(pose)
        # Se o dobot responder uma posição válida, fecharemos o processo e retornaremos a porta do Dobot
        if type(pose) == tuple and pose[0]:
            print("PORT=="+i.device+"==")
            exit(int(i.device.replace("COM","")))
        # continua o loop caso o dobot não responda
        else:
            print("[X] sem resposta na porta \n")

    # Continua o loop caso haja um erro ao se conectar em alguma porta 
    except:
        print("[X] erro ao conectar na porta \n")
        continue

# Caso o loop termine sem a identificação do Dobot, executa código abaixo

print("Nao foi possivel identificar o robo em nenhuma das portas disponiveis")

# Abre uma janela de erro avisando que o Dobot não está conectado.
sg.theme("DarkRed1")
layout = [  [sg.Text("Não foi possivel identificar o Dobot!")],
            [sg.Text('certifique-se que ele está ligado e conectado ao computador.')],
            [sg.Button('Continuar mesmo assim'), sg.Button('OK')] ]

window = sg.Window('Oops!', layout)

# Enquanto a janela estiver aberta:
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'OK':
        # Finaliza o processo com o código 0.
        sys.exit(0)
    
    # Caso o usuário opte por continuar mesmo assim, com o robo desconectado,
    # retorna a porta default, 1
    elif event == 'Continuar mesmo assim':
        sys.exit(1)

