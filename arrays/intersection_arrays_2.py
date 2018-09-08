from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        """
        Not valid. Needs to find all repeating elements

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))

    def intersect_counter(self, nums1, nums2):
        """
        Time:

        :param nums1:
        :param nums2:
        :return:
        """
        nums1_counter = Counter(nums1)
        result = []

        for number in nums2:
            if nums1_counter[number] > 0:
                result.append(number)
                nums1_counter[number] -= 1
        return result


if __name__ == '__main__':
    sol = Solution()
    ip = [1, 2, 9, 3, 4, 8, 444, 2]
    ip2 = [2, 2, 3]
    print(sol.intersect(ip, ip2))
    print(sol.intersect_counter(ip, ip2))
