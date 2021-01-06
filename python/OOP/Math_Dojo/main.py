
class MathDojo:
    def __init__(self):
    	self.result = 0

    def add(self, num, *nums):
        self.result=num
        for x in nums:
            self.result+=x
        print("suma ",self.result)
        return self

    def subtract(self, num, *nums):
        self.result = num
        for y in nums:
            self.result -= y
        print("resta ", self.result)
        return self
# crear una instruccion:

md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).add(3,2,6,8,9).result
print(x)	# debe imprimir 5

test_resta=MathDojo()

test_resta.subtract(4).subtract(9,4,3,1).subtract(6,4)
