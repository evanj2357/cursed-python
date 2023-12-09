import random
import sys


def a(x, y, z):
    return x + y + z


def b(x, y, z):
    return x * y * z


def c(x, y, z):
    return -1 * x - y - z


def _shuffle():
    temps = [f.__code__ for f in (a, b, c)]
    random.shuffle(temps)
    for f, code in zip([a, b, c], temps):
        f.__code__ = code


def reshuffle():
    _shuffle()


_shuffle()


if __name__ == '__main__':
    [x, y, z] = [int(sys.argv[i]) for i in range(1, 4)]
    print(f"a(x, y, z) = {a(x, y, z)}")
    print(f"b(x, y, z) = {b(x, y, z)}")
    print(f"c(x, y, z) = {c(x, y, z)}")
