#Programa: Registro de explorador espacial
from tipos_datos import misiones_completadas, nivel_energia

# Asignar valores a las variables
nombre_explorador = "Luna Vega"
planeta_origen = 'Marte'
edad_explorador = 29
misiones_completadas = 4
nivel_energia = 87.5


#for = 16 esto arroja error (no debemos usar keywords o palabras reservadas)
Nivel_Energia = 90.5 # no es una buena preactica
NIVEL_ENERGIA = 100.00 #Se considera que es una constante
nivel_energía = 80.0 # no se deben usar carcteres especiales (acentos, ñ)


# Imprimir los valores
print("== Registro Espacial ==")
print("nombre del explorador: ", nombre_explorador)
print("Planeta origen: ",planeta_origen)
print("edad del explorador: ", edad_explorador)
print("misiones del explorador: ", misiones_completadas)
print("nivel de energia del explorador: ", nivel_energia)
