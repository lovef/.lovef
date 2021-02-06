import sys
import argparse
import base64
import datetime

from . import io

helpText = """Tries to parse input

currently supports base64"""


def main():
    args = parseArguments()

    inputString = io.readFromClipboard() if args.clipboard \
        else args.input if args.input \
        else io.readFromStdin()

    print(parse(inputString))


def parseArguments():
    parser = argparse.ArgumentParser(description=helpText, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("input", nargs='?', help="Input to parse")
    parser.add_argument("-c", "--clipboard", help="Take input from clipboard", action="store_true")
    return parser.parse_args()


def parse(inputString):
    errors = ""
    try:
        return str(datetime.datetime.fromtimestamp(int(inputString)))
    except Exception as e:
        errors += "Failed to parse date time from seconds " + str(e) + "\n"
    try:
        return datetime.datetime.fromtimestamp(int(inputString)/1000) \
            .isoformat(sep=' ', timespec='milliseconds')
    except Exception as e:
        errors += "Failed to parse date time from miliseconds " + str(e) + "\n"
    try:
        return parseBase64(inputString)
    except Exception as e:
        errors += "Failed to parse Base64 " + str(e) + "\n"
    print(errors, end="")


def parseBase64(inputString):
    return base64.b64decode(inputString).decode('utf-8')
