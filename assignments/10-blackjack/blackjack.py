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

    parser.add_argument(
        '-p',
        '--player_hits',
        help='Player hits',
        action='store_true')

    parser.add_argument(
        '-d',
        '--dealer_hits',
        help='Dealer hits',
        action='store_true')

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
    args = get_args()
    seed = args.seed
    p_hits = args.player_hits
    d_hits = args.dealer_hits
    values = {}
    p_hand_value = 0
    d_hand_value = 0

    suits = ['♥', '♠', '♣', '♦']
    ranks = list(map(str,range(2,11))) + ['J', 'Q', 'K', 'A']
    
    for i, rank in enumerate(ranks, 2):
        if i <= 10:
            values[rank] = i
        else:
            values[rank] = 10
    values['A'] = 1

    deck_sep = list(product(suits,ranks))
    deck = []
    for tup in deck_sep:
        card = ''.join(tup)
        deck.append(card)
    deck.sort()
   
    if seed is not None:
        random.seed(seed)

    random.shuffle(deck)
    deck.reverse()
    p_hand = []
    d_hand = []

    p_hand.append(deck[0])
    d_hand.append(deck[1])
    p_hand.append(deck[2])
    d_hand.append(deck[3])
    
    next_card = 4
    if p_hits:
        p_hand.append(deck[next_card])
        next_card += 1
    if d_hits:
        d_hand.append(deck[next_card])

    for card in p_hand:
        card_rank = card[1:]
        p_hand_value += values[card_rank]
    for card in d_hand:
        card_rank = card[1:]
        d_hand_value += values[card_rank]

    print('D [{:>2}]: {}'.format(d_hand_value, ' '.join(d_hand)))
    print('P [{:>2}]: {}'.format(p_hand_value, ' '.join(p_hand)))

    if p_hand_value >= 21 or d_hand_value >= 21:
        if p_hand_value > 21:
            message = 'Player busts! You lose, loser!'
        elif d_hand_value > 21:
            message = 'Dealer busts.'
        elif p_hand_value == 21:
            message = 'Player wins. You probably cheated.'
        elif d_hand_value == 21:
            message = 'Dealer wins!' 
        print(message)
        sys.exit(0)

    if p_hand_value < 18 or d_hand_value < 18:
        if d_hand_value < 18:
            print('Dealer should hit.')
        if p_hand_value < 18:
            print('Player should hit.')
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
