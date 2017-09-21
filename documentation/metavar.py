"""
>>> parser0.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
>>> parser0.print_help()  # doctest: +ELLIPSIS
usage: PROG [-h] [--foo FOO] bar
...
positional arguments:
  bar
...
optional arguments:
  -h, --help  show this help message and exit
  --foo FOO

>>> parser1.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
>>> parser1.print_help()  # doctest: +ELLIPSIS
usage: PROG [-h] [--foo YYY] XXX
...
positional arguments:
  XXX
...
optional arguments:
  -h, --help  show this help message and exit
  --foo YYY

>>> parser2.print_help()  # doctest: +ELLIPSIS
usage: PROG [-h] [-x X X] [--foo bar baz]
...
optional arguments:
  -h, --help     show this help message and exit
  -x X X
  --foo bar baz
"""

import argparse

# default behavior #
####################

parser0 = argparse.ArgumentParser(prog='PROG')
parser0.add_argument('--foo')
parser0.add_argument('bar')

# specifying through metavar #
##############################

parser1 = argparse.ArgumentParser(prog='PROG')
parser1.add_argument('--foo', metavar='YYY')
parser1.add_argument('bar', metavar='XXX')

# different metavar for nargs #
###############################

parser2 = argparse.ArgumentParser(prog='PROG')
parser2.add_argument('-x', nargs=2)
parser2.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))
