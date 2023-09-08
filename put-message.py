#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser(
    "put-message", description="put information into file sneaky beaky like"
)
parser.add_argument("-m", "--message", help="message to embed")
parser.add_argument("-s", "--stego", help="path to write stegocontainer")
parser.add_argument("-c", "--container", help="text to edit", required=True)


def transform_spaces(txt: str, msg: bytes) -> str:
    bit = 7
    idx = 0
    line_cnt = len(msg) * 8

    res = []
    lines = txt.split("\n")
    for i in range(line_cnt):
        line = lines[i] if i < len(lines) else ""
        if msg[idx] & (1 << bit):
            line += " "
        res.append(line)
        bit -= 1
        if bit == -1:
            bit = 7
            idx += 1
    return "\n".join(res)


transform = transform_spaces

args = parser.parse_args()

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
