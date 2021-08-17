# Autor: Cervantes Beltrán Karen
# License: MIT

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BCM)
# Set up pin no. 15 as output and default it to low
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)

#apaga y enciede irrigación 
def Irrigacion(num):
    if (num=="ON"):          
        GPIO.output(15, GPIO.HIGH) # led on
        print("ENCENDIDO")#mensaje encendido
    if (num=="OFF"):    
        GPIO.output(15, GPIO.LOW)# led off
        print("APAGADO")#mensaje apagado
	# Turn led off