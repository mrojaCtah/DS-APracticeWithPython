

dict1 = dict.fromkeys(range(0, 100), 0)
dict2 = dict.fromkeys(range(0, 1000), 0)
dict3 = dict.fromkeys(range(0, 10000), 0)

def test1():
    dict1['99'] = 1

def test2():
    dict2['999'] = 1

def test3():
    dict3['9999'] = 1

if __name__ == '__main__':

    import timeit

    print(timeit.timeit("test1()", "from __main__ import test1", number=1000))
    print(timeit.timeit("test2()", "from __main__ import test2", number=1000))
    print(timeit.timeit("test3()", "from __main__ import test3", number=1000))
