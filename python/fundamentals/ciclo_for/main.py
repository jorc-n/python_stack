
# EJERCICIO 1
def biggie_size(lista1):
    for x in range(len(lista1)):
        if lista1[x]>0:
            lista1[x]="big"
    return lista1

print(biggie_size([0,1,2,4,-4]))

#EJERCICIO 2

def cuenta_positivos(lista2):
    sum=0
    for x in range (len(lista2)):
        if lista2[x]>0:
            sum+=1
    lista2[len(lista2)-1]=sum
    return lista2

print(cuenta_positivos([0,1,1,1,0]))

# EJERCICIO 3

def suma_total(lista3):
    sum=0
    for x in range(len(lista3)):
        sum=sum+lista3[x]
    return sum

print(suma_total([1,1,1,1,1,1]))
print(suma_total([6,3,-2]))

# EJERCICIO 4

def promedio(lista4):
    sum=0
    for x in range(len(lista4)):
        sum=sum+lista4[x]
    return sum/len(lista4)

print(promedio([1,2,3,4]))

# EJERCICIO 5

def longitud(lista5):
    return len(lista5)

print(longitud([1,1,1,1,1]))

# EJERCICIO 6

def minimo (lista6):
    if len(lista6)==0:
        return False
    min=lista6[0]
    for x in range(len(lista6)):
        if lista6[x]<min:
            min=lista6[x]
    return min

print(min([1,1,0,1,1,1]))
print(minimo([37,2,1, -9]))
print(minimo([]))

# EJERCICIO 7
def maximo (lista7):
    if len(lista7)==0:
        return False
    max=lista7[0]
    for x in range(len(lista7)):
        if lista7[x]>max:
            max=lista7[x]
    return max
print(maximo([37,2,1, -9]))
print(maximo([]))

# EJERCICIO 8

def analisis_final(lista8):
    if len(lista8)==0:
        return False
    diccionario={}
    diccionario["sumatotal"]=suma_total(lista8)
    diccionario["promedio"]= promedio(lista8)
    diccionario["minimo"]=minimo(lista8)
    diccionario["maximo"]=maximo(lista8)
    diccionario["longitud"]=longitud(lista8)
    return  diccionario

print(analisis_final([37,2,1,-9]))

# EJERCICIO 9
def inverso(lista9):
    return lista9[::-1]

print(inverso([37,2,1,9]))

