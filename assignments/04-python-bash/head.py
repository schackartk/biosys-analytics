#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-02-07
Purpose: Homework 4, imitate head using python
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) < 1 or len(args) > 2:
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    head_file = args[0]

    if not os.path.isfile(head_file):
        print('{} is not a file'.format(head_file))
        sys.exit(1)

    if len(args) > 1:
            num_lines = int(args[1])
    else:
        num_lines = 3

    if num_lines < 1:
        print('lines ({}) must be a positive number'.format(num_lines))
        sys.exit(1)

    lines = open(head_file).readlines()

    for i, line in enumerate(lines):
        if i <= (num_lines - 1):
            print('{}'.format(line), end='')
        else:
            sys.exit(0)

# --------------------------------------------------
main()
