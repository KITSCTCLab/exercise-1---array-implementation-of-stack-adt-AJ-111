import os
class Stack:
    def __init__(self, size, top):
        self.items = []
        self.size = size
        self.top = top

    def is_empty(self):
        if(self.top = -1):
            print("the stack is empty")

    def is_full(self):
        if(self.top = self.size - 1):
            print("the stack is full")

    def push(self, data):
        if not self.is_full():
            self.top += 1
            self.stack.appened(data)

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            self.stack.pop()

    def status(self):
        # Write code here

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
