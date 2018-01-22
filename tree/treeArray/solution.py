def tree_arrays(node):

    result = []
    if node is None:
        return result
    parent_nodes = [node]
    while len(parent_nodes) > 0:
        temp = []
        temp_parent = []
        for i in range(len(parent_nodes)):
            temp.append(parent_nodes[i].val)
            if parent_nodes[i].left is not None:
                temp_parent.append(parent_nodes[i].left)
            if parent_nodes[i].right is not None:
                temp_parent.append(parent_nodes[i].right)
        result.append(temp)
        parent_nodes = temp_parent
    return result
