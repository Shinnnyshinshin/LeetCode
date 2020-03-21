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
    

    def insert_list(self, list_to_add):
        pass

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
            return self._find(val, node.left)
        elif val > node.val and node.right is not None:
            return self._find(val, node.right)
        else:
            return None
                
    def printtree(self, node):
        if node is None:
            print(" not in tree ")
        else:
            self._printtree(node)
    
    def _printtree(self, node, prefix="", isLeft=True):
        if node is not None:
            if node.right is not None:
                self._printtree(node.right, prefix + ("│   " if isLeft else "    "), False)
            
            print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))
            
            if node.left is not None:
                self._printtree(node.left, prefix + ("    " if isLeft else "│   "), True)
