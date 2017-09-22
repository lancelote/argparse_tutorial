"""
>>> parser0.parse_args('-bac MMM'.split())
Namespace(bacon='MMM', badger=None)
>>> parser0.parse_args('-bad WOOD'.split())
Namespace(bacon=None, badger='WOOD')
>>> parser0.parse_args('-ba BA'.split())  # doctest: +SKIP
usage: PROG [-h] [-bacon BACON] [-badger BADGER]
PROG: error: ambiguous option: -ba could match -badger, -bacon

>>> parser1.parse_args('-bac MMM'.split())  # doctest: +SKIP
usage: PROG [-h] [-bacon BACON] [-badger BADGER]
PROG: error: unrecognized arguments: -bac MMM
"""

import argparse

parser0 = argparse.ArgumentParser(prog='PROG')
parser0.add_argument('-bacon')
parser0.add_argument('-badger')

# disable abbreviations #
#########################

parser1 = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
parser1.add_argument('-bacon')
parser1.add_argument('-badger')
