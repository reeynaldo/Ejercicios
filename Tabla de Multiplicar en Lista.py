
numero = int(input("1.Ingrese el numero de la tabla de multiplicar que desee: "))
print("Su numero es: ", numero)
M = 1

while numero < 1:
    print("Erro: 1. El numero introducido no puede ser menor que cero.")
    numero = int(input("1.Ingrese el numero de la tabla de multiplicación que desee: "))

while M < 11:

    r = numero * M
    M = M + 1

    tabla = [numero, 'x', M - 1, '=', r]

    print("[", tabla[0], tabla[1], tabla[2], tabla[3], tabla[4], "]")