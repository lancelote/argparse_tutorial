"""
>>> parser.parse_args('--foo BAR'.split())
Namespace(foo='BAR')
>>> parser.parse_args([])  # doctest: +SKIP
usage: argparse.py [-h] [--foo FOO]
argparse.py: error: option --foo is required
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', required=True)
