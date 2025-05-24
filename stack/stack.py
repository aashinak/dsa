from collections import deque

stack = deque()
stack.append("one")
stack.append("two")
stack.append("three")
stack.append("four")
stack.append("five")
stack.append("six")
print(stack)
print(stack.pop())
print(stack)


class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

stack = Stack()
stack.push("one")
stack.push("two")
stack.push("three")
print(stack.size())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.size())