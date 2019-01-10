import math

numList = [0, math.pi/3, math.pi * 2/3, math.pi, math.pi * 4/3, math.pi * 5/3, 2*math.pi]



def shittyLab(inputs):

    totalSum = 0
    for x in inputs:
        a = math.sin(x) * math.sin(x)
        b = 2 * x * math.cos(x) * math.sin(x)
        c = x * x * math.cos(x) * math.cos(x)
        d = 1

        sumParts = a + b + c + d

        finalPiece = math.sqrt(sumParts)

        

        if(numList.index(x) == 0 or numList.index(x) == 6):
            totalSum += finalPiece
        elif((numList.index(x) % 2) != 0):
            newNum1 = finalPiece * 4
            totalSum += newNum1
        elif((numList.index(x) % 2) == 0):
            newNum2 = finalPiece * 2
            totalSum += newNum2

    finalProduct = totalSum * (math.pi/9)       

    print("final product = " + str(finalProduct))

shittyLab(numList)
