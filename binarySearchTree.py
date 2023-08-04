class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        break
                elif value > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        break
                else:
                    break 
    

    def search(self, value):
        current = self.root
        while current:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    
if __name__ == "__main__":
    bst = binarySearchTree()

    # Insert elements
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    # Search for an element
    print(bst.search(4))  
    print(bst.search(9))  
