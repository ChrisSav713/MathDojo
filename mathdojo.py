class MathDojo:
    ''''''
    def __init__(self):
        self.result = 0
    
    def add(self, num, *nums):
        for n in nums:
            num += n
        self.result = self.result + num
        return self
    
    def subtract(self, num, *nums):
        for n in nums:
            num += n
        self.result = self.result - num
        return self

# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

print(MathDojo().add(5,6,7).subtract(4,4).add(5,6,7).result)
print(MathDojo().add(1,5,4,10).add(10,15,5).add(25).add(5,5,5,5,5).subtract(25,25).result)
print(MathDojo().add(6,5,8,20).add(4,1,9,10,4).subtract(3,4,12,2).add(4,5,5,7,8).subtract(10).result)
