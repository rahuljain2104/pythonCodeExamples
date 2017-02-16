# all about oops
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        print("AbstractClass : inside bar")


class Derived(AbstractClass):
    def foo(self):
        print('Hooray!')

    def bar(self):
        print("Derived : inside bar")


d = Derived()
d.foo()
d.bar()
