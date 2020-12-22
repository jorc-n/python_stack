
def orden_seleccion(arr):
    pos=0
    for x in range(len(arr)):
        nuevo_menor=arr[x]
        for j in range (x,len(arr)):
            if arr[j]<nuevo_menor:
                nuevo_menor=arr[j]
                arr[j],arr[x]=arr[x], arr[j]
    return arr

print(orden_seleccion([6,9,5,1,2,4]))
