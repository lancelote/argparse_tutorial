"""
>>> parser0.print_help()  # doctest: +ELLIPSIS
usage: PROG [-h] [--foo FOO]
...
optional arguments:
  -h, --help  show this help message and exit
  --foo FOO   foo help

>>> parser1.print_help()  # doctest: +ELLIPSIS
usage: PROG [--foo FOO]
...
optional arguments:
  --foo FOO  foo help

>>> parser2.print_help()  # doctest: +ELLIPSIS
usage: PROG [+h]
...
optional arguments:
  +h, ++help  show this help message and exit
"""

import argparse

# standard way #
################

parser0 = argparse.ArgumentParser(prog='PROG')
parser0.add_argument('--foo', help='foo help')

# do not show the help #
########################

parser1 = argparse.ArgumentParser(prog='PROG', add_help=False)
parser1.add_argument('--foo', help='foo help')

# change help prefix #
######################

parser2 = argparse.ArgumentParser(prog='PROG', prefix_chars='+/')
