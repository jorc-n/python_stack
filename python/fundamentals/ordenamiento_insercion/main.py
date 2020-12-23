
def ordenamiento_insercion(arr):

    for x in range (len(arr)):
        for j in range (x):
            if arr[j]>arr[x]:
                menor=arr[x]
                for k in range(x,j-1,-1):
                    arr[k]=arr[k-1]
                arr[j]=menor
    return arr

print(ordenamiento_insercion([6,2,1,7,5,9,8,0]))
