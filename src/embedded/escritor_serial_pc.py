import serial.tools.list_ports
import time

tempo_espera = 2
taxa_transmissao = 115200


def find_coms():

    ports_found = serial.tools.list_ports.comports()
    print("[COM ports found]")
    for item in ports_found:
        print(str(item))

    return ports_found

find_coms()

comunicacao_serial = serial.Serial("COM5", taxa_transmissao, timeout = tempo_espera)


while True:
    print("liga")
    comunicacao_serial.write(b"on\n") # Escreve "on" na serial
    time.sleep(2)

    print("desliga")
    comunicacao_serial.write(b"off\n")
    time.sleep(2)


