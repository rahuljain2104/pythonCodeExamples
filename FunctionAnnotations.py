
# def random_func(name: str, age: int, weight: float) -> str:
#     print("Name: ",str)
#     print("Age: ",age)
#     print("Weight: ",weight)

sum = lambda x, y: x+y

print(sum(2, 3))

can_vote = lambda age: True if age>=18 else False

print(can_vote(19))

powerList = [lambda x:x**2,
             lambda x: x**3,
             lambda x: x**4]

for func in powerList:
    print(func(4))

# attack = {'quick':(lambda x :print("Quick Attack")),
#           'power':(lambda x :print("power Attack")),
#           'miss':(lambda  x :print("Missed Attack"))
#          }
#
# attack['quick']()
#
# import random
#
# attackKey = random.choice(list(attack.keys()))
#
# attack[attackKey]()
import random as rnd

# create the list
lst = []

# populate the list with 100 H and T
for i in range(1, 101):
    lst += rnd.choice(['H', 'T'])

# Output the results
print("Heads : ", lst.count('H'))
print("Tails : ", lst.count('T'))

####### Map Function #########
oneTo10 = range(1, 11)

def dbl_num(num):
    return num*2

print(list(map(dbl_num, oneTo10)))
print(list(map(lambda x: x*3, oneTo10)))

aList = list(map((lambda x, y:x+y),[1, 2, 3], [4, 5, 6]))

print(aList)


########### Filter ##############

print(list(filter((lambda x: x%2 == 0), range(1,11))))

########### Filter Multiples of 9 ############
# ########### generate random list of 100 values ##########

randList = list(rnd.randint(1, 1001) for i in range(100))
print(list(filter((lambda x: x%9 == 0), randList)))


######### reduce - returns a single result #########
print(reduce((lambda x,y: x+y), range(1, 6)))


