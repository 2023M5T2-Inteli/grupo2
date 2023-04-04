import serial.tools.list_ports
from time import sleep

timewait = 2
baudrate = 115200

# Lista todas as portas COM, uma delas é o Raspberry Pi Pico
def find_coms():

    ports_found = serial.tools.list_ports.comports()
    print("[COM ports found]")
    for item in ports_found:
        print(str(item))

    return ports_found

find_coms() # Executa a função

ser = serial.Serial("COM27", baudrate, timeout = timewait) # Abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico esta

while True:
    print("base")
    ser.write(b"on\n")
    sleep(2)
    line = ser.readline() # Realiza a leitura de um pacote de informaçãoes via serial
    print(line.decode("UTF-8")) # Exibe a string que foi enviada pelo Raspberry Pi Pico decodificada como texto

    print("medindo")
    ser.write(b"off\n")
    sleep(2)
    line = ser.readline() # Realiza a leitura de um pacote de informaçãoes via serial
    print(line.decode("UTF-8")) # Exibe a string que foi enviada pelo Raspberry Pi Pico decodificada como texto