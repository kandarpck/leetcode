class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = int(''.join(str(e) for e in digits))
        number += 1
        res = []
        for num in str(number):
            res.append(int(num))
        return res


if __name__ == '__main__':
    sol = Solution()
    ip = [9, 9, 9, 9, 9, 9, 9, 9, 9]
    print(sol.plusOne(ip))
