# Autor: Moreno Morado Jesús Daniel 
# License: MIT
# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
import time
from time import sleep
# Set up pin no. 24 as output and default it to low
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
#lee velocidad de ventilador y lo muestra en pantalla
def Ventilador (vel):
    print("La Potencia Ventilador",vel)
    M_In1 = 17
    M_In2 = 27
    M_Enable = 22

    GPIO.setup(M_In1,GPIO.OUT)
    GPIO.setup(M_In2,GPIO.OUT)
    GPIO.setup(M_Enable,GPIO.OUT)

    # Creamos la instancia PWM con el GPIO a utilizar y la frecuencia de la señal PWM
    p = GPIO.PWM(M_Enable, 50)
    #Inicializamos el objeto PWM
    p.start(0)

    print("Hacemos girar el motor en un sentido por 10 segundos mientras aumentamos  y disminuimos la velocidad")
    # Establecemos el sentido de giro con los pines 17 y 27  
    GPIO.output(M_In1,GPIO.HIGH)
    GPIO.output(M_In2,GPIO.LOW)
    pass

def OperaVent(vel):
    #Aumenta velocidad
    for m in range(0, vel, 1):
        p.ChangeDutyCycle(m)
        time.sleep(0.05)
    GPIO.cleanup()
    pass

def OperaOFFVent(vel):
    #Disminuye velocidad
    for m in range(vel, -1, -1):
        p.ChangeDutyCycle(m)
        time.sleep(0.05)

    print ("Detenemos el motor")
    p.ChangeDutyCycle(0)
    sleep(1)

    GPIO.cleanup()
    pass

def VentiladorONOFF(op):
    if (op=="ON"):
        GPIO.output(24, GPIO.HIGH)# led on
        print("Ventilador ENCENDIDO")#mensaje encendido
    if(op=="OFF"):
        GPIO.output(24, GPIO.LOW) # led off
        print("Ventilador APAGADO")#mensaje apagado
        pass
