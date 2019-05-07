numbers = [1, 2, 3, 10, 11, 15, 99]

def algo(n):
    if n % 2 != 0:
        return True
    return False

def both_requisites(n):
    if algo(n) and n > 10:
        return True
    return False


higher_than_ten = [num for num in numbers if both_requisites(num)]

print(higher_than_ten)

nombres = ['Alicia', 'María', 'Amaro']
acciones = [' salta', ' llora', ' rasca']

for nombre in nombres:
    for accion in acciones:
        print(nombre + accion)

for num in range(1,11):
    for s_num in range(1,11):
        print('{} * {} = {}'.format(num, s_num, num * s_num))

