import sys
import fileinput
import argparse
import base64

helpText = """Tries to parse input

currently supports base64"""

def main():
    args = parseArguments()

    inputString = readFromClipboard() if args.clipboard \
        else args.input if args.input \
        else readFromStdin()

    print(parse(inputString))

def parseArguments():
    parser = argparse.ArgumentParser(description = helpText, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("input", nargs='?', help="Input to prettify")
    parser.add_argument("-c", "--clipboard", help="Take input from clipboard",
        action="store_true")
    return parser.parse_args()

def readFromClipboard():
    import tkinter
    return tkinter.Tk().clipboard_get()

def readFromStdin():
    text = ""
    for line in fileinput.input():
        text = text + line
    return text

def parse(inputString):
    errors = ""
    try:
        return parseBase64(inputString)
    except Exception as e:
        errors = errors + "Failed to parse Base64 " + str(e) + "\n"
    print(errors, end = "")

def parseBase64(inputString):
    return base64.b64decode(inputString).decode('utf-8')
