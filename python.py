def depth_limited_search(tree, node, goal, depth_limit):
    if node == goal:
        return True
    if depth_limit == 0:
        return False
    if node not in tree:
        return False
    for child in tree[node]:
        if depth_limited_search(tree, child, goal, depth_limit - 1):
            return True
    return False

if __name__ == "__main__":
    # Build the tree structure as a dictionary
    tree = {
        "X": ["A", "B"],
        "A": ["C", "D"],
        "B": ["I", "J"],
        "c": ["E", "F"],
        "D": ["G"],
        "I": ["H"],
        "J": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
    }

    # Replace 'goal_node' with your actual goal node value.
    goal_node = "H"
    depth_limit = 3  # Set the depth limit according to your requirements.

    if depth_limited_search(tree, "X", goal_node, depth_limit):
        print("Goal found at " + goal_node)
    else:
        print("Goal not found.")
