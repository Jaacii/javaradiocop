import math # Modul math
import time # Modul time

from aufraeumen import *
from setup import * # GPIO Setup importieren und ausführen

try:
	while 1:
		losfahren()
		pr.start(100) # Motor A, speed Tastverhältnis
		pl.start(100) # Motor B, speed Tastverhältnis

except KeyboardInterrupt:
	bremsen()
	aufraeumen()

