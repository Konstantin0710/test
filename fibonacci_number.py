"""Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... .
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms."""


def gen_fib(arg):
    """Fibonacci number generator"""
    first_number = 0
    second_number = 1
    while first_number < arg:
        yield first_number
        first_number, second_number = second_number, first_number + second_number


def sum_fib(arg):
    """sum of even numbers"""
    return sum(i for i in gen_fib(arg) if i % 2 == 0)


print(sum_fib(4000000))
assert sum_fib(10) == 10
assert sum_fib(100) == 44
