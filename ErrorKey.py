try :

    colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
    colores['blanco']
    print("El color es", colores)

except KeyError:
        print("Error: La clave no esta en el diccionario")