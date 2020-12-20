for x in range (151):
    print(x)

for cinco in range (5,1001,5):
    print(cinco)

for dojoWay in range (101):
    if dojoWay % 10==0:
        print("CODIN DOJO")
    elif dojoWay % 5 ==0:
        print("CODIFICACIÓN")
    else:
        print(dojoWay)
suma=0
for sumaImpares in range (500001):
    if sumaImpares%2==1:
        suma=suma+sumaImpares
print(suma)

for regresiva in range (2018, 0, -4):
    print(regresiva)

lowNum=2
highNum=9
mult=3
for contFlex in range (lowNum, highNum+1, 1):
    if contFlex%mult==0:
        print(contFlex)
