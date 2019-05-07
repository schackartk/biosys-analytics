#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-05-07
Purpose: Final for 534
"""

import argparse
import sys
import os
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Convert all words of a file to pig latin',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files',
        metavar='FILE',
        help='Input file(s)',
        nargs='+',
        type=str),

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='str',
        type=str,
        default='out-yay')

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
def pigify(word):
    """Turn word into pig latin"""
    word = re.sub("[^a-zA-Z0-9']", '', word)
    #word = re.sub('\d','',word)

    begin_punct = re.compile('[^a-zA-Z0-9]')
    begin_cons = re.compile('(?P<begin>[^aeiouAEIOU]+)'
                            '(?P<end>[a-zA-Z]*)')

    match_punct = begin_punct.match(word)
    match = begin_cons.match(word)
    
    if match_punct:
        pig = ('-yay')
    elif match:
        pig = '{}-{}ay'.format(match.group('end'),match.group('begin'))
    else:
        pig = '{}-yay'.format(word)

    return pig
        

# --------------------------------------------------
def main():
    """Main"""
    args = get_args()
    files = args.files
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)    

    num_writes = 0
    for f in files:
        if not os.path.isfile(f):
            print('"{}" is not a file.'.format(f))
        else:
            num_writes += 1
            name = os.path.basename(f)
            print('{}: {}'.format(num_writes,name))
            out_file = os.path.join(out_dir,name)
            out_fh = open(out_file,'w')
            for line in open(f).read().split('\n'):
                for word in line.split():
                    out_fh.write('{} '.format(pigify(word)))
                out_fh.write('\n')

    print('Done, wrote {} {} to "{}".'.format(num_writes,'file' if num_writes == 1 else 'files', out_dir))
# --------------------------------------------------
if __name__ == '__main__':
    main()
