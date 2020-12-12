class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key 
  
def boustrophedon(root):
  if root is None:
    return ## exits when at the end
  
  currentLevel = []
  nextLevel = []
  boustList = []

  rightToLeft = True
  # add the current node to the current level
  currentLevel.append(root)

  while len(currentLevel) > 0:
    cur_node = currentLevel.pop(-1)
    boustList.append(cur_node.val)

    if rightToLeft:
      if cur_node.left:
        nextLevel.append(cur_node.left)
      if cur_node.right:
        nextLevel.append(cur_node.right)
    else:
      if cur_node.right:
        nextLevel.append(cur_node.right)
      if cur_node.left:
        nextLevel.append(cur_node.left)
    
    if len(currentLevel) == 0:
        rightToLeft = not rightToLeft
        currentLevel = nextLevel
        nextLevel = []
  
  print(boustList)
    

  
  
# Driver program to test the above functions 
# Let us create the following BST 
#     1 
#    / \ 
#   2   3 
#  / \ / \ 
# 4  5 6  7 
  
root = Node(1) 
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root.right.left.left = Node(8)
root.right.left.right = Node(9)

root.right.left.right.left = Node(10)
root.right.left.right.right = Node(11)

  
# Print inoder traversal of the BST 
# inorder(root) 

# boustrophedon order:
print('boustrophedon:')
boustrophedon(root)