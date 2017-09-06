"""
>>> from documentation.simple_example import parser
>>> args = parser.parse_args(['1', '2', '3'])
>>> args.accumulate(args.integers)
3
>>> args = parser.parse_args(['1', '2', '3', '--sum'])
>>> args.accumulate(args.integers)
6
"""

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
