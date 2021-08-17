# Autor: Moreno Morado Jesús Daniel 
# License: MIT
# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
import sys
import time
#Biblioteca Adafruit_DHT by https://github.com/adafruit/Adafruit_Python_DHT.git
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)
# Set up pin no. 18 as output and default it to low
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

#Instancia de la biblioteca Adafruit_DHT
sensor = Adafruit_DHT.DHT11
#Definimos pin de datos
pin = 24

def OperaTemp(band):
    # Si la bandera está activa lee sensor
    if (band == 1):
        # Intenta ejecutar las siguientes instrucciones, si falla va a la instruccion except
        try:
    		# Obtiene la humedad y la temperatura desde el sensor
            humedad, temperatura = Adafruit_DHT.read_retry(sensor,pin)

    		# Imprime en la consola las variables temperatura y humedad con un decimal
            print('Temperatura={0:0.1f} C  Humedad={1:0.1f}%'.format(temperatura, humedad))

        # Se ejecuta en caso de que falle alguna instruccion dentro del try
        except RuntimeError as error:
            # Imprime en pantalla el error
            print(error.args[0])

#Lee temperatura y muestra en pantalla
def Temperatura (vel):
    print("La Potencia Temperatura",vel)
    
    pass
def ONOFFTEMP (op):
    if (op=="ON"):
        GPIO.output(18, GPIO.HIGH)# led on
        print("Temperatura ENCENDIDO")#mensaje encendido
        band = 1 #Bandera activa sensor
        OperaTemp(band) #Activa Sensor
    if(op=="OFF"):
        GPIO.output(18, GPIO.LOW)# led off
        print("Temperatura APAGADO")#mensaje apagado
        band = 0 #Bandera no activa sensor
        OperaRadiador(band) #No activa sensor
    pass





