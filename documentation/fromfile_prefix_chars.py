"""
>>> parser.parse_args(['-f', 'foo', '@args.txt'])
Namespace(f='bar')
"""

import argparse

parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument('-f')
