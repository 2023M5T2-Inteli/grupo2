import machine
import sys
from hx711 import HX711
from time import sleep

# inicializando o modulo HX711 (DT, SCK)
hx = HX711(2, 3)
# valor base de medida
base = 142000
    
#Função para ler e retornar os valores da célula de carga
def readCell(load_cell):
    val = load_cell.read()
    print("Load cell value: ", val)
    return val

def convert(vl, bs):
    wt = (vl - bs)/1655
    print("Weight: ", wt)
    return wt
    
# Lendo o valor da célula de carga e printando
while True:
    base = readCell(hx)
    sys.stdout.write("Medindo...\n")
    sleep(5)
    value = readCell(hx)
    weight = convert(value, base)
    sys.stdout.write(str(weight))
    print("\n")
    sleep(2)
    
    