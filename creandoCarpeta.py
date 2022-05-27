"""1ra forma"""
# import os 

# os.mkdir("example_directory/")
"""2da forma"""
from pathlib import Path 
# Creamos un objeto "obj" de la clase Path y le pasamos como argumento la ruta
obj= Path("example2_directory/")
# Accedemos a su método mkdir()
try:
    obj.mkdir()
except FileExistsError as e:
    # Nos mostrará un error más entendible
    print(e)
# ########################

"""Si la ruta ya existe nos generará un Error -> FileExistsError"""
# Lo controlamos con un Try Except


