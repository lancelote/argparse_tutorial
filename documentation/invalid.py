"""
>>> # invalid type
>>> parser.parse_args('--foo spam'.split())  # doctest: +SKIP
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: argument --foo: invalid int value: 'spam'

>>> # invalid option
>>> parser.parse_args(['--bar'])  # doctest: +SKIP
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: no such option: --bar

>>> # wrong number of arguments
>>> parser.parse_args('spam badger'.split())  # doctest: +SKIP
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: extra arguments found: badger
"""

import argparse

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', type=int)
parser.add_argument('bar', nargs='?')
