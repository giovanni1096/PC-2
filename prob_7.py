def es_primo(numero):
    
    if numero <= 1:
        return False
   
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True
numero_ingresado = int(input("Ingrese un número para verificar si es primo: "))

if es_primo(numero_ingresado):
    print(f"{numero_ingresado} es un número primo.")
else:
    print(f"{numero_ingresado} no es un número primo.")