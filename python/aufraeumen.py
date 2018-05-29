import RPi.GPIO as GPIO # GPIO-Bibliothek importieren
import time             # Modul time
from setup import *

def aufraeumen():
    # Erst bremsen dann cleanup
    GPIO.output(IN1, 0)  # Bremsen
    GPIO.output(IN2, 0)  # Bremsen
    GPIO.output(IN3, 0)  # Bremsen
    GPIO.output(IN4, 0)  # Bremsen
    time.sleep(.1)
    GPIO.cleanup()       # Aufräumen
    print("GPIOs aufgeräumt")
    
def bremsen():
    GPIO.output(IN1, 0)  # Bremsen
    GPIO.output(IN2, 0)  # Bremsen
    GPIO.output(IN3, 0)  # Bremsen
    GPIO.output(IN4, 0)  # Bremsen
    
def losfahren():
    GPIO.output(IN1, 1)      # Motor A Rechtslauf			
    GPIO.output(IN2, 0)      # Motor A Rechtslauf
    GPIO.output(IN3, 1)      # Motor B Rechtslauf
    GPIO.output(IN4, 0)      # Motor B Rechtslauf

def links():
 
    GPIO.output(IN1, 1)  # Bremsen
    GPIO.output(IN2, 0)  # Bremsen
    GPIO.output(IN3, 0)  # Bremsen
    GPIO.output(IN4, 1)  # Bremsen

    
def rechts():
    GPIO.output(IN1, 0)  # Bremsen
    GPIO.output(IN2, 1)  # Bremsen
    GPIO.output(IN3, 1)  # Bremsen
    GPIO.output(IN4, 0)  # Bremsen
    
def back():		#evtl funktioniert rückwärts fahren nicht
    GPIO.output(IN1, 0)      # Motor A Rechtslauf
    GPIO.output(IN2, 1)      # Motor A Rechtslauf
    GPIO.output(IN3, 0)      # Motor B Rechtslauf
    GPIO.output(IN4, 1)      # Motor B Rechtslauf
