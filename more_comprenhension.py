numbers = [2, 3, 10]



# nombre de lista = [ lo que quieres añadir, bucle/bucles, condicion si existe]
# nombre de lista = [ lo que quieres añadir o funcion, bucle/bucles ]

def cuadrado(num):
    return num * num

less_than_ten = [cuadrado(number) for number in numbers]

print(less_than_ten)