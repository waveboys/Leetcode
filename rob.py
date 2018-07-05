# class Solution:
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         if len(nums) == 2:
#             return max(nums[0], nums[1])
#
#         dp = [0 for i in range(len(nums))]
#         dp[0] = nums[0]
#         dp[1]  = nums[1]
#         dp[2] = dp[0] + nums[2]
#         for i in range(3, len(nums)):
#             dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
#
#         return max(dp[-2], dp[-1])


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return sum(nums)

        def rob1(nums):
            cur = 0
            last = 0
            for i in nums:
                temp = cur
                cur = max(last + i, cur)
                last = temp
            return cur

        return max(rob1(nums[:-1]), rob1(nums[1:]))
nums = [2,7,9,6,1,5,1]
print(Solution().rob(nums))
