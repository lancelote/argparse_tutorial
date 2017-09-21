"""
>>> parser0.print_help()  # doctest: +ELLIPSIS
usage: frobble [-h] [--foo] bar [bar ...]
...
positional arguments:
  bar         one of the bars to be frobbled
...
optional arguments:
  -h, --help  show this help message and exit
  --foo       foo the bars before frobbling

>>> parser1.print_help()  # doctest: +ELLIPSIS
usage: frobble [-h] [bar]
...
positional arguments:
  bar         the bar to frobble (default: 42)
...
optional arguments:
  -h, --help  show this help message and exit

>>> parser2.print_help()  # doctest: +ELLIPSIS
usage: frobble [-h]
...
optional arguments:
  -h, --help  show this help message and exit
"""

import argparse

# simple usage #
################

parser0 = argparse.ArgumentParser(prog='frobble')
parser0.add_argument('--foo', action='store_true',
                     help='foo the bars before frobbling')
parser0.add_argument('bar', nargs='+',
                     help='one of the bars to be frobbled')

# format specifiers #
#####################

parser1 = argparse.ArgumentParser(prog='frobble')
parser1.add_argument('bar', nargs='?', type=int, default=42,
                     help='the bar to %(prog)s (default: %(default)s)')


# silence help #
################

parser2 = argparse.ArgumentParser(prog='frobble')
parser2.add_argument('--foo', help=argparse.SUPPRESS)
