import serial.tools.list_ports
from time import sleep

tempo_espera = 2
taxa_transmissao = 115200
com = "COM30"

# Lista todas as portas COM, uma delas é o Raspberry Pi Pico
def find_coms():

    ports_found = serial.tools.list_ports.comports()
    print("[COM ports found]")
    for item in ports_found:
        print(str(item))

    return ports_found

find_coms() # Executa a função

comunicacao_serial = serial.Serial(com, taxa_transmissao, timeout = tempo_espera) # Abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico esta

while True:

    line = comunicacao_serial.readline() # Realiza a leitura de um pacote de informaçãoes via serial
    
    print(line.decode("UTF-8")) # Exibe a string que foi enviada pelo Raspberry Pi Pico decodificada como texto


