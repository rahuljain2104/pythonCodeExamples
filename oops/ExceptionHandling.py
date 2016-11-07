try:
    a_list = [1, 2, 3]
    print(a_list[3])

except(IndexError, NameError):
    print("Sorry that index doesn't exist")

except:
    print("An unknown error occured")
