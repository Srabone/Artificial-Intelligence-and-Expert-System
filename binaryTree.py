def create_node(current, left=None, right=None):
    return [current, left, right]

def preorder_traversal(node):
    if node is not None:
        print(node[0], end=' ')
        preorder_traversal(node[1])
        preorder_traversal(node[2])

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node[1])
        print(node[0], end=' ')
        inorder_traversal(node[2])

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node[1])
        postorder_traversal(node[2])
        print(node[0], end=' ')


if __name__ == "__main__":
    root = create_node('a',
                       left=create_node('b',
                                        left=create_node('c'),
                                        right=None),
                       right=create_node('d',
                                        left=create_node('e'),
                                        right=create_node('f')),
    )

    print("Pre-order Traversal:", end=" ")
    preorder_traversal(root)

    print("\nIn-order Traversal:", end=" ")
    inorder_traversal(root)

    print("\nPost-order Traversal:", end=" ")
    postorder_traversal(root)
