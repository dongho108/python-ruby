class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v, int):
            self.v1 = v1
        if isinstance(v, int):
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

c1 = Cal(10,10)
print(c1.add())
print(c1.substract())
c1.setV1('one')
c1.getV1()

c2 = Cal(30, 20)
print(c2.add())
print(c2.substract())
