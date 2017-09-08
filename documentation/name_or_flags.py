"""
>>> parser.parse_args(['BAR'])
Namespace(bar='BAR', foo=None)

>>> parser.parse_args(['BAR', '--foo', 'FOO'])
Namespace(bar='BAR', foo='FOO')

>>> parser.parse_args(['--foo', 'FOO'])  # doctest: +SKIP
usage: PROG [-h] [-f FOO] bar
PROG: error: too few arguments
"""

import argparse

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-f', '--foo')
parser.add_argument('bar')
