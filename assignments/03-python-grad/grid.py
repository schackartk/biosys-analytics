#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-02-04
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():

    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    number = args[0]

    if int(number) < 2 or int(number) > 9:
        print('NUM ({}) must be between 1 and 9'.format(number))
        sys.exit(1)

    l = 1
    i = 1
    j = 1
    while i <= int(number):
        while j <= int(number):
            if j != int(number):
                print(str(l).rjust(3), end ="")
                l += 1
                j += 1
            else:
                print(str(l).rjust(3))
                l += 1
                j += 1
        i += 1
        j = 1



# --------------------------------------------------
main()
