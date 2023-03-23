# Importação das bibliotecas usadas
import machine
import time

# Definindo os pinos para a Ponte H
bomb1 = machine.Pin(0, machine.Pin.OUT)  # Pino 1 da Ponte H
bomb2 = machine.Pin(2, machine.Pin.OUT)  # Pino 3 da Ponte H
ima1 = machine.Pin(7, machine.Pin.OUT)  # Pino 9 da Ponte H
ima2 = machine.Pin(9, machine.Pin.OUT)  # Pino 10 da Ponte H

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

# Ciclo de funcionamento dos imãs
while True:
    print("CICLO")
    
    ativaIma()
    
    time.sleep(27) # Tempo do imã ligado
    
    ativaBomb()
    
    time.sleep(27) # Tempo do imã ligado
    
    desativaBomb()
    
    inverteIma()
    
    time.sleep(1) # Tempo da inversão do campo do imã
    
    desativaIma()
    
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
    
    