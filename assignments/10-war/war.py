#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-03-19
Purpose: Rock the Casbah
"""

import argparse
import sys
from itertools import product
import random

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='"War" card game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
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
    seed = args.seed
    values = {}

    suits = ['♥', '♠', '♣', '♦']
    ranks = list(map(str,range(2,11))) + ['J', 'Q', 'K', 'A']
    for rank in ranks:
        if rank.isdigit():
            values[rank] = int(rank)
        else:
            continue
    values['J'] = 11
    values['Q'] = 12
    values['K'] = 13
    values['A'] = 14    

    deck_sep = list(product(suits,ranks))
    deck = []
    for tup in deck_sep:
        card = ''.join(tup)
        deck.append(card)
    deck.sort()
   
    if seed is not None:
        random.seed(seed)

    random.shuffle(deck)

    p1_hand = []
    p2_hand = []
    for i, cards in enumerate(deck):
        if i%2:
            p1_hand.append(cards)
        else:
            p2_hand.append(cards)
    p1_hand.reverse()
    p2_hand.reverse()

    score_1 = 0
    score_2 = 0

    for rounds in range(0,26):
        p1_play = p1_hand[rounds]
        p2_play = p2_hand[rounds]
        p1_val = values[p1_play[1:]]
        p2_val = values[p2_play[1:]]

        if p1_val > p2_val:
            winner = 'P1'
            score_1 += 1
        elif p1_val < p2_val:
            winner = 'P2'
            score_2 += 1
        else:
            winner = 'WAR!' 
        print('{:>3} {:>3} {}'.format(p1_hand[rounds],p2_hand[rounds],winner))

    if score_1 > score_2:
        won = 'Player 1 wins'
    elif score_1 < score_2:
        won = 'Player 2 wins'
    else:
        won = 'DRAW'

    print('P1 {} P2 {}: {}'.format(score_1,score_2,won))

# --------------------------------------------------
if __name__ == '__main__':
    main()
