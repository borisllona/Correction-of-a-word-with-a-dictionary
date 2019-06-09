#!/usr/bin/env python3

"""Check correctness of assignment"""

import sys
import string

def main():
    """Check correctness of assignment"""
    original = open(sys.argv[1])
    corrected = open(sys.argv[2])
    actualeditions = open(sys.argv[3])
    realeditions = open(sys.argv[4])

    counter = 0
    byte = original.read(1)
    byte_corrected = corrected.read(1)
    files_different = -1
    while byte:
        if byte != byte_corrected:
            files_different = counter
        counter += 1
        byte = original.read(1)
        byte_corrected = corrected.read(1)

    if files_different < 0:
        sys.exit(0)
    else:
        line = actualeditions.readlines()
        aeditions = int(line[0].strip())
        line = realeditions.readlines()
        reditions = int(line[0].strip())
        if aeditions >= reditions:
            sys.exit(0)
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
