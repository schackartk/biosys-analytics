#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-02-21
Purpose: Grad HW 5, find the winner
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
        'positional', metavar='STATE', help='State of the board')

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
    state = args.positional
    cells = [0,1,2,3,4,5,6,7,8,9]

    acc_char = {i:0 for i in '.-XO'}
    count = 0

    for i, char in enumerate(state):
        if char in acc_char:
            count += 1
            if char == '.':
                char = '-'
            if char != '-':
                cells[i+1] = char

    if count != 9 or len(state) != 9:
        print('State "{}" must be 9 characters of only ., X, O'.format(state))
        sys.exit(1)
    
    winner = ''    

    for p in 'XO':
        for i in range(1,8,3):
            if cells[i] == cells[i+1] == cells[i+2] == p:
                winner = p
        for l in range(1,4):
            if cells[l] == cells[l+3] == cells[l+6] == p:
                winner = p
        if cells[1] == cells[5] == cells[9] == p or cells[3] == cells[5] == cells[7] == p:
            winner = p
    
    if winner == '':
        print('No winner')
    else:
        print('{} has won'.format(winner))
       
    


# --------------------------------------------------
if __name__ == '__main__':
    main()

