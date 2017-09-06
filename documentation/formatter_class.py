"""
>>> parser0.print_help()  # doctest: +ELLIPSIS
usage: PROG [-h]
...
this description was indented weird but that is okay
...
optional arguments:
  -h, --help  show this help message and exit
...
likewise for this epilog whose whitespace will be cleaned up and whose words
will be wrapped across a couple lines

>>> parser1.print_help()  # doctest: +ELLIPSIS
usage: PROG [-h]
...
Please do not mess up this text!
--------------------------------
    I have indented it
    exactly the way
    I want it
...
optional arguments:
  -h, --help  show this help message and exit

>>> parser2.print_help()  # doctest: +ELLIPSIS
usage: PROG [-h] [--foo FOO] [bar [bar ...]]
...
positional arguments:
  bar         BAR! (default: [1, 2, 3])
...
optional arguments:
  -h, --help  show this help message and exit
  --foo FOO   FOO! (default: 42)

>>> parser3.print_help()  # doctest: +ELLIPSIS
usage: PROG [-h] [--foo int] float
...
positional arguments:
  float
...
optional arguments:
  -h, --help  show this help message and exit
  --foo int
"""

import argparse
import textwrap

# remove whitespaces #
######################

parser0 = argparse.ArgumentParser(
    prog='PROG',
    description='''this description
        was indented weird
            but that is okay''',
    epilog='''
            likewise for this epilog whose whitespace will
        be cleaned up and whose words will be wrapped
        across a couple lines'''
)

# preserve formatting #
#######################

parser1 = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
        Please do not mess up this text!
        --------------------------------
            I have indented it
            exactly the way
            I want it
        '''))

# show default values #
#######################

parser2 = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser2.add_argument('--foo', type=int, default=42, help='FOO!')
parser2.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')

# show argument types #
#######################

parser3 = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.MetavarTypeHelpFormatter
)
parser3.add_argument('--foo', type=int)
parser3.add_argument('bar', type=float)
