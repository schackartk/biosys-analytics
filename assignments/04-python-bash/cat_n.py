#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-02-07
Purpose: Homework 4, imitate cat -n using python
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {}  FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    arg = args[0]

    if not os.path.isfile(arg):
        print('{} is not a file'.format(arg))
        sys.exit(1)    
    
    lines = []
    
    for line in open(arg):
        lines.append(line)
    
    for i, line in enumerate(lines):
        print('{:3}: {}'.format(i, line,), end='')
    


# --------------------------------------------------
main()
