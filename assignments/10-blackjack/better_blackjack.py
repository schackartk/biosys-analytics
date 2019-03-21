#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-03-20
Purpose: A game of blackjack
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
def evaluate(hand, values):
    
    value = 0
    ranks = []
    ace = False
    
    for card in hand:
        rank = card[1:]
        if rank == 'A':
            ace = True

        value += values[rank]
        
        if value > 21 and ace:
            value -= 10
            ace = False

    return value
# --------------------------------------------------
def print_hands_hidden(p_hand, d_hand):
    print('\nD:  ? {:>3}'.format(' '.join(d_hand[1:])))
    print('P: {:>3}'.format(' '.join(p_hand)))

# --------------------------------------------------
def print_hands(p_hand,d_hand):
    print('D: {:>3}'.format(' '.join(d_hand)))
    print('P: {:>3}'.format(' '.join(p_hand)))

# --------------------------------------------------
def main():
    args = get_args()
    seed = args.seed
    values = {}
    p_hand = []
    d_hand = []
    p_hand_value = 0
    d_hand_value = 0

    suits = ['♥', '♠', '♣', '♦']
    ranks = list(map(str,range(2,11))) + ['J', 'Q', 'K', 'A']
    
    for i, rank in enumerate(ranks, 2):
        if i <= 10:
            values[rank] = i
        else:
            values[rank] = 10
    values['A'] = 11

    deck_sep = list(product(suits,ranks))
    deck = []
    for tup in deck_sep:
        card = ''.join(tup)
        deck.append(card)
    deck.sort()
   
    if seed is not None:
        random.seed(seed)

    random.shuffle(deck)

    p_hand.append(deck[0])
    p_hand.append(deck[2])
    d_hand.append(deck[1])
    d_hand.append(deck[3])
    next_card = 4

    print_hands_hidden(p_hand,d_hand)   
 
    if evaluate(p_hand,values) == 21:
            print('Blackjack! You win!')
            sys.exit(0)

    wanna_hit = input('Would you like to hit? (y/N)')
    hit = True if wanna_hit in ['y','yes','Y','YES'] else False

    while hit:
        p_hand.append(deck[next_card])
        next_card += 1
        print_hands_hidden(p_hand,d_hand)       
 
        if evaluate(p_hand,values) > 21:
            print('Bust! Better luck next time.')
            sys.exit(0)
        if evaluate(p_hand,values) == 21:
            print('You won!')
            sys.exit(0)
 
        wanna_hit = input('Would you like to hit? (y/N)')
        hit = True if wanna_hit in ['y','yes','Y','YES'] else False

    print('\nShow em:')
    print_hands(p_hand,d_hand)
 
    while evaluate(d_hand, values) < 17:
        d_hand.append(deck[next_card])
        next_card += 1
        print('Dealer must hit\n')
        print_hands(p_hand,d_hand)

    if evaluate(d_hand,values) > 21:
        print('Dealer busts! I suppose you win')
        sys.exit(0)

    if evaluate(p_hand, values) > evaluate(d_hand,values):
        print('You won!')
    elif evaluate(p_hand, values) < evaluate(d_hand,values):
        print('You lost, better luck next time')
    else:
        print('Draw!')

# --------------------------------------------------
if __name__ == '__main__':
    main()
