class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int_list = list(str(x))
        if x > 0:
            res = "".join(reversed(int_list))
        elif x < 0:
            res = "-" + "".join(reversed(int_list[1:]))
        else:
            res = 0
        res = 0 if abs(int(res)) > 0x7FFFFFFF else res
        return int(res)


if __name__ == '__main__':
    sol = Solution()
    ip = -999991
    print(sol.reverse(ip))