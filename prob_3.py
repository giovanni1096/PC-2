numeros_pares = []
numeros_impares = []

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()

    if respuesta != "SI":
        break  # Salir del bucle si la respuesta no es "SI"

    numero = int(input("Ingrese el número: "))
    
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

numeros_ingresados = numeros_pares + numeros_impares
print("Números ingresados:", numeros_ingresados)

print("Cantidad de números pares:", len(numeros_pares))
print("Cantidad de números impares:", len(numeros_impares))