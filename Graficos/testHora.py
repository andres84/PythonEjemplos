import locale
from datetime import *

dt = datetime.now()
print(dt.isoformat())

# Idioma "es-ES" (codigo para el espaniol de Espania)
locale.setlocale(locale.LC_ALL, 'es-ES') 

print(dt.strftime("%A %d %B %Y %I:%M"))
print(dt.strftime("%A %d de %B del %Y - %H:%M"))  # %I 12h - %H 24h
