"""
>>> parser.parse_args('+f X ++bar Y'.split())
Namespace(bar='Y', f='X')
"""

import argparse

parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
parser.add_argument('+f')
parser.add_argument('++bar')
