# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{},{}]".format(self.start, self.end)


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        Time: O(n log n) if not sorted else O(n)
        Space: O(n)
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for idx in range(1, len(intervals)):
            prev = res[-1]
            current = intervals[idx]
            if current.start <= prev.end:
                prev.end = max(current.end, prev.end)
            else:
                res.append(current)
        return res


if __name__ == '__main__':
    ip = [Interval(1, 2), Interval(2, 4), Interval(4, 6), Interval(7, 9)]
    print(Solution().merge(ip))
    ip = []
    print(Solution().merge(ip))
