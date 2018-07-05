# -*- coding: utf-8 -*-
# bin()函数是把一个整数转化为它的二进制形式，通过比较时钟和分钟转化为二进制，然后比较二进制数里1的个数是否与num相同
# %02d使用0作为占位符，如果整数不够2位的话，使用0作为填充
class solution:
    def readBinaryWatch(self, num):
        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]


def letterCasePermutation(S):
    """
    :type S: str
    :rtype: List[str]
    """
    str = []
    for i in S:
        if i.isalpha():
            str.append([i.lower(), i.isalpha()])
        else:
            str.append([i])

print(solution().readBinaryWatch(2))