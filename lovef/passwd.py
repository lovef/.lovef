import argparse
import secrets

helpText = """Generates passwords"""

chars = "23456789" + \
    "abcdefghijkmnopqrstuvwxyz" + \
    "ABCDEFGHJKLMNPQRSTUVWXYZ" +\
    "_-+"
charsLen = len(chars)

def main():
    args = parseArguments()

    if args.clipboard:
        length = args.length if args.length else 32
        addToClipboard(generate(length))

    printPasswordTable(args.length)

def printPasswordTable(first):
    print(f'{16:16}{24:8}{32:8}{40:8}{48:8}{56:8}{64:8}')
    print(generate(first if first else 16))
    print(generate(24))
    print(generate(32))
    print(generate(48))
    print(generate(64))
    print(f'{16:16}{24:8}{32:8}{40:8}{48:8}{56:8}{64:8}')

def parseArguments():
    parser = argparse.ArgumentParser(description = helpText, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("length", nargs='?', help="Specific length to use", type = int)
    parser.add_argument("-c", "--clipboard", help="Copy to clipboard (experimental)",
        action="store_true")
    return parser.parse_args()

def generate(length):
    password = ""
    for i in range(length):
        password += chars[secrets.randbelow(charsLen)]
    return password

# https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python
def addToClipboard(text):
    from tkinter import Tk
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update() # now it stays on the clipboard after the window is closed
    window.destroy()
    print("Added password to your clipboard")
    input("do your thing and press enter when you are done")
