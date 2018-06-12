import math # Modul math
import time # Modul time

from aufraeumen import *
from setup import * # GPIO Setup importieren und ausführen

try:
        while 1:
                bremsen()
                pr.start(50) # Motor A, speed Tastverhältnis
                pl.start(50) # Motor B, speed Tastverhältnis
				#hier gibt es evtl etwas umzustellen. 
except KeyboardInterrupt:
        bremsen()
        aufraeumen()