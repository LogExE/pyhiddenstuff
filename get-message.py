import sys
import argparse

parser = argparse.ArgumentParser(
    "get-message", description="get hidden information from file"
)
parser.add_argument("-m", "--message", help="path to write message")
parser.add_argument("-s", "--stego", help="path to write stegocontainer")


def get_spaces(txt: str) -> bytes:
    lines = txt.split('\n')

    res = []
    byte = 0
    bit = 7
    for line in lines:
        if len(line) > 0 and line[-1] == " ":
            byte += 1 << bit
        bit -= 1
        if bit == -1:
            res.append(byte)
            byte = 0
            bit = 7
    return bytes(res)

get = get_spaces

args = parser.parse_args()

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
