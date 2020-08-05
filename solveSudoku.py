#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/4 下午6:18
#@Author: guangliang
#@File  : solveSudoku.py
"""
解题思路：对于每一个要进行填充的数字，遍历每一个数字然后看是否满足数独的条件。
1、对于每个等待填充的数字，要看它所在的行、列与三角形结构数组里是否满足数独的条件
2、对于每个等待填充的数字，还要回溯下后面等待填充的是否满足数独的条件
"""
class Solution:
    def solveSudoku(self,board:list)->None:
        def is_validSudoku(board,x,y):
            temp = board[x][y]
            board[x][y] = "D"
            for i in range(9):
                if board[i][y] == temp:
                    return False
            for j in range(9):
                if board[x][y] == temp:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[int(x/3)*3+i][int(y/3)*3+j] == temp:
                        return False
            board[x][y] = temp
            return True
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in "123456789":
                            board[i][j] = num
                            # dfs 回溯后面等待填充的是否能满足数独条件
                            if is_validSudoku(board,i,j) and dfs(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True
        dfs(board)




