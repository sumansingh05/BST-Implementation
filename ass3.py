class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self.insert_Recursive(self.root,data)

    def insert_Recursive(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert_Recursive(root.left,data)
        elif data > root.data:
            root.right = self.insert_Recursive(root.right,data)
        return root
    
    def preorder(self):
        result = []
        self.preorder_Recursive(self.root,result)
        return result
    
    def preorder_Recursive(self,root,result):
        if root:
            result.append(root.data)
            self.preorder_Recursive(root.left,result)            
            self.preorder_Recursive(root.right,result)
    
    def inorder(self):
        result = []
        self.inorder_Recursive(self.root,result)
        return result
    
    def inorder_Recursive(self,root,result):
        if root:
            self.inorder_Recursive(root.left,result)
            result.append(root.data)
            self.inorder_Recursive(root.right,result)

    def postorder(self):
        result = []
        self.postorder_Recursive(self.root,result)
        return result
    
    def postorder_Recursive(self,root,result):
        if root:            
            self.postorder_Recursive(root.left,result)            
            self.postorder_Recursive(root.right,result)
            result.append(root.data)

    def size(self):
        return len(self.inorder())
    
    
bst = BST()
bst.insert(45)
bst.insert(25)
bst.insert(95)
bst.insert(200)
bst.insert(1)
bst.insert(40)
bst.insert(84)
print("Inorder traversal:",bst.inorder())
print("Length of Binary Search Tree ",bst.size())
print("Preorder traversal:",bst.preorder())
print("Length of Binary Search Tree ",bst.size())
print("Root of Binary Search Tree is ",bst.root.data)
print("Postorder traversal:",bst.postorder())

        
            

