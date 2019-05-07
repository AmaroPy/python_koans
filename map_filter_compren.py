
def elevar(numero):
    if numero % 2 == 0:
        return numero * numero

def filtrar(n):
    if n != None:
        return n

# map(funcion, lista (tambien vale rango))

cuadrado = list(map(elevar, range(-1,11)))
clean_cuadrado = list(filter(filtrar , cuadrado))

print(cuadrado)
print(clean_cuadrado)

mi_compren = [numero * numero for numero in range(-1,11) if numero % 2 == 0]
print(mi_compren)



compren_anidada = ['{} x {} = {}'.format(numero, other_num, numero * other_num) for numero in range(1,11) for other_num in range(1,11)]

for com in compren_anidada:
    print(com)