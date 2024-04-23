class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        self.root = self.helper_insert(self.root,data)

    def helper_insert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.helper_insert(root.left,data)
        elif data > root.data:
            root.right = self.helper_insert(root.right,data)
        return root 
    
    def search(self,data):
        return self.helper_search(self.root,data)
    
    def helper_search(self,root,data):
        if root is None or root.data == data:
            return root
        if data < root.data:
            return self.helper_search(root.left,data)
        else:
            return self.helper_search(root.right,data)
        
    def preorder(self):
        result = []
        self.helper_preorder(self.root,result)
        return result
    
    def helper_preorder(self,root,result):
        if root:
            result.append(root.data)
            self.helper_preorder(root.left,result)
            self.helper_preorder(root.right,result)

    def inorder(self):
        result = []
        self.helper_inorder(self.root,result)
        return result
    
    def helper_inorder(self,root,result):
        if root:
            self.helper_inorder(root.left,result)
            result.append(root.data)
            self.helper_inorder(root.right,result)

    def postorder(self):
        result = []
        self.helper_postorder(self.root,result)
        return result
    
    def helper_postorder(self,root,result):
        if root:
            self.helper_postorder(root.left,result)
            self.helper_postorder(root.right,result)
            result.append(root.data)


    
bst = BST()
bst.insert(10)
bst.insert(90)
bst.insert(100)
bst.insert(40)
bst.insert(50)
bst.insert(70)
print("Inorder traversal:",bst.inorder())
print("Preorder traversal:",bst.preorder())
print("Postorder traversal:",bst.postorder())

    

        
