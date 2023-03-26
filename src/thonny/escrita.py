import serial.tools.list_ports
import time

tempo_espera = 2
taxa_transmissao = 115200

def find_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'Arduino' in p.description:
            return p.device
    return None

porta = find_port()

comunicacao_serial = serial.Serial("COM8", taxa_transmissao, timeout=tempo_espera)

while True:
    print("liga")
    comunicacao_serial.write(b'on\n')
    time.sleep(10)

    print("desliga")
    comunicacao_serial.write(b'off\n')
    time.sleep(10)