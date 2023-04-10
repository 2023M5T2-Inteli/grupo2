import sys
import machine
from time import sleep

led = machine.Pin("LED", machine.Pin.OUT) # Cria o objeto de controle para o objeto da placa

def led_on():
    led(1)

def led_off():
    led(0)
    
# Testa para ver se o código está sendo executado, piscando o LED da placa
led_on()
sleep(2)
led_off()
sleep(2)

while True:
    # Realiza uma leitura de informação da serial
    v = sys.stdin.readline().strip()

    # Se a string lida for "on", ele liga o LED da placa, se for "off", desliga
    if v.lower() == "on":
        led_on()
    elif v.lower() == "off":
        led_off()