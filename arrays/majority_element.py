from collections import Counter


class Solution:
    
    def majorityElement(self, nums):
        """
        Time: N
        Space: N
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        nums_count = Counter(nums)
        for num, count in nums_count.items():
            if count > len(nums) / 3:
                res.append(num)
        return res


    def majorityElement2(self, nums):
        """
        Time: N
        Space: 1
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]


if __name__ == '__main__':
    sol = Solution()
    ip = [1, 1, 4, 4, 2, 2, 2, 1]
    print(sol.majorityElement(ip))
    print(sol.majorityElement2(ip))
