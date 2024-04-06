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

    def min_value(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data
    
    def max_value(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data
    
    def delete(self,data):
        self.root = self.delete_recursive(self.root,data)

    def delete_recursive(self,root,data):
        if root is None:
            return None
        elif data < root.data:
            root.left = self.delete_recursive(root.left,data) 
        elif data > root.data:
            root.right = self.delete_recursive(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.data = self.min_value(root.right)
            root.right = self.delete_recursive(root.right,root.data)
        return root 


    def size(self):
        return len(self.inorder())


bst = BST()
bst.insert(60)
bst.insert(10)
bst.insert(100)
bst.insert(34)
bst.insert(84)  
bst.insert(89)
print("Inorder Traversal:",bst.inorder())
print("Preorder Traversal:",bst.preorder())
print("Size of Binary Search Tree ",bst.size())
print("Minimum value of Binary Search Tree ",bst.min_value())
print("Maximum value of Binary Search Tree ",bst.max_value())

search_result = bst.search(84)
if search_result:
    print("84 is found in Binary Search Tree")
else:
    print("84 is not found in Binary Search Tree")

bst.delete(100)
print("Inorder Traversal after deleting a Node :",bst.inorder())
print("Size of Binary Search Tree ",bst.size())
print("Minimum value of Binary Search Tree ",bst.min_value())
print("Maximum value of Binary Search Tree ",bst.max_value())
