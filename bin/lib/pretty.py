import json
import xml.dom.minidom
from xml.etree import ElementTree
import sys
import fileinput
import argparse

helpText = """Tries to prettify input

currently supports JSON, XML"""

def main():
    args = parseArguments()

    inputString = readFromClipboard() if args.clipboard \
        else args.input if args.input \
        else readFromStdin()

    print(prettify(inputString, args.recursive))

def parseArguments():
    parser = argparse.ArgumentParser(description = helpText, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("input", nargs='?', help="Input to prettify")
    parser.add_argument("-c", "--clipboard", help="Take input from clipboard", action="store_true")
    parser.add_argument("-r", "--recursive", help="Try to parse JSON strings recurively", action="store_true")
    return parser.parse_args()

def readFromClipboard():
    import tkinter
    return tkinter.Tk().clipboard_get()

def readFromStdin():
    text = ""
    for line in fileinput.input():
        text = text + line
    return text

def prettify(inputString, recursive = False):
    errors = ""
    try:
        return prettifyJson(inputString, recursive)
    except Exception as e:
        errors = errors + "Failed to parse JSON " + str(e) + "\n"
    try:
        return prettifyXml(inputString)
    except Exception as e:
        errors = errors + "Failed to parse XML " + str(e) + "\n"
    print(errors, end = "")

def prettifyJson(inputString, recursive):
    parsed = json.loads(inputString, strict = False)
    if recursive:
        for key in parsed:
            value = parsed[key]
            if type(value) == str:
                try:
                    parsed[key] = json.loads(value)
                except:
                    pass
    pretty = json.dumps(parsed, indent = 2)
    return pretty

def prettifyXml(inputString):
    root = ElementTree.fromstring(inputString)
    indentElementTree(root)
    return ElementTree.tostring(root, encoding='unicode').rstrip()

# http://effbot.org/zone/element-lib.htm#prettyprint
def indentElementTree(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indentElementTree(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
