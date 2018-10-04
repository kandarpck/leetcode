from collections import Counter


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        nums_count = Counter(nums)
        for num, count in nums_count.items():
            if count > len(nums) / 3:
                res.append(num)
        return res


if __name__ == '__main__':
    sol = Solution()
    ip = [1, 1, 4, 4, 2, 2, 2, 1]
    print(sol.majorityElement(ip))
    print(sol.majorityElement(ip))
