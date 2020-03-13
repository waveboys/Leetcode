#Letter Combinations of a Phone Number
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does
not map to any letters.
Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

"""
1、先把前面的元素一个一个组合完，然后再依次和后面的每一个元素进行组合
"""
class Solution:
    def letterCombinations(self, digits: str) -> list:
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits)==0:
            return []
        for i in range(len(digits)):
            res = []
            if i == 0:
                for k in dic[digits[i]]:
                    res.append(k)
            else:
                for j ,_ in enumerate(tmp):
                    for k in dic[digits[i]]:

                        res.append(tmp[j]+k)
            tmp = res
        return res
print(Solution().letterCombinations("23"))