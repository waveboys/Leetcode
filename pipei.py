class Solution(object):
    def parseExpression(self, p):
        els = []
        i = 0
        while i < len(p):
            if p[i] == '.' or (ord('a') <= ord(p[i]) <= ord('z')):
                if i + 1 < len(p) and p[i + 1] == '*':
                    els.append((p[i], '*'))
                    i += 2
                else:
                    els.append((p[i], None))
                    i += 1
            else:
                print("improper pattern at %d: %s" % (i, p))
                raise ValueError
        return els

    def isMatch(self, s, p):
        path = self.parseExpression(p)
        seen = set()
        st = [(0, 0)]
        while st:
            i, j = st.pop()
            if j == len(path):
                if i == len(s):
                    return True
            else:
                c, q = path[j]
                if q == None:
                    if i < len(s) and (c == '.' or c == s[i]):
                        if (i + 1, j + 1) not in seen:
                            st.append((i + 1, j + 1))
                            seen.add((i + 1, j + 1))
                else:
                    if (i, j + 1) not in seen:
                        st.append((i, j + 1))
                        seen.add((i, j + 1))
                    while i < len(s) and (c == '.' or s[i] == c):
                        if (i + 1, j + 1) not in seen:
                            st.append((i + 1, j + 1))
                            seen.add((i + 1, j + 1))
                        i += 1
        return False