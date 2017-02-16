# class Singleton:
#     class __Singleton:
#         def __init__(self, name=None):
#             self.name = name
#             print("__Singleton")
#     instance = None
#
#     def __init__(self, name):
#         if not Singleton.instance:
#             Singleton.instance = Singleton.__Singleton(name)
#         else:
#             Singleton.instance.val = name
#
# single = Singleton("Rahul")

class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)


x = OnlyOne('sausage')
print(x)
y = OnlyOne('eggs')
print(y)
z = OnlyOne('spam')
print(z)
print(x)
print(y)
