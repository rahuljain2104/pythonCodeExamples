# need to define attributes and capabilities

class Square:
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the height")

        # __ for private data
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
            print("this is a digit")
        else:
            print("please enter only numbers for height")


    @property
    def width(self):
        print("Retrieving the width")

        # __ for private data
        return self.__width


    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("please enter only numbers for width")


    def get_area(self):
        return int(self.width)*int(self.height)


def main():
    aSquare = Square()
    aSquare.height = 20
    aSquare.width = int(20)

    print "Area is : " + str(aSquare.get_area())


main()