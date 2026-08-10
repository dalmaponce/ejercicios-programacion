numeros = [45, 32, 18, 27, 9, 14, 60, 11, 10, 12]  # valores simulados sin usar input()

cantidad = len(numeros)

# Validamos que haya al menos 10 números
if cantidad < 10:
    print("Error: Debe comparar al menos 10 números enteros!")
else:
    # Asignamos un valor máximo inicial como "menor"
    menor = float("inf")

    for i in range(cantidad):
        numero = numeros[i]
        menor = numero if numero < menor else menor

    print(f"El número menor es: {menor}")

    if menor < 10:
        print(f"El número {menor} es menor que 10!")
    else:
        print(f"El número {menor} es igual o mayor que 10!")