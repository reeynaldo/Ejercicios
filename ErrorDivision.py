try:
    num = 10 / 0
    print(num)
except ZeroDivisionError:
    print("Error: No puedes dividir numeros enteros entre cero")