from pathlib import Path 

obj = Path("paquete/modulo/camote")
obj.mkdir(parents=True)

# Es recomendable hacerlo con pathlib ya que es lo mismo para crear un único directorio que para crear varios.(anidados)