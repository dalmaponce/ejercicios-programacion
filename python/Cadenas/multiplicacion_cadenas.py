# Programa: Multiplicacion de Cadenas
from warnings import simplefilter

# 1. Crear un separador visual
linea = "=" * 20
print(linea) # Salida: ====================

# 2. Identacion simple
nivel = 2
sangria = "    "* nivel
print(sangria + "definicion_bloque_codigo") # Salida:         definicion_bloque_codigo

# 3. Patrones simples
print("1"*5) # Salida: "11111" (texto no numero)

# 4. Error comun (comentado para evitar crash)
#print("Hola" * 2.5) # TypeError!
