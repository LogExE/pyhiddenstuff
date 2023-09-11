#!/usr/bin/env python3

import sys
import argparse

from stego_stuff import get_spaces, get_letters

parser = argparse.ArgumentParser(
    "get-message", description="get hidden information from file"
)
parser.add_argument("-m", "--message", help="path to write message")
parser.add_argument("-s", "--stego", help="path to write stegocontainer")

args = parser.parse_args()

if args.stego is None:
    txt = sys.stdin.read()
else:
    with open(args.stego, "r") as srdr:
        txt = srdr.read()

msg = get_letters(txt)

if args.message is not None:
    with open(args.message, "wb") as msgwrtr:
        msgwrtr.write(msg)
else:
    sys.stdout.buffer.write(msg)
