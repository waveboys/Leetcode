#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/4 下午6:18
#@Author: guangliang
#@File  : solveSudoku.py
"""
解题思路：对于每一个
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
                            if is_validSudoku(board,i,j) and dfs(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True
        dfs(board)




