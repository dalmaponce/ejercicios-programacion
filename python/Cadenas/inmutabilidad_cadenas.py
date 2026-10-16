# Ejemplo: cadenas inmutables

animal = "Gato"

# animal[4] = "S" # proboca un error
# CORRECTO: concatenar (Sumar)
# Tomamos "Gato" + "s" y lo guardamos en una nueva variable
plural = animal + "s"

print(animal) # salida: "Gato" (intacto)
print(plural) # Salida: "Gatos" (Nuevo objeto)

plural = f"{animal}s"
print(plural)