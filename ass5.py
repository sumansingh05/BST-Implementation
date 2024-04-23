class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        self.root = self.insert_recursive(self.root,data)

    def insert_recursive(self,root,data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert_recursive(root.left,data)
        else:
            root.right = self.insert_recursive(root.right,data)
        return root
    
    def search(self,data):
        return self.search_recursive(self.root,data)
    
    def search_recursive(self,root,data):
        if root is None or root.data is data:
            return root
        elif data < root.data:
            return self.search_recursive(root.left,data)
        else:
            return self.search_recursive(root.right,data)

    def preorder(self):
        result = []
        self.preorder_recursive(self.root,result)
        return result
    
    def preorder_recursive(self,root,result):
        if root:
            result.append(root.data)
            self.preorder_recursive(root.left,result)       
            self.preorder_recursive(root.right,result)

    def inorder(self):
        result = []
        self.inorder_recursive(self.root,result)
        return result
    
    def inorder_recursive(self,root,result):
        if root:
            self.inorder_recursive(root.left,result)
            result.append(root.data)
            self.inorder_recursive(root.right,result)
    

    def postorder(self):
        result = []
        self.postorder_recursive(self.root,result)
        return result
    
    def postorder_recursive(self,root,result):
        if root:        
            self.postorder_recursive(root.left,result)       
            self.postorder_recursive(root.right,result)
            result.append(root.data)


bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(3)
bst.insert(9)
bst.insert(15)
bst.insert(17)
bst.insert(12)
print("Inorder Traversal:",bst.inorder())


    
