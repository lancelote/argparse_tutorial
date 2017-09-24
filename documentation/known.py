"""
>>> parser.parse_known_args('--foo --badger BAR spam'.split())
(Namespace(bar='BAR', foo=True), ['--badger', 'spam'])
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true')
parser.add_argument('bar')
