import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if re.match('^\s*(\+|-)?(\d+|\d*\.\d+|\d+\.\d*|\d+\.?\d*e[\+|-]?\d+|\d*\.?\d+e[\+|-]?\d+)\s*$',s):
            return True
        else:
            return False