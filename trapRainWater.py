#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/11 下午12:16
#@Author: guangliang
#@File  : trapRainWater.py
"""

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map,
compute the volume of water it is able to trap after raining.
Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
"""
class Solution:
    def trapRainWater(self, heightMap):
        m = len(heightMap)
        n = len(heightMap[0]) if m else 0

        peakMap = [[0x7FFFFFFF] * n for _ in range(m)]

        q = []

        for x in range(m):
            for y in range(n):
                if x in (0, m - 1) or y in (0, n - 1):
                    peakMap[x][y] = heightMap[x][y]
                    q.append((x, y))
        print(q)
        print(peakMap)

        while q:
            x, y = q.pop(0)
            for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                nx, ny = x + dx, y + dy
                if nx <= 0 or nx >= m - 1 or ny <= 0 or ny >= n - 1:
                    continue
                limit = max(peakMap[x][y], heightMap[nx][ny])
                if peakMap[nx][ny] > limit:
                    peakMap[nx][ny] = limit
                    q.append((nx, ny))

        return sum(peakMap[x][y] - heightMap[x][y] for x in range(m) for y in range(n))
print(Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))