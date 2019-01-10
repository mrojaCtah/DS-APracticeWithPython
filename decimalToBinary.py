from pythonds.basic.stack import Stack
import math

def myDivideByTwo(decimalNum):
    
    stack = Stack()
    counter = 0
    cont = True
    newNum = 0
    
    while(cont):
        newNum = decimalNum // 2
        remainderNum = decimalNum % 2
        stack.push(remainderNum)
        if(newNum == 0):
            cont = False
    while(not stack.isEmpty()):
        x = stack.pop()
        num2Add = x * math.pow(10, counter)
        newNum += num2Add
        counter += 1
    return newNum

print(myDivideByTwo(42))
