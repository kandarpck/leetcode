from collections import Counter


class Solution(object):

    def singleNumber(self, nums):
        """
        Time N^2
        Space 1
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            duplicate = False
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    duplicate = True
            if not duplicate:
                return nums[i]

    def singleNumberCounter(self, nums):
        """
        Time N
        Space 1
        :type nums: List[int]
        :rtype: int
        """
        num_counter = Counter(nums)
        return num_counter.most_common()[:-2:-1][0][0]

    def singleNumberDuplicates(self, nums):
        """
        Time N
        Space N
        :return:
        """
        duplicates = []
        for number in nums:
            if number not in duplicates:
                duplicates.append(number)
            else:
                duplicates.remove(number)
        return duplicates.pop()

    def singleNumberMath(self, nums):
        """
        Time: N
        Space: N

        :return:
        """
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumberXOR(self, nums):
        """
        Time: N
        Space: 1
        :param nums:
        :return:
        """
        result = 0
        for number in nums:
            result ^= number
        return result


if __name__ == '__main__':
    sol = Solution()
    ip = [1, 1, 9, 3, 4, 2, 9, 2, 4]
    print(sol.singleNumber(ip))
    print(sol.singleNumberCounter(ip))
    print(sol.singleNumberDuplicates(ip))
    print(sol.singleNumberMath(ip))
    print(sol.singleNumberXOR(ip))
