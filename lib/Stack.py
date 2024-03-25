class Stack:

    def __init__(self, items = [], limit = 100):
        # if items is None:
        #     items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item) if len(self.items) < self.limit else Exception('Stack is full.')

    def pop(self):
        self.items.pop() if len(self.items) > 0 else Exception('Stack is empty.')

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        print (len(self.items) >= self.limit) 
        return len(self.items) >= self.limit 

    def search(self, target):
        try:
            index = self.items.index(target)
            return len(self.items) - index - 1
        except ValueError:
            return -1

    def empty(self):
        print (len(self.items) == 0)
        return len(self.items) == 0  
    
    def __str__(self): # to convert the resulting object to a string
        return str(self.items)
    
stk = Stack([1,2,3,4,5], 10)
print(stk)
stk.full()
stk.empty()
print(stk.pop())
print('\n')
print(stk)
print(stk.push(7))
print(stk)
print('\n')
print(stk.search(1))
print(stk.size())
print(stk.peek())
print(stk.isEmpty())