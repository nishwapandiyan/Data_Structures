class NodeTree:

  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

  def search(node,target):
    if node is None:
      return
    elif node.data == target:
      return node
    elif node.data < target:
      return NodeTree.search(node.right,target)
    else:
      return NodeTree.search(node.left,target)

root = NodeTree(13)
node7 = NodeTree(7)
node15 = NodeTree(15)
node3 = NodeTree(3)
node8 = NodeTree(8)
node14 = NodeTree(14)
node19 = NodeTree(19)
node18 = NodeTree(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

result = NodeTree.search(root,23)
if result:
  print(f"Result Found:{result.data}")
else:
  print("Target Not Found")