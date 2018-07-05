import math
def uniquePathWithObstacles(obstacleGrid):

    m = len(obstacleGrid)
    n = len(obstacleGrid[:][0])
    res = [[0 for i in range(n)] for j in range(m)]
    if obstacleGrid[0][0] == 1 or obstacleGrid == None:
        return 0

    for i in range(m):
        if obstacleGrid[i][0] == 0:
            res[i][0] = 1
        else:
            break

    for j in range(n):
        if obstacleGrid[0][j] == 0:
            res[0][j] = 1
        else:
            break

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                res[i][j] = res[i-1][j] + res[i][j-1]


    return res[-1][-1]

def paths(m,n):

    res = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            if i-1 <0 or j-1<0:
                res[i][j] = 1
            else:
                res[i][j] = res[i-1][j] + res[i][j-1]


    return res[-1][-1]


def miniPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    res = [[0 for i in range(n)] for j in range(m)]
    res[0][0] = grid[0][0]
    for i in range(1, m):
        res[i][0] = res[i-1][0] + grid[i][0]
    for j in range(1, n):
        res[0][j] = res[0][j-1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
           res[i][j] = min(res[i-1][j] + grid[i][j], res[i][j-1]+grid[i][j])

    return res[-1][-1]


def calculateMinimumHP(dungeon):
   m = len(dungeon)
   n = len(dungeon[0])
   res = [[0 for i in range(n)] for j in range(m)]
   health = [[0 for i in range(n)] for j in range(m)]
   if dungeon[0][0] <= 0:
       res[0][0] = abs(dungeon[0][0]) + 1
       health[0][0] = 1
   else:
       res[0][0] = 1
       health[0][0] = dungeon[0][0] + 1
   for i in range(1, m):
       if dungeon[i][0]+health[i-1][0] <= 0:
           res[i][0] = res[i-1][0] + abs(dungeon[i][0] + health[i-1][0]) + 1
           health[i][0] = 1
       else:
           res[i][0] = res[i - 1][0]
           health[i][0] = dungeon[i][0]+health[i-1][0]

   for j in range(1,n):
       if dungeon[0][j] + health[0][j-1] <= 0:
           res[0][j] = res[0][j-1] + abs(dungeon[0][j] + health[0][j-1]) + 1
           health[0][j] = 1
       else:
           res[0][j] = res[0][j - 1]
           health[0][j] = dungeon[0][j] + health[0][j-1]

   for i in range(1, m):
       for j in range(1, n):
           if health[i-1][j] + dungeon[i][j] <= 0:
               a1 = res[i-1][j] + abs(health[i-1][j] + dungeon[i][j]) + 1
               b1 = 1
           else:
               a1 = res[i - 1][j]
               b1 = health[i - 1][j] + dungeon[i][j]
           if health[i][j-1] + dungeon[i][j] <= 0:
               a2 = res[i][j-1] + abs(health[i][j-1] + dungeon[i][j]) + 1
               b2 = 1
           else:
               a2 = res[i][j-1]
               b2 = health[i][j-1] + dungeon[i][j]
           if a1 > a2:
               res[i][j] = a2
               health[i][j] = b2
           else:
               res[i][j] = a1
               health[i][j] = b1

   print(res)
   print(health)
   return res[-1][-1]


def calculateMinimumHP1(dungeon):
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    m, n = len(dungeon), len(dungeon[0])
    hps = [[0 for j in range(n)] for i in range(m)]
    hps[-1][-1] = max(1 - dungeon[-1][-1], 1)
    for i in range(m - 2, -1, -1):
        hps[i][-1] = max(hps[i + 1][-1] - dungeon[i][-1], 1)
    for j in range(n - 2, -1, -1):
        hps[-1][j] = max(hps[-1][j + 1] - dungeon[-1][j],  1)
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            hps[i][j] = max(min(hps[i + 1][j], hps[i][j + 1]) - dungeon[i][j], 1)
    print(hps)
    return hps[0][0]

def cherryPickup(grid):
    m, n = len(grid), len(grid[0])
    res = [[0 for i in range(n)] for j in range(m)]
    
# print(miniPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
dungeon = [[-2, -3, 3],[-5, -10, 1], [10, 30, -5]]
print(calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]))
print(calculateMinimumHP1([[1,-3,3],[0,-2,0],[-3,-3,-3]]))