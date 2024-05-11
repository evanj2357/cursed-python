import random
import sys


def a(x, y, z):
    return x + y + z


def b(x, y, z):
    return x * y * z


def c(x, y, z):
    return -1 * x - y - z


def shuffle(*args):
    temps = [f.__code__ for f in args]
    random.shuffle(temps)
    for f, code in zip(args, temps):
        f.__code__ = code


if __name__ == '__main__':
    shuffle(a, b, c)
    [x, y, z] = [int(sys.argv[i]) for i in range(1, 4)]
    print(f"a(x, y, z) = {a(x, y, z)}")
    print(f"b(x, y, z) = {b(x, y, z)}")
    print(f"c(x, y, z) = {c(x, y, z)}")
