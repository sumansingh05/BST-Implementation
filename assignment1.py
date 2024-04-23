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
        if root is None or root.data==data:
            return root
        if data < root.data:
            return self.helper_search(root.left,data)
        else:
            return self.helper_search(root.right,data)
        
    def inorder(self):
        result = []
        self.helper_inorder(self.root,result)
        return result
    
    def helper_inorder(self,root,result):
        if root:
            self.helper_inorder(root.left,result)
            result.append(root.data)
            self.helper_inorder(root.right,result)

    def preorder(self):
        result = []
        self.helper_preorder(self.root,result)
        return result
    
    def helper_preorder(self,root,result):
        if root:
            result.append(root.data)
            self.helper_preorder(root.left,result)
            self.helper_preorder(root.right,result)

    def postorder(self):
        result = []
        self.helper_postorder(self.root,result)
        return result
    
    def helper_postorder(self,root,result):
        if root:            
            self.helper_postorder(root.left,result)
            self.helper_postorder(root.right,result)
            result.append(root.data)

    def min_value(self,temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.data

    def max_value(self,temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.data    
    
    def delete(self,data):
        self.root = self.helper_delete(self.root,data)

          
    def helper_delete(self,root,data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.helper_delete(root.left,data)
        elif data > root.data:
            root.right = self.helper_delete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left 
            root.data = self.min_value(root.right)
            root.right = self.helper_delete(root.right,root.data) 
        return root
    
    def size(self):
        return len(self.inorder())


bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
print("Inorder traversal:",bst.inorder())
print("Preorder traversal:",bst.preorder())
print("Postorder traversal:",bst.postorder())

search_result = bst.search(40)
if search_result:
    print("40 is found in the Binary Search Tree")
else:
    print("40 is not found in the Binary Search Tree")
    
bst.delete(20)
print("Inorder traversal:",bst.inorder())
bst.delete(40)
print("Inorder traversal:",bst.inorder())

