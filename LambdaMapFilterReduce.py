# def get_func_mult_by_num(num):
#
#     def mult_by(value):
#         return num*value
#
#     return mult_by
#
#
# generated_func = get_func_mult_by_num(5)
# print("5*10 = ", generated_func(10))
#
# listOfFuncs = [times_two, generated_func]
#
# print("5*9=", listOfFuncs[1](9))

def is_it_odd(num):
    if num % 2 is not 0:
        return True
    else:
        return False


def change_list(lst, func):
    oddList = []

    for element in lst:
        if func(element):
            oddList.append(element)

    return oddList

aList = range(1, 20)
print(change_list(aList, is_it_odd))

