import sys
import argparse
import base64
import datetime
import json
import datetime
import re

from . import io

helpText = """Tries to parse input

currently supports seconds or milliseconds sinse epoch, JWT, base64"""


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
        return parseJwt(inputString)
    except Exception as e:
        errors += "Failed to parse JWT " + str(e) + "\n"
    try:
        return parseBase64(inputString)
    except Exception as e:
        errors += "Failed to parse Base64 " + str(e) + "\n"
    print(errors, end="")

def parseJwt(inputString):
    parts = inputString.split('.')
    parsed = [parseBase64(p) for p in parts[:2]]
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

def parseBase64(data):
    missing_padding = len(data) % 4
    if missing_padding:
        data += '=' *  (4 - missing_padding)
    return base64.b64decode(data).decode('utf-8')
