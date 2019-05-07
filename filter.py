def elevar(numero):
    if numero % 2 == 0:
        return numero 
    

# map(funcion, lista (tambien vale rango))

cuadrado = list(filter(elevar, range(1,11)))

print(cuadrado)