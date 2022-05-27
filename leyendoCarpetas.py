from pathlib import Path 

# Creamos un objeto de la clase Path
basePathObj = Path('my_directory/')
for i in basePathObj.iterdir():
    if i.is_dir():
        print(i.name)
