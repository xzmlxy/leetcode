def path(root):
    """
    :type
    root: TreeNode
    """
    if root is None:
        return []
    s = str(root.val) + "->"
    result = []
    if root.left is not None:
        result.extend(path(root.left))
    if root.right is not None:
        result.extend(path(root.right))
    for i in range(0, len(result)):
        result[i] = s + result[i]
    if len(result) == 0:
        return [str(root.val)]
    return result
