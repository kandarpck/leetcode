from statistics import median


class Solution(object):
    def median_rating(self, businesses):
        ratings = []
        for business in businesses:
            ratings.append(business['rating'])
        print(median(ratings))
        ratings.sort()
        if len(ratings) < 1:
            return None
        elif len(ratings) % 2 == 0:
            return (ratings[len(ratings) // 2 - 1] + ratings[(len(ratings) // 2)]) / 2.0
        else:
            return ratings[len(ratings) // 2]


if __name__ == '__main__':
    bus_ratings = [

        {'id': 101, 'rating': 5.0},
        {'id': 102, 'rating': 2.0},
        {'id': 103, 'rating': 5.0},
        {'id': 104, 'rating': 1.0},
        {'id': 105, 'rating': 5.0},
        {'id': 106, 'rating': 3.0}

    ]
    print(Solution().median_rating(bus_ratings))
