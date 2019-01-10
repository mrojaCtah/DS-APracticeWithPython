#
#
#
#
import timeit
import random

listToTime1 = list(range(100))
listToTime2 = list(range(1000))
listToTime3 = list(range(10000))
lists = [listToTime1, listToTime2, listToTime3]

def indexTester():
    for list1 in lists:
        index = list1.length() - 1
        varToFetch = list1[index]

def test1():
    varToFetch = listToTime1[99]
def test2():
    varToFetch = listToTime2[999]
def test3():
    varToFetch = listToTime3[9999]

if __name__ == '__main__':
    import timeit

    print(timeit.timeit("test1()", "from __main__ import test1", number=1000))

    print(timeit.timeit("test2()", "from __main__ import test2", number=1000))

    print(timeit.timeit("test3()", "from __main__ import test3", number=1000))
