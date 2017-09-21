"""
>>> parser0.parse_args(['rock'])
Namespace(move='rock')
>>> parser0.parse_args(['fire'])  # doctest: +SKIP
usage: game.py [-h] {rock,paper,scissors}
game.py: error: argument move: invalid choice: 'fire' (choose from 'rock',
'paper', 'scissors')

>>> parser1.parse_args(['3'])
Namespace(doors=3)
>>> parser1.parse_args(['4'])  # doctest: +SKIP
usage: doors.py [-h] {1,2,3}
doors.py: error: argument door: invalid choice: 4 (choose from 1, 2, 3)
"""

import argparse

# simple example #
##################

parser0 = argparse.ArgumentParser(prog='game.py')
parser0.add_argument('move', choices=['rock', 'paper', 'scissors'])

# type conversion and choices #
###############################

parser1 = argparse.ArgumentParser(prog='doors.py')
parser1.add_argument('doors', type=int, choices=range(1, 4))
