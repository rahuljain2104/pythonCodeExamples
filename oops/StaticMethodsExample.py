class Sum:

    @staticmethod
    def get_sum(*args):
        sum1 = 0
        for i in args:
            sum1 += i
        return sum1


class Dog:
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1


    @staticmethod
    def getNumOfDogs():
        print("There are certainly {} dogs".format(Dog.num_of_dogs))


def main():
    spot = Dog("Spot")
    spot.getNumOfDogs()

    doug = Dog("Doug")
    doug.getNumOfDogs()
    print("Sum : ", Sum.get_sum(1, 3, 2, 4, 5))


main()
