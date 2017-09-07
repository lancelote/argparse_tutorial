"""
>>> parser0.add_argument('--foo', help='new foo help')  # doctest: +ELLIPSIS
Traceback (most recent call last):
...
argparse.ArgumentError: argument --foo: conflicting option string: --foo

>>> parser1.print_help()  # doctest: +ELLIPSIS
usage: PROG [-h] [-f FOO] [--foo FOO]
...
optional arguments:
  -h, --help  show this help message and exit
  -f FOO      old foo help
  --foo FOO   new foo help
"""

import argparse

parser0 = argparse.ArgumentParser(prog='PROG')
parser0.add_argument('-f', '--foo', help='old foo help')

parser1 = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
parser1.add_argument('-f', '--foo', help='old foo help')
parser1.add_argument('--foo', help='new foo help')
