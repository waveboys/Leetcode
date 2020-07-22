#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/22 上午11:30
#@Author: guangliang
#@File  : isValidSudoku.py
"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""

"""
解题思路：关键是对于每个出现的数字，怎么标识已经出现过
1、使用3个二维数组，rows、cols、boxs分别用来存储行、列、子九宫格的情况
2、其中一维下标 n 对于3个二维数组分别表示：第 n 行，第 n 列，第 n 个子九宫格
3、其中二维下标 m 对于3个二维数组分别表示：在当前行、列、子九宫格的数字m
4、二维数组中的值则表示：该数字出现的次数（在本题中次数超过 1 次即代表重复）
举例：rows[2][5] = 1，第 2 行中数字 5 出现了 1 次
"""
class Solution:
    def isValidSudoku(self, board: list) -> bool:
        rowFlag = [[0 for i in range(9)] for j in range(9)]
        lineFlag = [[0 for i in range(9)] for j in range(9)]
        boxesFlag = [[0 for i in range(9)] for j in range(9)]
        for i in range(9):
            row = []
            line = []
            box = []
            for j in range(9):
                row.append(0)
                line.append(0)
                box.append(0)
            rowFlag.append(row)
            lineFlag.append(line)
            boxesFlag.append(box)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j]) - 1
                k = i//3*3+j//3
                if rowFlag[i][num] or lineFlag[j][num] or boxesFlag[k][num]:
                    return False
                rowFlag[i][num] = 1
                lineFlag[j][num] = 1
                boxesFlag[k][num] = 1
        return True
a = [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(a))

