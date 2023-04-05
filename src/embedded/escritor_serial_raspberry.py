import sys
from time import sleep

while True:
    
    sys.stdout.write("Ha\n") # Escreve na serial
    sleep(2) #Espera 2 segundos para escrever algo diferente
    
    sys.stdout.write("YEAH YEAH\n")
    sleep(2)