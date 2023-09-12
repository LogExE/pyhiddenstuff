#!/usr/bin/env python3

import sys
import os
import argparse

from stego_stuff import transform_spaces, transform_letters

parser = argparse.ArgumentParser(
    "put-message", description="put information into file sneaky beaky like"
)
parser.add_argument("-m", "--message", help="message to embed")
parser.add_argument("-s", "--stego", help="path to write stegocontainer")
parser.add_argument("-c", "--container", help="text to edit", required=True)

args = parser.parse_args()
method = os.getenv("STEG_METHOD", "spaces")

if method == "spaces":
    transform = transform_spaces
elif method == "letters":
    transform = transform_letters

if args.message is None:
    msg = sys.stdin.buffer.read()
else:
    with open(args.message, "rb") as msgrdr:
        msg = msgrdr.read()

with open(args.container, "r") as contrdr:
    txt = contrdr.read()
    result = transform(txt, msg)
    if args.stego is not None:
        with open(args.stego, "w") as stegowrtr:
            stegowrtr.write(result)
    else:
        sys.stdout.write(result)
