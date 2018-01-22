class NextTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def connect(self, root):
        if root is not None:
            self.connect_list([root])

    def connect_list(self, root):
        if root[0].left is None:
            return
        i = 0
        next_root = []
        temp = len(root) - 1
        while i < temp:
            root[i].left.next = root[i].right
            root[i].right.next = root[i + 1].left
            next_root.append(root[i].left)
            next_root.append(root[i].right)
            i += 1
        root[i].left.next = root[i].right
        next_root.append(root[i].left)
        next_root.append(root[i].right)
        self.connect_list(next_root)
