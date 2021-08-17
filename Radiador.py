# Autor: Moreno Morado Jesús Daniel 
# License: MIT
# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
import time
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BCM)
# Set up pin no. 23 as output and default it to low
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)

def OperaRadiador(vel,band):
    GPIO.setwarnings(False)
    # Indicamos que el pin23 es de salida de corriente
    GPIO.setup(23,GPIO.OUT)
    # Guardamos el valor de PWM para pin23
    pwm_led=GPIO.PWM(23,500)
    # Iniciamos el led con longitud de pulso 0
    pwm_led.start(0)
    # Si la bandera esta activa modifica la potencia
    if (band == 1):
        # Modificamos longitud de pulso
        pwm_led.ChangeDutyCycle(vel)

#Lee potencia de radidador y muestra en pantalla
def PotenciaRad(vel):
    print("La Potencia Radiador",vel)
    
def ONOFFRAD(op):
    if (op=="ON"):
        GPIO.output(23, GPIO.HIGH)# led on
        print("Radiador ENCENDIDO")#mensaje encendido
        band = 1 #Bandera activa modificación de pulso
        OperaRadiador(vel,band) #Activa Radiador
    if(op=="OFF"):
        GPIO.output(23, GPIO.LOW)# led off
        print("Radiador APAGADO")#mensaje apagado
        band = 0 #Bandera no hay modificación de pulso
        OperaRadiador(vel,band) #No activa Radiador
        pass
