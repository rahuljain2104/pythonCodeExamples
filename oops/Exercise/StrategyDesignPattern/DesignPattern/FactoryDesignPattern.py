# This will be the superclass for all animals
class Animal:
    def __init__(self, name="", sound=""):
        self.__name = name
        self.__sound = sound

    #      need to create getter and setter for fields/attributes
    @property
    def name(self):
        print("animal name is :" + self.__name)
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) is str:
            self.__name = name
        else:
            print("name can only have string values")


# animal = Animal(name="tommy", sound="bhau bhau")
# print(animal.name)
#
# # setting different name to animal
# animal.name = "tommy hilfiger"
# print(animal.name)
#####################################################


class Dog(Animal):
    def __init__(self, is_good_pet=None):
        self.__is_good_pet = is_good_pet

    @property
    def is_good_pet(self):
        return self.__is_good_pet

    @is_good_pet.setter
    def is_good_pet(self, is_good_pet):
        if type(is_good_pet) is bool:
            self.__is_good_pet = is_good_pet
        else:
            print("only boolean values can be assigned")


# tommy = Dog()
# tommy.name = "tommy"
# tommy.is_good_pet = False
# print("{} is a {} dog".format(tommy.name, tommy.is_good_pet))

####################################################


class Bird(Animal):
    def fly(self):
        print("I can fly")


# tweety = Bird()
# tweety.name = "tweety"
# tweety.sound = "chee chee"
# print(tweety.name)
# print(tweety.sound)


class AnimalFactory:
    def get_animal(self, animal_type):
        if animal_type == 'Dog':
            return Dog()
        if animal_type == 'Bird':
            return Bird()
        else:
            return Animal()


def main():
    animal_type = input("which animal you want")
    animal_factory = AnimalFactory()
    animal = animal_factory.get_animal(animal_type=animal_type)
    animal.name = "chimpanzze"
    print(animal.name)
    print(animal.fly())


main()
