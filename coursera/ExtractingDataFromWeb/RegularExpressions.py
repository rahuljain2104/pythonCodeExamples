import re

train_finddigits = open('regex_sum_340266.txt', 'r')
test_finddigits = open('regex_sum_42.txt', 'r')


def find_sum_of_digits_in_file(input_file):
    data = input_file.read()
    digits = []
    digits = re.findall('[0-9]+', data)
    summation = 0

    for digit in digits:
        summation += int(digit)
    return summation


print find_sum_of_digits_in_file(test_finddigits)
print find_sum_of_digits_in_file(train_finddigits)
