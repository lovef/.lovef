import sys
import argparse
import base64
import datetime
import json
import datetime
import re

from . import io

helpText = """Tries to parse input

currently supports seconds or milliseconds since epoch, JSON, JWT, base64"""


def script():
    print(main())

def main(args=sys.argv[1:]):
    args = parseArguments(args)

    inputString = io.readFromClipboard() if args.clipboard \
        else args.input if args.input \
        else io.readFromStdin()

    return Parser(args).parse(inputString)


def parseArguments(args):
    parser = argparse.ArgumentParser(description=helpText, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("input", nargs='?', help="Input to parse")
    parser.add_argument("-c", "--clipboard", help="Take input from clipboard", action="store_true")
    parser.add_argument("-e", "--escape", help="Escape non-ascii characters", action="store_true")
    parser.add_argument("-q", "--query", nargs='*', help="Query output")
    return parser.parse_args(args)

class Parser:
    args = None

    def __init__(self, args):
        self.args = args

    def parse(self, inputString):
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
            return self.parseJson5(inputString)
        except Exception as e:
            errors = errors + "Failed to parse JSON 5: " + str(e) + "\n"
        try:
            return self.parseJson(inputString)
        except Exception as e:
            errors = errors + "Failed to parse JSON: " + str(e) + "\n"
        try:
            return self.parseJwt(inputString)
        except Exception as e:
            errors += "Failed to parse JWT " + str(e) + "\n"
        try:
            return self.parseBase64(inputString)
        except Exception as e:
            errors += "Failed to parse Base64 " + str(e) + "\n"
        print(errors, end="")

    def parseJwt(self, inputString):
        parts = inputString.split('.')
        parsed = [self.parseBase64(p) for p in parts[:2]]
        payload = json.loads(parsed[1])
        payloadPretty = json.dumps(payload, indent=2)
        for key in payload:
            value = payload[key]
            try:
                d = datetime.datetime.fromtimestamp(value)
                payloadPretty = re.sub(f"{value},?", f"\\g<0> /* {d} */", payloadPretty)
            except:
                pass
        return parsed[0] + "\n" + payloadPretty

    def parseBase64(self, data):
        missing_padding = len(data) % 4
        if missing_padding:
            data += '=' *  (4 - missing_padding)
        return base64.b64decode(data).decode('utf-8')

    def parseJson5(self, inputString):
        import json5
        parsed = json5.loads(inputString)
        return self.dumps(parsed)

    def parseJson(self, inputString):
        parsed = json.loads(inputString)
        return self.dumps(parsed)

    def dumps(self, obj):
        for query in self.args.query or []:
            if type(obj) is list:
                obj = obj[int(query)]
            else:
                obj = obj[query]
        if type(obj) is str:
            return obj
        return json.dumps(obj, indent=2, ensure_ascii=self.args.escape)
