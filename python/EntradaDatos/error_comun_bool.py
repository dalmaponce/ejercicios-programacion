# Error Comun de Principiante
respuesta_usuario = "False" # esto es texto

# La funcion bool evalua si el string esta vacio
es_verdad = bool(respuesta_usuario)

print(f"El valor es: {es_verdad}")
# Output: El valor es: True
# ¿Porque? Porque el string "False" tiene 5 letras. No esta vacio.

# Forma correcta de validar vacio:
texto_vacio = ""
print(bool(texto_vacio)) # False