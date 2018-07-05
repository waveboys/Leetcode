# -*- coding: utf-8 -*-
'''
题目：
    Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

    For example, given the following triangle
    [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
    ]
    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
解题思路：从底向上采用动态规划的思想，从倒数第二行开始，每一列都是取它下一层邻居的最小值，不断向上迭代到第一层
'''
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if len(triangle[0])==0:
            return

        for i in range(n-2,-1,-1):
            for j, num in enumerate(triangle[i]):
                triangle[i][j] = num + min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

print(Solution().minimumTotal([[]]))