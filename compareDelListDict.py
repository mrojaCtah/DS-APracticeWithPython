

# compare del operation
# of lists and dictionaries

dicto1 = dict.fromkeys(range(0, 100), 0)
dicto2 = dict.fromkeys(range(0, 10000), 0)

def dict1():
    del dicto1[99]

def dict2():
    del dicto2[97]

listo1 = list(range(100))
listo2 = list(range(10000))

def list1():
    listo1.remove(99)

def list2():
    listo2.remove(99)

if __name__ == '__main__':
    import timeit
    
    print(timeit.timeit("dict1()", "from __main__ import dict1", number=1000))
    print(timeit.timeit("list1()", "from __main__ import list1", number=1000))
    print(timeit.timeit("dict2()", "from __main__ import dict2", number=1000))
    print(timeit.timeit("list2()", "from __main__ import list2", number=1000))
