class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self.insertRecursive(self.root,data)

    def insertRecursive(self,root,data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insertRecursive(root.left,data)
        else:
            root.right = self.insertRecursive(root.right,data)
        return root
        
    def inorder(self):
        result = []
        self.inorderRecursive(self.root,result)
        return result
    
    def inorderRecursive(self,root,result):
        if root:
            self.inorderRecursive(root.left,result)
            result.append(root.data)
            self.inorderRecursive(root.right,result)

bst = BST()
bst.insert(20)
bst.insert(10)
bst.insert(2)
bst.insert(80)
bst.insert(50)
print("Inorder Traversal:",bst.inorder())