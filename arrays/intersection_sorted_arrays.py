# intersection of two sorted arrays of integers
# example:
# A:   (1, 3, 3, 6, 7, 9, 10)
# B:   (2, 3, 3, 4, 9, 15)
#
# answer: (3, 3, 9)


class Solution(object):
    def intersection_sorted_arrays(self, A, B):
        """
        A, B: sorted input arrays
        rtype: List
        Time: O(max(a, b))
        Space: 1
        """
        i, j = 0, 0
        result = []
        if not (A or B):
            return result
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                i += 1
            elif B[j] < A[i]:
                j += 1
            else:
                result.append(A[i])
                i += 1
                j += 1
        return result
