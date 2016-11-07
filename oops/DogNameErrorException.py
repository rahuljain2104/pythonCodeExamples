class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


try:
    dogName = raw_input("What is your dogs name : ")
    if any(char.isdigit() for char in dogName):
        raise DogNameError

except DogNameError:
    print("Your dogs name can't contain a number")

finally:
    print("It will always going to print")


