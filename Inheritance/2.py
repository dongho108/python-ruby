class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def getValue(self):
        return self.v1
        return self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1():
        return self.v1
    def add(self):
        return self.v1+self.v2
    def substract(self):
        return self.v1-self.v2

class CalMultiply(Cal):
    def multiply(self):
        return self.v1*self.v2
class CalDivide(CalMultiply):
    def divide(self):
        return self.v1/self.v2

c1 = CalMultiply(10, 10)
print(c1.add())
print(c1.multiply())

c2 = CalDivide(20,10)
print(c2, c2.add())
print(c2, c2.divide())
