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


def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    number_dict = {'0':'', '1': '', '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'],\
                   '6':['m', 'n', 'o'], '7':['p', 'q', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
    len_dit = len(digits)
    if len_dit == 0:
        return None

    count = 0

def ditgits_to_str(digits, count, number_dict, len_dit, result, s):
    if len_dit == count:
        result.append(s)
        return
    else:
        for i in digits:
            s += number_dict[]