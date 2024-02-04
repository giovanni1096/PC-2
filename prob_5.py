def contar_digitos(numero, digito):
   
    numero_str = str(numero)
    
   
    cantidad = numero_str.count(str(digito))
    
    
    print(f"Cantidad de veces {digito} en el número {numero}: {cantidad}")

numero_ingresado = 15789000
digito_a_contar = 0

contar_digitos(numero_ingresado, digito_a_contar)