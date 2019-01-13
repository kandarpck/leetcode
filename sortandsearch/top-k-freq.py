from collections import Counter


class Solution(object):
    # one pass dutch partitioning problem
    # Time: O(nlogk)
    # Space: O(n)
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_counter = Counter(nums)
        return [val for val, _ in nums_counter.most_common(k)]


if __name__ == '__main__':
    nums = [0, 2, 2, 0, 1, 0, 2, 1]
    print(Solution().topKFrequent(nums, k=2))
