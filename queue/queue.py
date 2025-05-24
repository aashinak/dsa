from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enque(self, val):
        self.buffer.appendleft(val)
        print(self.buffer)
    
    def deque(self):
        if not self.is_empty():
            print(self.buffer)
            return self.buffer.pop()
        return "Queue empty"

    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
q = Queue()
q.enque("one")
q.enque("two")
q.enque("three")
q.enque("four")

print(q.deque())
print(q.deque())
print(q.deque())
print(q.deque())
print(q.deque())
