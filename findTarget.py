#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/9/12 下午11:18
#@Author: guangliang
#@File  : findTarget.py
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        vals = []
        def inOrderTraverse(node,vals):
            if node is None:
                return None
            inOrderTraverse(node.left,vals)
            vals.append(node.val)
            inOrderTraverse(node.right,vals)

        inOrderTraverse(root,vals)
        d = {}
        for i in range(len(vals)):
            if (k - vals[i]) in d:
                return True
            d[vals[i]] = i
        return False
root = TreeNode(5)
left1 = TreeNode(3)
right1 = TreeNode(6)
root.left = left1
root.right = right1
left2 = TreeNode(2)
right2 = TreeNode(4)
right3 = TreeNode(7)
left1.left = left2
left1.right = right2
right1.right = right3
print(Solution().findTarget(root,28))








