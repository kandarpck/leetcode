# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{},{}]".format(self.start, self.end)


class Solution(object):
    def open_ratio(self, open_times, query_time):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        Time:  O(n)
        Space: O(1)
        """
        accrued_time = 0.0
        if not open_times or not query_time:
            return accrued_time
        for r_time in open_times:
            if query_time.start <= r_time.start <= query_time.end <= r_time.end:
                accrued_time += query_time.end - r_time.start
            elif query_time.start <= r_time.start <= r_time.end <= query_time.end:
                accrued_time += r_time.end - r_time.start
            elif r_time.start <= query_time.start <= query_time.end <= r_time.end:
                accrued_time += query_time.end - query_time.start
            elif r_time.start <= query_time.start <= r_time.end <= query_time.end:
                accrued_time += r_time.end - query_time.start
        return accrued_time / (query_time.end - query_time.start)


class Solution2(object):
    def sort_ratings(self, ratings):
        ratings = [line.split(' ') for line in ratings.split('\n')]
        return sorted(ratings, key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    ip1 = [Interval(0, 24)]
    q1 = Interval(4, 10)
    print(Solution().open_ratio(ip1, q1))
    ip2 = [Interval(4, 10), Interval(13, 16)]
    q2 = Interval(0, 24)
    print(Solution().open_ratio(ip2, q2))
    ip3 = [Interval(7, 10), Interval(11, 15)]
    q3 = Interval(9, 12)
    print(Solution().open_ratio(ip3, q3))

    print(Solution2().sort_ratings("1005 2\n1001 5\n1002 5\n1004 1"))
