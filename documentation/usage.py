"""
>>> parser.print_help()  # doctest: +ELLIPSIS
usage: PROG [options]
...
"""

import argparse

parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
parser.add_argument('--foo', nargs='?', help='foo help')
parser.add_argument('bar', nargs='+', help='bar help')
