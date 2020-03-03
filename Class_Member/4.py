class Cal(object):
    _history = []
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
        result = self.v1 + self.v2
        Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))
        return result
    def substract(self):
        result = self.v1 - self.v2
        Cal._history.append("substract : %d-%d=%d" % (self.v1, self.v2, result))
        return result
    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)

class CalMultiply(Cal):
    def multiply(self):
        result = self.v1 * self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result
class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1 / self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result

c1 = CalMultiply(10, 10)
print(c1.add())
print(c1.multiply())

c2 = CalDivide(20,10)
print(c2, c2.add())
print(c2, c2.divide())

Cal.history()
