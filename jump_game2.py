import numpy as np
# class Solution:
#     def jump(self, nums:list) -> int:
#         # for i in range(nums):
#         def jump_digui(nums,n):
#             jump = np.inf
#             if n==len(nums)-1:
#                 return 0
#             nn = nums[n]
#             for i in range(1,nn+1):
#                 if n+i >= len(nums):
#                     break
#                 temp_jump = jump_digui(nums,n+i)
#                 if temp_jump < jump:
#                     jump = temp_jump
#             return jump + 1
#         if len(nums) < 1:
#             return None
#         if len(nums) == 1:
#             return 0
#         jums = jump_digui(nums,0)
# #         return jums
# class Solution:
#     def jump(self, nums):
#         result = reach = maxReach = 0
#         for index, num in enumerate(nums):
#             if index > reach:
#                 reach = maxReach
#                 result += 1
#             maxReach = max(maxReach, index + num)
#         return result
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        N = len(nums)
        count = 0
        pos = 0
        while cur < N - 1:
            count += 1
            pre = cur
            while pos <= pre:
                cur = max(cur, pos + nums[pos])
                pos += 1
        return count

print(Solution().jump([2,9,1,1,4]))



