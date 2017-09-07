"""
>>> parser.parse_args(['--foon'])  # doctest: +SKIP
usage: PROG [-h] [--foobar] [--foonley]
PROG: error: unrecognized arguments: --foon
"""

import argparse

parser = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
parser.add_argument('--foobar', action='store_true')
parser.add_argument('--foonley', action='store_false')
