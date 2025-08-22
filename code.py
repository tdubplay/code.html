#exercide num 3
def reverses(self):
    stack = []

    for letters in self:
        stack.append(letters)

    empty = ""
    while stack:
        empty += stack.pop()

    return empty

myinput = "HELLO"
myoutput = reverses(myinput)
print("Input:" ,myinput)
print("Output:" ,myoutput)

#exercide num 4
from collections import deque
queue = deque()

queue.append("Alice")
print("\nEnqueue: Alice")

queue.append("Bob")
print("Enqueue: Bob")

queue.append("Charlie")
print("Enqueue: Charlie")

serving = queue.popleft()
print("Serve ->", serving)
print("Queue:", list(queue))

#exercide num 5
def balance(self):
    stack = []
    if self in "({[":
        stack.append(self)
    elif self in ")}]":
        if not stack:
            return "Not Balance"

balance = balance("")
