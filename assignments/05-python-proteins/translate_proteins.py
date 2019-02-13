#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-02-13
Purpose: HW 5, write a script to translate DNA or RNA into proteins
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='STR', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations',
        metavar='FILE',
        type=str,
        required=True)

    parser.add_argument(
        '-o',
        '--output',
        help='Output file name',
        metavar='FILE',
        type=str,
        default='out.txt')

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
    sequence = args.positional
    sequence = sequence.upper()
    codons = args.codons
    out_file = args.output

    if not os.path.isfile(codons):
        print('--codons "{}" is not a file'.format(codons))
        sys.exit(1)

    codon_dict = {}
    for line in open(codons):
        codon,aa = line.split()
        codon_dict[codon] = aa

    k = 3
    n = len(sequence) - k + 1

    protein = ''
    for i in range(0, n, k):
        this_codon = sequence[i:i+k]
        
        if this_codon in codon_dict.keys():
            this_aa = codon_dict[this_codon]
        else:
            this_aa = '-'
        protein += this_aa

    with open(out_file, "w") as outgoing:
        print(protein, file=outgoing)
        print('Output written to "{}"'.format(out_file))

# --------------------------------------------------
if __name__ == '__main__':
    main()
