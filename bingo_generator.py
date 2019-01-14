import base64
import random
import sys
import zlib

from argparse import ArgumentParser

def _assert(cond, message):
    if not cond:
        print(message, file=sys.stderr)
        sys.exit(1)

def decode_b64_string(string):
    return zlib.decompress(base64.b64decode(string)).decode("utf-8")

def generate_bingos(lines, number):
    bingos = []
    for _ in range(number):
        shuffled = random.sample(lines[1:], 24)
        bingos.extend(shuffled[:12] + lines[:1] + shuffled[12:])
    return bingos

def main(board_text, document_text, separator, count):
    lines = [line.strip() for line in sys.stdin if line.strip()]

    _assert(len(lines) >= 25, "Not enough tiles to fill a 5x5 Bingo board!")

    number = (len(board_text.split("{{}}")) - 1) // 25

    bingos = [board_text.format(*generate_bingos(lines, number))
              for _ in range(count)]
    print(document_text.format(separator.join(bingos)))

board_text = decode_b64_string(b'eJztmk1rwjAYx+/9FAFh6CbDt4Mgwi7CdtnB7WZk1DZ'
                b'qmI0ljXYz5LuvqZlvi0PwOXh4PEjaPM8vaf6XH6U6oBlTCyZmaq6pmvMs5'
                b'7GaG9147HSpYl9qex1QwfJomSShiDWdSR7bktZBx3GFWMYs4xtmq5rds2X'
                b'L6bRYviw6W5PLMLUbMaPmWNMJm3Gh16F0+9yv5KYiJhSThmaR5KmyM5UmZ'
                b'QXod8KOd/0mCFyfCierRSiNftImioq/gyn+uUl5pFaSmYAUP2rvZOp7wTQ'
                b'Xa54Z0icjySIVitmC1UnCBU9WCbGr98vTGm/77GZHZcuYhIpU3QHUiRvUy'
                b'P55deXl9W0wfP94HgwHFWN6lyHIAylXhEG17gFhbUhY5xLYv7TfkwI4/T+'
                b'o61PwIa9Owwe9OhUfFCQd97gw+ZzCQBLyQCEy8mAhUvJgQXJqQ+Z0CgPJy'
                b'QOFyMmDhcjJgwXJqQOZ0ykMJCcPFCInDxYiJw/2spy24FiG+ShTLHWKQKq'
                b'NOmnUiL0oltn5UMHfjWu9oBSYYyW5Q1NBU0FTQVNBU0FTQVNBU7lZU6EU3'
                b'6qgq6CroKugq6CroKugq9yuq+BbFTQVNBU0FTQVNBU0FTSV2zUVSt1d9w1'
                b'LEJgfpljihA==')

document_text = decode_b64_string(b'eJxVz01rwzAMBuB7fkWg126hOw56GoHt0kPXW12G'
                b'oii2qT+CrSxzTf77XOgYOerhlXgleo+TJcdoIMYMgTUaWioxRRoBryDpbC'
                b'FI7fYvaLe1oYH3O7SXLMlb4pBW2cz6eltvn3aXPHjH5HAd/YYw657VWgdw'
                b'mFQfio5ljpzMA4vg4D3nt0DA1NezZlULph9mzop5jK9NIwtO3TN62xi4JT'
                b'ml1HTaSf8kyVEA9mEplzoqL+W/5wvcKw5gtUkZbYyLiGQI+c6VcDQbcpJV'
                b'Fqx0fNSuNh+Hz/Z4+npvj+2mqgS5/v/kLxCMhoA=')

if __name__ == "__main__":

    parser = ArgumentParser(description="Generates 5x5 Bingo boards.")
    parser.add_argument("count", metavar="n", type=int, nargs="?", default=1, 
                        help="Number of Bingo boards to be generated.")
    parser.add_argument("-d", "--document-template", dest="document",
                        help="File containing a latex template in which to "
                             "embed the Bingo boards.")
    parser.add_argument("-b", "--board-template", dest="board",
                        help="File containing a latex template in which to "
                             "embed the values for a single Bingo board.")
    parser.add_argument("-p", "--placeholder", default="#INSERT_HERE#",
                        help="Placeholder string for Bingo fields.")
    parser.add_argument("-s", "--separator", default="\n\\newpage\n",
                        help="String to join the Bingo boards with.")
    args = parser.parse_args()

    if args.document:
        with open(args.document) as document:
            document_text = document.read()
    document_text = document_text.replace("{", "{{") \
                                 .replace("}", "}}") \
                                 .replace(args.placeholder, "{}")


    if args.board:
        with open(args.board) as board:
            board_text = board.read()
    board_text = board_text.replace("{", "{{") \
                           .replace("}", "}}") \
                           .replace(args.placeholder, "{}")

    main(board_text, document_text, args.separator, args.count)
