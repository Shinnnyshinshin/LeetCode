import sys
sys.path.append("/Users/willshin/Development/LeetCode/mymodules")



import BinaryTree as bt
from collections import deque


# so we are going to extend the binary tree to have a BFS_Traversal
class BFStree(bt.Tree):
    def __init__(self):
        self.root = None
        self.bfsqueue = deque()
    
    def BFS_traversal(self, node):
        if node is None:
            # this is our base case : no root
            return   
        # add root: 
        self.bfsqueue.append(node)
        while(len(self.bfsqueue) > 0):
            print(node.val)
            node = self.bfsqueue.popleft()
            if node.left is not None:
                self.bfsqueue.append(node.left)
            if node.right is not None:
                self.bfsqueue.append(node.right)
 
global MyTree
MyTree = BFStree()
MyTree.insert(8)
MyTree.insert(3)
MyTree.insert(10)
MyTree.insert(1)
MyTree.insert(6)
MyTree.insert(4)
MyTree.insert(7)
MyTree.insert(14)
MyTree.insert(13)

# we will god 

# this is to find if a value is in the tree
#MyTree.printtree(MyTree.getRoot())
MyTree.BFS_traversal(MyTree.getRoot())


# my next task is the 3 different DFS traversals:
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
