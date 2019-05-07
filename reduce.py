from functools import reduce

def elevar(acumulador, numero):
    return acumulador + numero
    
# importar from functools import reduce
# reduce(funcion CON 2 PARAMETROS, lista (tambien vale rango))

cuadrado = reduce(elevar, range(1,11))

print(cuadrado)