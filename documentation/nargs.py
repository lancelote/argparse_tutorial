"""
>>> parser0.parse_args('c --foo a b'.split())
Namespace(bar=['c'], foo=['a', 'b'])

>>> parser1.parse_args('XX --foo YY'.split())
Namespace(bar='XX', foo='YY')
>>> parser1.parse_args('XX --foo'.split())
Namespace(bar='XX', foo='c')
>>> parser1.parse_args([])
Namespace(bar='d', foo='d')

>>> parser2.parse_args(['input.txt', 'output.txt'])  # doctest: +SKIP
Namespace(infile=<_io.TextIOWrapper name='input.txt' encoding='UTF-8'>,
          outfile=<_io.TextIOWrapper name='output.txt' encoding='UTF-8'>)
>>> parser2.parse_args([])  # doctest: +SKIP
Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>,
          outfile=<_io.TextIOWrapper name='<stdout>' encoding='UTF-8'>)

>>> parser3.parse_args('a b --foo x y --bar 1 2'.split())
Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])

>>> parser4.parse_args('a b'.split())
Namespace(foo=['a', 'b'])
>>> parser4.parse_args([])  # doctest: +SKIP
usage: PROG [-h] foo [foo ...]
PROG: error: too few arguments

>>> parser5.parse_args('--foo B cmd --arg1 XX ZZ'.split())
Namespace(args=['--arg1', 'XX', 'ZZ'], command='cmd', foo='B')
"""

import argparse
import sys

# multiple arguments #
######################

parser0 = argparse.ArgumentParser()
parser0.add_argument('--foo', nargs=2)
parser0.add_argument('bar', nargs=1)

# one argument #
################

parser1 = argparse.ArgumentParser()
parser1.add_argument('--foo', nargs='?', const='c', default='d')
parser1.add_argument('bar', nargs='?', default='d')

# optional input and output files #
###################################

parser2 = argparse.ArgumentParser()
parser2.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                     default=sys.stdin)
parser2.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                     default=sys.stdout)

# all arguments #
#################

parser3 = argparse.ArgumentParser()
parser3.add_argument('--foo', nargs='*')
parser3.add_argument('--bar', nargs='*')
parser3.add_argument('baz', nargs='*')

# one or more arguments #
#########################

parser4 = argparse.ArgumentParser(prog='PROG')
parser4.add_argument('foo', nargs='+')

# all remaining arguments #
###########################

parser5 = argparse.ArgumentParser()
parser5.add_argument('--foo')
parser5.add_argument('command')
parser5.add_argument('args', nargs=argparse.REMAINDER)
