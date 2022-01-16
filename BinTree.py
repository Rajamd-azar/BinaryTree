import BinaryNode

class BTree:
    def __init__(self):
        self.root = None
 
    def inorder(self):
        if self.root is not None:
            self.root.inorder()
 
    def add(self, key):
        new_node = BinaryNode.BNode(key)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)