"""
>>> # no negative number options, -1 is a positional argument
>>> parser0.parse_args('-x -1'.split())
Namespace(foo=None, x='-1')

>>> # no negative number options, -1 and -5 are positional arguments
>>> parser0.parse_args('-x -1 -5'.split())
Namespace(foo='-5', x='-1')

>>> # negative number options, -1 is an option
>>> parser1.parse_args('-1 X'.split())
Namespace(foo=None, one='X')

>>> # negative number options, -2 is an option
>>> parser1.parse_args(['-2'])  # doctest: +SKIP
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: no such option: -2

>>> # negative number options, both -1s are options
>>> parser1.parse_args('-1 -1'.split())  # doctest: +SKIP
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: argument -1: expected one argument

>>> # positional argument starting with dash
>>> parser1.parse_args('-- -f'.split())
Namespace(foo='-f', one=None)
"""

import argparse

parser0 = argparse.ArgumentParser(prog='PROG')
parser0.add_argument('-x')
parser0.add_argument('foo', nargs='?')

parser1 = argparse.ArgumentParser(prog='PROG')
parser1.add_argument('-1', dest='one')
parser1.add_argument('foo', nargs='?')
