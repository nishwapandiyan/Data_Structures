class Node:

  def __init__(self,data):
    self.data = data
    self.next = None

def print_details(head):
  current = head
  while current:
    print(current.data,end='->')
    current = current.next
  print("Null")

def insertNode(head,newNode,position):
  if position == 1:
   newNode.next = head
   return newNode

  current = head
  for _ in range(position - 2):
    if current.next is None:
      break
    current = current.next

  newNode.next = current.next
  current.next = newNode
  return head


node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(50)
node5 = Node(60)
node6 = Node(70)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print_details(node1)
newNode = Node(90)
node1 = insertNode(node1,newNode,4)
print_details(node1)