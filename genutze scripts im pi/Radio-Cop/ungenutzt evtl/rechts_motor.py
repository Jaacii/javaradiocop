import math # Modul math
import time # Modul time

from fahrscript import *
from setup import * # GPIO Setup importieren und ausführen

try:
        while 1:
                rechts()
                pr.start(50) # Motor A, speed Tastverhältnis
                pl.start(50) # Motor B, speed Tastverhältnis

except KeyboardInterrupt:
        bremsen()
        aufraeumen()