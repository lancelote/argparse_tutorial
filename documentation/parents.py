import argparse


parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--parent', type=int)


foo_parser = argparse.ArgumentParser(parents=[parent_parser])
foo_parser.add_argument('foo')

bar_parser = argparse.ArgumentParser(parents=[parent_parser])
bar_parser.add_argument('--bar')
