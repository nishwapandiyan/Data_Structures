# =========== Queue Example ===========#
class Queue:

  def __init__(self):
    self.queue = []

  def Enqueue(self,element):
    self.queue.append(element)

  def Dequeue(self):
    if self.isEmpty():
      return "Queue is Empty"
    else:
      return self.queue.pop()

  def Peek(self):
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue)

  def Size(self):
    return len(self.queue)

my_queue = Queue()

list = [10,20,30,40,50,60,70]
for i in list:
  my_queue.Enqueue(i)

print(my_queue.queue)
print(my_queue.Size())