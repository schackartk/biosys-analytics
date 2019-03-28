#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-03-15
Purpose: 99 bottles o' beer on tha wall
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
        '--num_bottles',
        help='How many bottles',
        metavar='INT',
        type=int,
        default=10)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    bottles = args.num_bottles

    while bottles >= 1:
        print('{} {} of beer on the wall,'.format(bottles,'bottles' if not bottles == 1 else 'bottle'))
        print('{} {} of beer,'.format(bottles,'bottles' if not bottles == 1 else 'bottle'))
        print('Take one down, pass it around,')
        bottles -= 1
        print('{} {} of beer on the wall!{}'.format(bottles,'bottles' if not bottles == 1 else 'bottle','' if bottles == 0 else '\n'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
