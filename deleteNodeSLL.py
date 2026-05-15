class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

def print_items(head):
  current = head

  while current:
    print(current.data,end='->')
    current = current.next
  print("Null")

def delete_items(head,deleteitem):
  if head == deleteitem:
    return head.next

  current = head
  while(current.next and current.next != deleteitem):
    current = current.next

  if current.next is None:
    return head

  current.next = current.next.next
  return head

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print("List Before Deletion:")
print_items(node1)
node1 = delete_items(node1,node6)
print("List Before Deletion:")
print_items(node1)