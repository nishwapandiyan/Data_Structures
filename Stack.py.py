
class Stack:
  def __init__(self):
    self.stack = []

  def push(self,element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is Empty"
    else:
      return self.stack.pop()

  def peek(self):
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

mystack = Stack()

list = [10,20,30,40,50,60,70]

for i in list:
  mystack.push(i)

print(mystack.stack)
print(mystack.peek())
print(mystack.isEmpty())
print(mystack.size())
