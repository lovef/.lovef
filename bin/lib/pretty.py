#!/usr/bin/env python3

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

    print(prettify(inputString))

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

def prettify(inputString):
    errors = ""
    try:
        return prettifyJson5(inputString)
    except Exception as e:
        errors = errors + "Failed to parse JSON 5: " + str(e) + "\n"
    try:
        return prettifyJson(inputString)
    except Exception as e:
        errors = errors + "Failed to parse JSON: " + str(e) + "\n"
    try:
        return prettifyXml(inputString)
    except Exception as e:
        errors = errors + "Failed to parse XML: " + str(e) + "\n"
    print(errors, end = "")

def prettifyJson5(inputString):
    import json5
    parsed = json5.loads(inputString)
    return json.dumps(parsed, indent=2)

def prettifyJson(inputString):
    parsed = json.loads(inputString)
    return json.dumps(parsed, indent=2)

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
