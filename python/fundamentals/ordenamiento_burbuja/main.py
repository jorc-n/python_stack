
def burbuja(arr):

    for x in range (len(arr)-1):
        for j in range (len(arr)-1-x):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(burbuja([6,5,3,1,8,7,2,4]))