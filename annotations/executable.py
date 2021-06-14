"""
Type annotations are executed as code!

They also aren't used by the interpreter, except to populate the
`__annotations__` attribute.
"""

import inspect

X: int = 5

# code re-use isn't always a good idea ;)
def foo(x: __annotations__["X"]) -> __annotations__["X"]:
    return 2 * x

if __name__ == "__main__":
    # The module has annotations:
    print(__annotations__)

    # They're mutable!
    __annotations__["X"] = X
    print(__annotations__)

    # The function annotations have the original value from `__annotations__["X"]`
    # because they were evaluated when the function definition was first read:
    print(foo.__annotations__)