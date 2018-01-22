class Solution(object):
    def is_same_tree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is not None:
            if q is not None:
                if p.val != q.val:
                    return False
                if self.is_same_tree(p.left, q.left):
                    return self.is_same_tree(p.right, q.right)
                else:
                    return False
            else:
                return False
        else:
            if q is not None:
                return False
            else:
                return True
