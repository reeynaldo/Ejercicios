def Numeros(num1,num2):
    num = 0

    if num1 > num2:
        num = num2 + 1

    elif num1 < num2:
            num = num2 - 1

            for num in range(num1 + 1,num2):
                print(num)

Numeros(1,10)

