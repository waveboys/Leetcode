# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return root.val

        queue = []
        nums = []
        nums.append(root.val)
        if root.left != None:
            queue.append(root.left)
        if root.right != None:
            queue.append(root.right)

        while len(queue) != 0:
            s = 0
            ll = []
            for node in queue:
                s += node.val
                if node.left != None:
                    ll.append(node.left)
                if node.right != None:
                    ll.append(node.right)

            queue = ll.copy()
            nums.append(s)

        def rob1(nums):
            cur = 0
            last = 0
            for i in nums:
                temp = cur
                cur = max(last + i, cur)
                last = temp
            return cur

        return rob1(nums)