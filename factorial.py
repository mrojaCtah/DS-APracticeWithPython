def factorial(num):
    if(num == 1):
        return num
    return num * factorial(num - 1)

num1 = factorial(3)
num2 = factorial(4)
print('num 1: ' + str(num1))
print('num 2: ' + str(num2))
