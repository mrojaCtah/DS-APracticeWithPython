newList = []
def reverseList(numList):
    if(len(numList) == 0):
        return newList
    newList.append(numList.pop())
    return reverseList(numList)

list1 = [1, 2, 3, 4]
reverseList = reverseList(list1)
print(reverseList)
