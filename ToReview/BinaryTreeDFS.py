import sys
sys.path.append("/Users/willshin/Development/LeetCode/mymodules")

from collections import deque

import BinaryTree as bt

# so we are going to extend the binary tree to have a BFS_Traversal
class DFStree(bt.Tree):
    def __init__(self):
        self.root = None
        self.dfsstack = deque()

    def preOrder(self, node):
        if node is None:
            return
        print(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val)


    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.val)
        self.inOrder(node.right)

"""
Tree Traversals (Inorder, Preorder and Postorder)
Unlike linear data structures (Array, Linked List, Queues, Stacks, etc) which have only one logical way to traverse them, trees can be traversed in different ways. Following are the generally used ways for traversing trees.


│       ┌── 14
│   ┌── 10
│   │   └── 9
└── 8
    │   ┌── 6
    └── 3
        └── 2


(A) InOrder (Left, Root, Right) : 2, 3, 6, 8, 9, 10, 14
(B) PreOrder (root, left, rghgt) : 8, 3, 2, 6, 10, 9, 14
(C) postOrder  (left, right, rot): 2, 6, 3, 9, 14, 10, 8
        
 """


global MyTree
MyTree = DFStree()
MyTree.insert(8)
MyTree.insert(3)
MyTree.insert(10)
MyTree.insert(2)
MyTree.insert(6)
MyTree.insert(9)
MyTree.insert(14)


# this is to find if a value is in the tree
print("Here is a graphic of the current tree")
#MyTree.printtree(MyTree.getRoot())

print("preOrder Traversal")
MyTree.preOrder(MyTree.getRoot())
print("postOrder Traversal")
MyTree.postOrder(MyTree.getRoot())
print("inOrder Traversal")
MyTree.inOrder(MyTree.getRoot())

