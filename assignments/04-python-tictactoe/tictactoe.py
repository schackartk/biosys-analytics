#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-02-07
Purpose: Grad HW 4, make a game of tic tac toe
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--state',
        help='The state of the board',
        metavar='str',
        type=str,
        default='---------')

    parser.add_argument(
        '-p',
        '--player',
        help='The player to modify the state',
        metavar='str',
        type=str)

    parser.add_argument(
        '-c',
        '--cell',
        help='The cell to alter',
        metavar='int',
        type=int)

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
    state = args.state
    player = args.player
    cell = args.cell
    cells = [0,1,2,3,4,5,6,7,8,9]
   
    acc_char = {i:0 for i in '-XO'}
    count = 0

    for i, char in enumerate(state):
        if char in acc_char:
            count += 1
            if char != '-':
                cells[i+1] = char
    
    if count != 9 or len(state) != 9:
        print('Invalid state "{}", must be 9 characters of only -, X, O'.format(state))
        exit(1)

    if player != 'X' and player != 'O' and player != None:
        print('Invalid player "{}", must be X or O'.format(player))
        exit(1)

    if cell != None:
        if not 0 < cell < 10:
            print('Invalid cell "{}", must be 1-9'.format(cell))
            exit(1)

    if any([cell, player]):
        if not all([cell, player]):
            print('Must provide both --player and --cell')
            exit(1)
        elif cells[cell] != 'X' and cells[cell] != 'O':
            cells[cell]=player
        else:
            print('Cell {} already taken'.format(cell))
            exit(1)

    border = '-------------'

    print(border)
    print('| {} | {} | {} |'.format(cells[1], cells[2], cells[3]))
    print(border)
    print('| {} | {} | {} |'.format(cells[4], cells[5], cells[6]))
    print(border)
    print('| {} | {} | {} |'.format(cells[7], cells[8], cells[9]))
    print(border)


# --------------------------------------------------
if __name__ == '__main__':
    main()
