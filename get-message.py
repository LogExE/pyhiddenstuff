#!/usr/bin/env python3

import sys
import os
import argparse

from stego_stuff import get_spaces, get_letters

parser = argparse.ArgumentParser(
    "get-message", description="get hidden information from file"
)
parser.add_argument("-m", "--message", help="path to write message")
parser.add_argument("-s", "--stego", help="path to write stegocontainer")

args = parser.parse_args()
method = os.getenv("STEG_METHOD", "spaces")

if method == "spaces":
    get = get_spaces
elif method == "letters":
    get = get_letters

if args.stego is None:
    txt = sys.stdin.read()
else:
    with open(args.stego, "r") as srdr:
        txt = srdr.read()

msg = get(txt)

if args.message is not None:
    with open(args.message, "wb") as msgwrtr:
        msgwrtr.write(msg)
else:
    sys.stdout.buffer.write(msg)
