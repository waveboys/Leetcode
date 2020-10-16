#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 9:54 下午
# @Author  : lambert
# @Site    : 
# @File    : rotate.py
# @Software: PyCharm
"""
思路：
先对角线进行转换
再反向旋转
"""
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(0, len(matrix)):
            matrix[i] = list(reversed(matrix[i]))
        print(matrix)
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)

