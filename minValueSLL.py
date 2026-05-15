class Node:

  def __init__(self,data):
    self.data = data
    self.next = None

def get_min(head):
  minvalue = head.data
  current = head.next

  while current:
    if current.data < minvalue:
         minvalue = current.data
    current = current.next
  print(minvalue)

node1 = Node(100)
node2 = Node(29)
node3 = Node(38)
node4 = Node(42)
node5 = Node(15)
node6 = Node(60)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

get_min(node1)