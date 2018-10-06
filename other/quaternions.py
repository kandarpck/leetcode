"""

This is the quaterions.py sample code to get you started.

"""
import math


class quat:
    def __init__(self, *args):
        if len(args) == 4:
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]
            self.d = args[3]
        elif len(args) == 1:
            self.a = args[0]
            self.b = 0
            self.c = 0
            self.d = 0
        else:
            raise ValueError('Wrong number of inputs to constructor.')

    def __str__(self):
        return str(self.a) + "+" + str(self.b) + "i+" + str(self.c) + "j+" + str(self.d) + "k"

    def __add__(self, other):
        if type(other) == quat:
            return quat(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
        else:
            return self + quat(other)

    def __mul__(self, other):
        if type(other) == quat:
            return quat(self.a * other.a, self.a * other.b, self.a * other.c, self.a * other.d)
        else:
            return self * quat(other)

    def __rmul__(self, other):
        if type(other) == quat:
            return quat(self.a * other.a, self.a * other.b, self.a * other.c, self.a * other.d)
        else:
            return self * quat(other)

    def __sub__(self, other):
        if type(other) == quat:
            return quat(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d)
        else:
            return self - quat(other)

    def norm(self):
        e = math.pow(self.a, 2)
        f = math.pow(self.b, 2)
        g = math.pow(self.c, 2)
        h = math.pow(self.d, 2)
        return str(quat(e, f, g, h))

    def inv(self):
        e = 1 / self.a if self.a else 0.0
        f = 1 / self.b if self.b else 0.0
        g = 1 / self.c if self.c else 0.0
        h = 1 / self.d if self.d else 0.0
        return str(quat(e, f, g, h))


if __name__ == '__main__':
    x = quat(5)
    y = quat(0, 4, 0, 0)
    z = quat(1, 1, 1, 1)
    print(x)
    print(x + y)
    print(x - y)
    print(2 * x)
    print(x.inv())
    print(x * y)
    print(x * z)
    print(x.norm())

    ''' Sample output:
    5+0i+0j+0k
    5+4i+0j+0k
    5+-4i+0j+0k
    10+0i+0j+0k
    0.2+0.0i+0.0j+0.0k
    0+20i+0j+0k
    5+5i+5j+5k
    '''
