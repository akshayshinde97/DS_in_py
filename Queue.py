
class Queue:
    '''implementation of Queue using list in python'''
    def __init__(self):
        self.queue = []

    def enqueue(self,inp):
        """add element at the end of the queue"""
        self. queue.append(inp)

    def dequeue(self):
        """removes the least recent(first in the queue) element """
        if(len(self.queue)):
            return self.queue.pop(0) #time complexity is O(N)
        else:
            return "queue is empty"

    def display(self):
        if(len(self.queue)):
            return self.queue
        else:
            return "queue is empty"

q = Queue()   

print(q.display())
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.display())

