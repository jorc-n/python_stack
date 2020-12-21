import random
def randInt(min=0, max=100 ):
    if (max < 0):
        max = max * (-1)
        print("Se consideró valor absoluto de número")
    if(min>max):
        max=min
        min=0
        print("Se reasignaron los valores máximo y mínimo")
    num = random.random()*max + min
    return round(num)
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
print(randInt(max=-50))


