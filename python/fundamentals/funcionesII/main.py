
# EJERCICIO 1
def cuentaRegresiva(num):
    lista=[]
    for x in range(num,-1,-1):
        lista.append(x)
    return lista

print(cuentaRegresiva(3))
print(cuentaRegresiva(8))

# EJERCICIO 2

def imprime_devuelve (lista2):
    if len(lista2)==0:
        return "Lista vacía"
    else: print(lista2[0])
    if len(lista2)<2:
        return "Fin lista"
    else: return lista2[1]


print(imprime_devuelve([4,5,6,7]))

# EJERCICIO 3
def primero_mas_tamano(lista3):
    sum=lista3[0]+len(lista3)
    return sum

print(primero_mas_tamano([2,1,3,1,3]))

# EJERCICIO 4
def mayores_que_segundo(lista4):
    if len(lista4)<2:
        return False
    lista42=[]
    for x in range(0,len(lista4),1):
        if lista4[x]>lista4[1]:
            lista42.append(lista4[x])
    return lista42

print(mayores_que_segundo([3]))
print(mayores_que_segundo([3,2,5,6,7,0,1]))

# EJERCICIO 5
def longitud_valor (lon,val):
    lista5=[]
    for x in range(lon):
        lista5.append(val)
    return lista5

print(longitud_valor(5,1))
