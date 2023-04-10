import PySimpleGUI as sg
from serial.tools import list_ports
import serial
import sys

available_ports = list_ports.comports()
print(f'\n-- portas disponiveis: {[x.device for x in available_ports]}\n')


for i in available_ports:
    print("-- conectando na porta -> ", i.device)
    try:
        comm = serial.Serial(i.device, 115200, timeout=2)
        comm.write(b"start\n")
        line = comm.readline().decode('utf-8')
        if line:
            print("PORT=="+i.device+"==")
            exit(int(i.device.replace("COM","")))
        else:
            print("[X] sem resposta na porta \n")

    except Exception as e:
        print(e)
        print("[X] erro ao conectar na porta \n")
        continue

print("Nao foi possivel identificar o controlador Raspberry em nenhuma das portas disponiveis")

sg.theme("DarkRed1")
layout = [  [sg.Text("Não foi possivel identificar o Rasberry pi pico w!")],
            [sg.Text('certifique-se que ele está ligado e conectado ao computador. O progarma será encerrado.')],
            [sg.Button('OK')] ]

window = sg.Window('Oops!', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'OK':
        
        sys.exit(0)

