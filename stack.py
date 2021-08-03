from collections import deque

class Stack():
    """python implementation of stack datastructure usig Deque"""
    def __init__(self):
        self.data = deque()

    def push(self,inp):
        """takes int or string as input and add it on top of other element in stack"""
        self.data.append(inp)
    
    def pop(self):
        """removes the top most element in stack"""
        if(len(self.data)!=0):
            return self.data.pop()
        else:
            return "Stack is empty"
    
    def peek(self):
        """returns the top most element in stack"""
        if(len(self.data)!=0):
            return self.data[-1]
        else:
            return "Stack is empty"
            
    def isempty(self):
        """returns true if stack is empty and false otherwise """
        if(len(self.data)==0):
            return True
        else:
            return False
    
    def size(self):
        """ returns the size of stack """
        return len(self.data)

s = Stack()
s.push(1)
print(s.size())
print(s.isempty())
print(s.peek())
print(s.pop())

