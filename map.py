numeros = [2,3,10]

def elevar(numero):
    return numero * numero

# map(funcion, lista (tambien vale rango))

cuadrado = list(map(elevar, range(1,11)))

print(cuadrado)

