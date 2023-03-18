# Importação das bibliotecas usadas
import machine
import time

# Definindo os pinos para a Ponte H
pino1 = machine.Pin(0, machine.Pin.OUT)  # Pino 1 da Ponte H
pino2 = machine.Pin(2, machine.Pin.OUT)  # Pino 3 da Ponte H
pino3 = machine.Pin(7, machine.Pin.OUT)  # Pino 9 da Ponte H
pino4 = machine.Pin(9, machine.Pin.OUT)  # Pino 10 da Ponte H

# Função para ligar os imãs
def ativaIma():
    pino1.value(1)
    pino2.value(0)
    
    pino3.value(1)
    pino4.value(0)
    
    print("Ligado")

# Função para inverter o campo magnético dos imãs
def inverteIma():
    pino1.value(0)
    pino2.value(1)
    
    pino3.value(0)
    pino4.value(1)
    
    print("Invertido")

# Função para desligar os imãs
def desligaIma():
    pino1.value(0)
    pino2.value(0)
    
    pino3.value(0)
    pino4.value(0)
    
    print("Desligado")

# Ciclo de funcionamento dos imãs
while True:
    print("CICLO")
    
    ativaIma()
    
    time.sleep(54) # Tempo do imã ligado 
    
    inverteIma()
    
    time.sleep(1) # Tempo da inversão do campo do imã
    
    desligaIma()
    
    time.sleep(11) # Tempo do imã desligado
    
    
    
    ativaIma()
    #ima ativado

    time.sleep(20)

    inverteIma()
    #ima invertido

    time.sleep(5)
    
    desligaIma()
    #ima desligado
    
    time.sleep(2)
    
    