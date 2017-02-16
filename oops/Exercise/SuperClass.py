class SuperClass:
    def __init__(self):
        __var1 = None
        var2 = None

    def __add__(self):
        return self.var1 + self.var2

    def __mult(self):
        print("inside super class")
        return self.var1 * self.var2

    def mult(self):
        return self.__mult()


class SubClass(SuperClass):
    def __init__(self):
        var3 = None

    def average(self):
        return (self.var1 + self.var2 + self.var3) / 3

    def mult(self):
        print(super(SubClass, self).mult())
        print("inside sub class")
        return self.var1 * self.var2 * self.var3


sObj = SuperClass()
sObj.var1 = 5
sObj.var2 = 10
print(sObj.__add__())
print(sObj.mult())

subObj = SubClass()
subObj.var3 = 15
subObj.var1 = 5
subObj.var2 = 50
print(subObj.average())
print(subObj.mult())
