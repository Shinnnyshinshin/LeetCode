# First thing I will need to do is build my own binary tree and traversal algorithm
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(TreeNode):
    def __init__(self):
        self.root = None
    
    def getRoot(self):
        return self.root
    
    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)
            
    def _insert(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(val, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(val, node.right)

    def find(self, val):
        if self.root == None:
            return None
        else:
            return self._find(val, self.root)
    
    def _find(self, val, node):
        if val == node.val:
            return node
        elif val < node.val and node.left is not None:
            self._find(val, node.left)
        elif val > node.val and node.right is not None:
            self._find(val, node.right)
                
                
    def printtree(self):
        if self.root is not None:
            self._printtree(self.root)
    
    def _printtree(self, node):
        if node is not None:
            self._printtree(node.left)
            print(str(node.val) + ' ')
            self._printtree(node.right)