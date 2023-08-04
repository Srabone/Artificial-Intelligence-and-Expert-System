def perform_depth_limited_search(tree, node, goal, depth_limit):
    if node == goal:
        return True
    if depth_limit == 0:
        return False
    if depth_limit > 0:
        for child in tree.get(node, []):
            if perform_depth_limited_search(tree, child, goal, depth_limit - 1):
                return True
    return False

def iterative_deepening_search(tree, start, goal):
    depth_limit = 0
    while True:
        if perform_depth_limited_search(tree, start, goal, depth_limit):
            return True
        else:
            depth_limit += 1
    

if __name__ == "__main__":
    # Build the tree structure as a dictionary
    tree = {
        "S": ["A", "C"],
        "A": ["D", "B"],
        "C": ["E", "G"],
        "D": ["F", "H"],
        "E": ["I"],
        "B": [],
        "G": [],
        "F": [],
        "H": [],
        "I": [],
    }

    # Replace 'goal_node' with your actual goal node value.
    goal_node = "G"

    if iterative_deepening_search(tree, "S", goal_node):
        print(goal_node + " Goal found " )
    else:
        print("Goal not found.")
