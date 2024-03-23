from functools import wraps


# for convenience
Return = '_return_'
_ = None


def If(condition, block, Else = None):
    '''Note: block and else_block need to be callables to
    ensure correct condition execution'''
    if condition:
        # blocks don't return values in Python
        block()
    else:
        Else()


def brackets(f):
    '''make "Return" work like it should'''
    @wraps(f)
    def _f(*args, **kwargs):
        return f(*args, **kwargs)[Return]
    
    return _f


@brackets
def bracket_test(n): return {
    (x := 1 + n):  # can't actually use semicolons here, but
    (y := 3 * x),  # mean(':', ',') is totally ';' so close enough
    print(x):
    If(n > 4, lambda: {
        # an equal number of alternating ':' and ',' is
        # unfortunately required before the Return
        print("n is", n): _,
    }, Else = lambda: {
        print("n was not more than 4!"): _,
    }),

    print(x + y):
    print(x - y),
    Return: (x, y),
}


if __name__ == '__main__':
    print(bracket_test(5))

    print("-------------")

    print(bracket_test(3))
