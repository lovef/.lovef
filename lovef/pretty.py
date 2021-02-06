import json
import xml.dom.minidom
from xml.etree import ElementTree
import sys
import argparse

from . import io

helpText = """Tries to prettify input

currently supports JSON, XML"""

def main(args=sys.argv[1:]):
    args = parseArguments(args)

    inputString = io.readFromClipboard() if args.clipboard \
        else args.input if args.input \
        else io.readFromStdin()

    return Pretty(args).prettify(inputString)

def parseArguments(args):
    parser = argparse.ArgumentParser(description = helpText, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("input", nargs='?', help="Input to prettify")
    parser.add_argument("-c", "--clipboard", help="Take input from clipboard", action="store_true")
    parser.add_argument("-e", "--escape", help="Escape non-ascii characters", action="store_true")
    return parser.parse_args(args)

class Pretty:
    args = None

    def __init__(self, args):
        self.args = args

    def prettify(self, inputString):
        errors = ""
        try:
            return self.prettifyJson5(inputString)
        except Exception as e:
            errors = errors + "Failed to parse JSON 5: " + str(e) + "\n"
        try:
            return self.prettifyJson(inputString)
        except Exception as e:
            errors = errors + "Failed to parse JSON: " + str(e) + "\n"
        try:
            return self.prettifyXml(inputString)
        except Exception as e:
            errors = errors + "Failed to parse XML: " + str(e) + "\n"
        print(errors, end = "")

    def prettifyJson5(self, inputString):
        import json5
        parsed = json5.loads(inputString)
        return self.dumps(parsed)

    def prettifyJson(self, inputString):
        parsed = json.loads(inputString)
        return self.dumps(parsed)

    def dumps(self, jsonString):
        return json.dumps(jsonString, indent=2, ensure_ascii=self.args.escape)

    def prettifyXml(self, inputString):
        root = ElementTree.fromstring(inputString)
        self.indentElementTree(root)
        return ElementTree.tostring(root, encoding='unicode').rstrip()

    # http://effbot.org/zone/element-lib.htm#prettyprint
    def indentElementTree(self, elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indentElementTree(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
