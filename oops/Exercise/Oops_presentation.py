# classes and objects
# inheritance
# abstraction
# data encapsulation
# static variables and methods
# polymorphism
# composition

# different types of animals and there properties
from abc import ABCMeta, abstractmethod


# problem statement: we need to classify different animals(HumanBeing and Pigeon) based on there attributes and
# capabilities


class Animal(metaclass=ABCMeta):
    # member variables(attributes)
    def __init__(self, animal_type=None, food_habits=None):
        self.__type = animal_type  # Vertebrate, Reptile, Amphibians
        self.__food_habits = food_habits  # Carnivore, Herbivore, Omnivorous

    @property
    def food_habits(self):
        return "I am a " + self.__food_habits

    @food_habits.setter
    def food_habits(self, food_habit):
        if food_habit in ("Carnivore", "Herbivore", "Omnivore"):
            self.__food_habits = food_habit
        else:
            print("wrong inputs, value not assigned !!")

    # member functions(capabilities)
    @abstractmethod
    def can_speak(self):
        pass

    @abstractmethod
    def can_fly(self):
        pass


class HumanBeing(Animal):
    def __init__(self, animal_type, food_habits):
        super().__init__(animal_type, food_habits)

    def can_speak(self):
        print("I can speak, I am a human")

    def can_fly(self):
        print("I cannot fly, not having wings")

    @staticmethod
    def self_reflection(self):
        print("Self reflection is my integral property")


class Bird(Animal):
    def __init__(self, animal_type, food_habits):
        super().__init__(animal_type, food_habits)

    def can_speak(self):
        print("I can speak, in birds language")

    def can_fly(self):
        print("I can fly high")

    @staticmethod
    def self_reflection(self):
        print("Self reflection is my integral property")


def main():
    human = HumanBeing("Vertebrate", "Herbivore")
    human.can_speak()
    human.can_fly()

    print(human.food_habits)


main()
