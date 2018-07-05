# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        gen = self._generateTrees(list(range(1, n+1)))

    def _generateTrees(self, nums):

        if not nums:
            yield None

        for i in range(len(nums)):
            for left in self._generateTrees(nums[:i]):
                for right in self._generateTrees(nums[i+1:]):
                    root = TreeNode(nums[i])
                    root.left = left
                    root.right = right
                    yield root

    def numTrees(self, n):
        res = [0 for i in range(n+1)]
        res[0] = 1
        res[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                res[i] += res[j]*res[i-1-j]

        return res[n]


    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = root.left
        right = root.right
        return max(self.maxDepth(left)+1, self.maxDepth(right)+1)

    def minDepth(self, root):
        ans = float('inf')
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node:
                if not node.left and not node.right:
                    ans = min(ans, depth)
                stack.extend([(node.left, depth + 1), (node.right, depth + 1)])
        return ans if root else 0

n=3
print(Solution().numTrees(n))