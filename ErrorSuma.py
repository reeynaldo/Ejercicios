try:
    resultado =  15 + "20"
    print(resultado)

except TypeError:
    print("Error: No puedes sumar numeros enteros con cadenas (int + str = error)")