from serial.tools import list_ports

import pydobot
import PySimpleGUI as sg

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = "COM7"

device = pydobot.Dobot(port=port, verbose=True)

layout = [
    [sg.Button('Iniciar Ensaio')],
    [sg.Text("Voltar para a posição inicial")],
    [sg.Button("First Position")],
    [sg.Text("Salvar nova posição")],
    [sg.Button("get pos")],
    [sg.Text("Iniciar o ensaio com nova posição")],
    [sg.Button("RUN ARRAY")],
    [sg.Button("Clear array")],
]


(fx, fy, fz, fr, j1, j2, j3, j4) = device.pose()

print(fx, fy, fz, fr, j1, j2, j3, j4)

arrayPos = []
presetArray = []
# Create the win[dow
window = sg.Window('Movimentação do robô', layout)
# Display and interact with the Window using an Event Loop, only for button ok2
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WIN_CLOSED:
        break
    if event == "Iniciar Ensaio":
        for i in presetArray:
            device.move_to(i[0], i[1], i[2], 0, wait=True)

    if event == "get pos":
        (x, y, z, fr, j1, j2, j3, j4) = device.pose()
        arrayPos.append([x, y, z])
    if event == "RUN ARRAY":
        for i in arrayPos:
            device.move_to(i[0], i[1], i[2], 0, wait=True)
    if event == 'Clear array':
        arrayPos = []
    if event == 'RUN':
        (x, y, z, r, j1, j2, j3, j4) = device.pose()
        print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

        device.move_to(
            x + int(values[0]), y + int(values[1]), z + int(values[2]), r, wait=False)

        print(values)

        sg.Popup('finalizado')

    elif event == 'First Position':
        device.move_to(225.7625732421875, 0.0,
                       150.50729370117188, 0.0, wait=True)

device.close()
# Finish up by removing from the screen
window.close()
