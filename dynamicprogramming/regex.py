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


if __name__ == '__main__':
    assert SolutionRecursive().isMatch("aa", "a") is False
    assert SolutionRecursive().isMatch("aa", "aa") is True
