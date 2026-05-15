class TreeNode:

  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

  def preorderTraversal(node):
    if node is None:
      return
    print(node.data, end=' ')
    TreeNode.preorderTraversal(node.left)
    TreeNode.preorderTraversal(node.right)

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeE.left = nodeG

TreeNode.preorderTraversal(root)