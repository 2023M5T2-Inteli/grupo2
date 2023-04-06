# Importação das bibliotecas usadas
import machine
import time
import sys

# Definindo os pinos para a Ponte H
bomb1 = machine.Pin(0, machine.Pin.OUT)  # Pino 1 da Ponte H
bomb2 = machine.Pin(2, machine.Pin.OUT)  # Pino 3 da Ponte H
ima1 = machine.Pin(7, machine.Pin.OUT)  # Pino 9 da Ponte H
ima2 = machine.Pin(9, machine.Pin.OUT)  # Pino 10 da Ponte H
start = False

# Função para ligar os imãs
def ativaIma():
    ima1.value(1)
    ima2.value(0)
    
    print("Ligado")
    
def ativaBomb():
    bomb1.value(1)
    bomb2.value(0)
    
def desativaBomb():
    bomb1.value(0)
    bomb2.value(0)

# Função para inverter o campo magnético dos imãs
def inverteIma():
    ima1.value(0)
    ima2.value(1)
    
    print("Invertido")

# Função para desligar os imãs
def desativaIma():
    ima1.value(0)
    ima2.value(0)
    
    print("Desligado")
    
print("oii")

# Ciclo de funcionamento dos imãs
while start:
    v = sys.stdin.readline().strip()

    # Se a string lida for "on", ele liga o LED da placa, se for "off", desliga
    if v.lower() == "on":
        ativaIma()
        
    elif v.lower() == "off":
        desativaIma()
        
    
    if v.lower() == "bomba":
        ativaBomb()
    elif v.lower() == "desbomba":
        desativaBomb()
    
while not start:
    v = sys.stdin.readline().strip()
    if v.lower() == "start":
        start = True
        print("start")
    else:
        print("não start")
  
    
      
