





# couple lines down
# Author: Connor Burk

class Queue:

    def __init__(self):
        
        self.items = []

    def __str__(self):

        return str(self.items)

    def isEmpty(self):

        return self.items == []

    def enqueue(self, item):
        
        self.items.insert(0, item)

    def dequeue(self):
        
        return self.items.pop()

    def size(self):

        return len(self.items)


# programming exercise
# --------------------
# implement a Queue ADT,
# such that the rear of the Queue
# is at the end of the list
# --------------------
# note: enqueue() is now O(1) instead of O(n)
# note 2: dequeue() is now O(n) instead of O(1)

class ReverseQueue:

    def __init__(self):

        self.items = []

    def __str__(self):

        return str(self.items)

    def isEmpty(self):

        return self.items == []

    def size(self):

        return len(self.items)

    def enqueue(self, item):

        self.items.append(item)

    def dequeue(self):

        return self.items.pop(0)



# test times between Queue() and ReverseQueue()
# for methods enqueue() and dequeue()

queueSize1 = Queue()
for x in range(1000):
    queueSize1.enqueue(x)

queueSize2 = Queue()
for x in range(10000):
    queueSize2.enqueue(x)

queueSize3 = Queue()
for x in range(100000):
    queueSize3.enqueue(x)

def q1(num):
    queueSize1.enqueue(num)

def q2(num):
    queueSize2.enqueue(num)

def q3(num):
    queueSize3.enqueue(num)

reverseQueueSize1 = ReverseQueue()
for x in range(1000):
    reverseQueueSize1.enqueue(x)

reverseQueueSize2 = ReverseQueue()
for x in range(10000):
    reverseQueueSize2.enqueue(x)

reverseQueueSize3 = ReverseQueue()
for x in range(100000):
    reverseQueueSize3.enqueue(x)

def rq1(num):
    reverseQueueSize1.enqueue(num)

def rq2(num):
    reverseQueueSize2.enqueue(num)

def rq3(num):
    reverseQueueSize3.enqueue(num)
        

# take times
if __name__ == '__main__':

    import timeit
    print(timeit.timeit("q1(10)", "from __main__ import q1", number = 1000))
    print(timeit.timeit("q2(100)", "from __main__ import q2", number = 1000))
    print(timeit.timeit("q3(1000)", "from __main__ import q3", number = 1000))
    print(timeit.timeit("rq1(10)", "from __main__ import rq1", number = 1000))
    print(timeit.timeit("rq2(100)", "from __main__ import rq2", number = 1000))
    print(timeit.timeit("rq3(1000)", "from __main__ import rq3", number = 1000))    
