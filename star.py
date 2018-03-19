import torch
import numpy as np

def multiply(*args):
    print(type(args))
    total = 1
    for arg in args:
        total *= arg
    return total

r = multiply(2, 3, 4, 5)
print('r = %d\n' %r)


def accept(**kwargs):
    for kw, val in kwargs.items():
        print('%s => %r' %(kw, val))

accept(foo='bar', spam='eggs')

class Test(object):
    def __init__(self, value='hello, world!'):
        self.data = value

t = Test()
print(t)

class TestRepr(Test):
    def __repr__(self):
        return 'TestRepr(%s)' %self.data

tr = TestRepr()
print(tr)
