
# Si queremos leer un archivo
with open('data.txt', 'r') as f:
    data = f.read()
    print(data)

print("===========")
# Si queremos escribir en un archivo (SOBRESCRIBIR)
with open('data.txt', 'w') as f:
    data="Holaaa a todos!, soy Jhomar"
    f.write(data)
    print(data)

import os 

entries = os.listdir('my_directory/')
print(entries)
for i in entries:
    print(i)

print("="*10)

# Imprime la direccion en memoria de todas las entradas del directorio actual.
entries2=os.scandir('my_directory/')
print(entries2)

with os.scandir('my_directory/') as entries:
    for i in entries:
        print(i.name)

# Otra forma de obtener una lista de directorios es usando el "Pathlib" módulo.
from pathlib import Path
print("="*20)
entries3=Path("my_directory")
for i in entries3.iterdir():
    print(i.name)

"""
Hay diversas formas de obtener la lista directorios de una ruta, podemos usar:
entries2=os.scandir('my_directory/')
os --> listdir, scandir
pathlib -> Path
"""
