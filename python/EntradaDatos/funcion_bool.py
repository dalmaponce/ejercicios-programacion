# Program: Funcion bool

# 1. Numero (int y float)
print(bool(0)) # False (El vacio numerico)
print(bool(0.0)) # False
print(bool(42))  # True


# 2. Texto (Strings)
# Cadena vacia = Nada = False
print(bool(""))  # False

# Cadena con espacio o texto = algo = True
print(bool(" "))  # True
print(bool("Hola")) # True

# 3. None (Ausencia total)
vacio = None
print(bool(vacio)) # False

print(bool(True)) # True
print(bool(False))  # False