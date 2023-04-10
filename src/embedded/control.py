import serial.tools.list_ports
from time import sleep

timewait = 2
baudrate = 115200
com = "COM30"

# Lista todas as portas COM, uma delas é o Raspberry Pi Pico
def find_coms():

    ports_found = serial.tools.list_ports.comports()
    print("[COM ports found]")
    for item in ports_found:
        print(str(item))

    return ports_found

find_coms() # Executa a função

ser = serial.Serial(com, baudrate, timeout = timewait) # Abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico esta

while True:
    print("base")
    ser.write(b"on\n")
    line = ser.readline()
    while line.decode("UTF-8") != 'basereaded':
        line = ser.readline()
    print(line.decode("UTF-8"))

    sleep(1)

    print("medindo")
    ser.write(b"off\n")
    line = ser.readline()
    while line.decode().strip() == '':# or line.decode().strip() == 'basereaded':
        line = ser.readline()
    print(line.decode("UTF-8"))

    sleep(1)