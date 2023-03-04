from serial.tools import list_ports

import pydobot
import PySimpleGUI as sg

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')    
port = "COM22"

device = pydobot.Dobot(port=port, verbose=True)

layout = [  [sg.Text("X")],
            [sg.Input()],
            [sg.Text("Y")],
            [sg.Input()],
            [sg.Text("Z")],
            [sg.Input()],
            [sg.Button('RUN')],
            [sg.Button("First Position")],
            [sg.Button("RUN ARRAY")],
            [sg.Button("get pos")]]
        

(fx, fy, fz, fr, j1, j2, j3, j4) = device.pose()
        
print(fx, fy, fz, fr, j1, j2, j3, j4)

arrayPos = []
# Create the win[dow
window = sg.Window(']Projeto, sim ou com certeza?', layout)
# Display and interact with the Window using an Event Loop, only for button ok2
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WIN_CLOSED:
        break
    if event == "get pos":
        (x,y,z,fr, j1, j2, j3, j4) = device.pose()
        arrayPos.append([x,y,z])
    if event == "RUN ARRAY":
        for i in arrayPos:
            device.move_to(i[0], i[1], i[2], 0, wait=True)
    if event == 'RUN':
        (x, y, z, r, j1, j2, j3, j4) = device.pose()
        print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')


        device.move_to(x + int(values[0]), y + int(values[1]), z + int(values[2]) , r, wait=False)
    
        print(values)

        sg.Popup('finalizado')

    elif event == 'First Position':
        device.move_to(fx, fy, fz, fr)
                
device.close()
# Finish up by removing from the screen
window.close()
