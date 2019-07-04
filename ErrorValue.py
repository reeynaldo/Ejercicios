def Valor(lista,elemento):

    try:
        if elemento in lista:
            raise ValueError

        else:
            lista.appende(elemento)
            return lista

    except ValueError:
        print("Error: Elementos duplicados")
        return lista

lista = [1, 2, 3, 4, 5, 6]

print(Valor(lista, 6))