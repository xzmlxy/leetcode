from tree.tree import TreeNode


def build_tree(preorder, inorder):

    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    length = len(preorder)
    if length == 0:
        return None
    node = TreeNode(preorder[0])
    temp = inorder.index(preorder[0])
    node.left = build_tree(preorder[1:temp + 1], inorder[0:temp])
    node.right = build_tree(preorder[temp + 1:], inorder[temp + 1:])
    return node
