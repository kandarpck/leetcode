import itertools


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        Time:  O(n * 2^n)
        Space: O(2^n)
        """
        seq = "1"
        for i in range(n - 1):
            seq = self.getNext(seq)
        return seq

    def getNext(self, seq):
        i, next_seq = 0, ""
        while i < len(seq):
            cnt = 1
            while i < len(seq) - 1 and seq[i] == seq[i + 1]:
                cnt += 1
                i += 1
            next_seq += str(cnt) + seq[i]
            i += 1
        return next_seq


class Solution2():
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))
        return s


if __name__ == '__main__':
    print(Solution().countAndSay(4))
    print(Solution2().countAndSay(6))
