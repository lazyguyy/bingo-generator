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

def generate_single_bingo(lines):
    shuffled = random.sample(lines[1:], 24)
    return shuffled[:12] + lines[:1] + shuffled[12:]

def main(board_text, document_text, separator):
    lines = [line.strip() for line in sys.stdin if line.strip()]

    _assert(len(lines) >= 25, "Not enough tiles to fill a 5x5 Bingo board!")

    bingos = [board_text.format(*generate_single_bingo(lines))
              for _ in range(args.count)]
    print(document_text.format(separator.join(bingos)))

board_text = decode_b64_string(b'eJyt1kFPgzAUwPG7n+IluwzlsLjdzI4ketlh80YXg+s'
                b'bvjg60naiI3x3AdFEfHEkPE6FpL+m/YeAesaUTOnp9ZzTzp8sVldQX6p54'
                b'vzHAUsyb+QqWEJscecTkx4whIwMZacMHJ1xqVJLevs1zxw1xu2ULSQepuq'
                b'43zv0IXSDAEpV2CT3+O7LycNqE60fn+6jdTSpqrthBNxAu6IMdXstiM0ls'
                b'cUQ7F/t+6QETv8PNb4CR46uwaGjq3CoSJ1uuzJ9+phIIQaVaMSwEpUYVqT'
                b'TXLJTHxPpxKASnRhWohPDDurUstomRew85t2HB6azEGYBNDf1Is3MgrR/q'
                b'fWfcXC58UKycR8TacygEo0ZVqIxww57FxUa/fuP5BOmAtoe')

document_text = decode_b64_string(b'eJx1kD9vAjEMxfd8ikq3VlWPqQvjSa1UMVA2gqrU'
                b'cY6I/EGJ6RWifPcmiDtxA5v1/Hu2n7n0cLLoCIyIMYlAGgxmxk8RjwIOos'
                b'etFaHXbrkA+/xkUNGyBbtLPXqLFM4zNpE+XObuTbtLyjtCB3P0V4RBS9oX'
                b'9QfLgjSeUoRqUMJqc05gY8w8okGgKjPucABvrXAy8T5omdPry4IT/tE475'
                b'5wXmLUF6xU+/YQ80pFpCv0kBmCONZe3pZMt6OnFHebbi0oWTBk/ln+h03L'
                b'scwYtVpP1sxY87H66tab7/du3TWMXfvTP/4BEoqlPg==')

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

    main(board_text, document_text, args.separator)
