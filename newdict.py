"""Implement a function with two arguments,
both are lists of possibly different length.
The function must return dictionary with keys from the first list
and corresponding values from the second.
If a key lacks value, resulting dictionary must contain None for that key (or null for JavaScript).
Redundant values must be ignored. Keys are guaranteed to be unique."""


def create_dict(list1, list2):
    """return dict"""
    return {j: gen_value(i, list2) for i, j in enumerate(list1)}


def gen_value(i, list2):
    """return value dict or None"""
    if i < len(list2):
        return list2[i]
    return None


assert create_dict([1, 2], [11, 22, 33]) == {1: 11, 2: 22}
assert create_dict([1, 2, 3], [11, 22, 33]) == {1: 11, 2: 22, 3: 33}
assert create_dict([1, 2, 3, 4], [11, 22, 33]) == {1: 11, 2: 22, 3: 33, 4: None}
