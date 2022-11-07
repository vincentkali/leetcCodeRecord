from functools import reduce

# Examples :-

my_list = [1, 2, 8, 50, 90]

# Without Lambda function :-


def sumAll(num1, num2):

    return num1 + num2


result = reduce(sumAll, my_list)

print(result)

# my_list = [ 1, 2, 8, 50, 90 ]  ==> 1 + 2 = 3 / 3 + 8 = 11 / 11 + 50 = 61 / 61 + 90 = 151

print("-" * 100)

# with Lambda function :-

my_list = [1, 2, 8, 50, 90]

result = reduce(lambda num1, num2: num1 + num2, my_list)

print(result)
print(sum(my_list))