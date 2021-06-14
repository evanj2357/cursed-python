"""
First-class functions are sooo last week, let's try first-class code!
"""

from typing import Callable, List, Mapping

def function_a(x: int) -> int:
    return x * x - 1

def function_b(x: int) -> int:
    return x * 0

def function_c(y: int) -> int:
    return -1 * y

def rotate_attrs_right(objects: List, attrs: List, get_and_set: Callable) -> List:
    """
    Rotate values of attributes in a list of objects one step to the right.

    :param xs: a list of objects
    :param field_get_and_set: a function that takes an object and a field value, sets
    the field to the given value, and returns the old value
    """
    if len(objects) < 2:
        return List(objects)

    prev = {attr: objects[-1].__getattribute__(attr) for attr in attrs}

    for obj in objects:
        prev = get_and_set(obj, prev)

    return objects

def get_attrs(obj: object, attrs: List) -> Mapping:
    return {attr: obj.__getattribute__(attr) for attr in attrs}

def get_and_set_attrs(obj: object, new_attrs: Mapping) -> Mapping:
    attrs = new_attrs.keys()

    old_data = {attr: obj.__getattribute__(attr) for attr in attrs}

    for attr in attrs:
        obj.__setattr__(attr, new_attrs[attr])

    return old_data


if __name__ == "__main__":
    alphabet_functions = [function_a, function_b, function_c]

    print(list(map(lambda f: f.__call__(5), alphabet_functions)))
    print(function_a(10))

    # note: this intentionally omits the name because I want to leave that
    # set to the original value
    attrs = ["__doc__", "__code__", "__defaults__", "__kwdefaults__", "__annotations__"]

    print(list(map(lambda f: f.__call__(5), rotate_attrs_right(alphabet_functions, attrs, get_and_set_attrs))))
    print(function_a(10))