"""
>>> parser0.parse_args('2 args.txt'.split())  # doctest: +ELLIPSIS
Namespace(bar=<... name='args.txt' mode='r' encoding='...'>, foo=2)

>>> parser1.parse_args(['out.txt'])  # doctest: +SKIP
Namespace(bar=<... name='out.txt' mode='w' encoding='UTF-8'>)

>>> parser2.parse_args(['9'])
Namespace(foo=9)
>>> parser2.parse_args(['7'])  # doctest: +SKIP
usage: PROG [-h] foo
PROG: error: argument foo: '7' is not a perfect square

>>> parser3.parse_args(['7'])
Namespace(foo=7)
>>> parser3.parse_args(['11'])  # doctest: +SKIP
usage: PROG [-h] {5,6,7,8,9}
PROG: error: argument foo: invalid choice: 11 (choose from 5, 6, 7, 8, 9)
"""

import argparse

import math

parser0 = argparse.ArgumentParser()
parser0.add_argument('foo', type=int)
parser0.add_argument('bar', type=open)

# create file #
###############

parser1 = argparse.ArgumentParser()
parser1.add_argument('bar', type=argparse.FileType('w'))

# custom type conversion #
##########################


def perfect_square(string):
    value = int(string)
    sqrt = math.sqrt(value)
    if sqrt != int(sqrt):
        msg = '%r is not a perfect square' % string
        raise argparse.ArgumentTypeError(msg)
    return value


parser2 = argparse.ArgumentParser(prog='PROG')
parser2.add_argument('foo', type=perfect_square)

# basics choices #
##################

parser3 = argparse.ArgumentParser(prog='PROG')
parser3.add_argument('foo', type=int, choices=range(5, 10))
