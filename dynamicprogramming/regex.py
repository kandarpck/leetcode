class SolutionRecursive:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        if len(p) == 1 or p[1] != "*":
            if len(s) and (p[0] == s[0] or p[0] == "."):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) and (p[0] == s[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])


class SolutionDP(object):
    def isMatch(self, s, p):
        pass


if __name__ == '__main__':
    assert SolutionRecursive().isMatch("aa", "a") is False
    assert SolutionRecursive().isMatch("baa", ".*a*") is True
    s = 'aa'
    p = 'aa'
    result = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
    print(result)