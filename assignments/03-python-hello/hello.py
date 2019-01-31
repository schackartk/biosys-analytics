#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-01-31
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]
    num_args = len(args)

    if num_args < 1:
        print('Usage: {} NAME [NAME2 ...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

   
    if num_args == 1:
        print('Hello to the ' + str(num_args) + ' of you: ' + args[0] + '!')
    elif num_args == 2:
        print('Hello to the ' + str(num_args) + ' of you: ' + ' and '.join(args) + '!')
    else:
        print('Hello to the ' + str(num_args) + ' of you: ' + ', '.join(args[:-1]) + ', and ' + args[num_args - 1] + '!')


# --------------------------------------------------
main()
