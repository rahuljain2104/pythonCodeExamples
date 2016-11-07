# iterable - stored list of values
# iterator -
# list comprehension

# print([i**2 for i in range(50) if i % 8 == 0])
#
# print([x*y for x in range(20) for y in range(4)])
#
# # list comprehension inside of list comprehension
# print([x for x in [i*2 for i in range(10)] if x % 8 == 0])

# generate list of 50 random values from 1000 numbers and
# print multiples of 9
import random as r
print([x for x in [r.randint(1, 1001) for i in range(50)] if x % 9 == 0])

############### multi dimensional list ##################
multiList = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

print([col[1] for col in multiList])

print([multiList[i][i] for i in range(len(multiList))])

############## generator function ################
# to get the large number of results

def isprime(num):

    for i in range(2, num):

        if num % i == 0:
            return False

    return True


def gen_primes(max_number):
    for num1 in range(2, max_number):

        if isprime(num1):
            yield num1


prime = gen_primes(50)

print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))