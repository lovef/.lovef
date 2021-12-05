import lovef.parse
import unittest

def parse(*args):
    return lovef.parse.main(args)

class Tests(unittest.TestCase):

    def test_parse_base64(self):
        self.assertEqual(parse("ZXhhbXBsZQ=="), "example")
        self.assertEqual(parse("w6XDpMO2"), "åäö")

    def test_parse_unpadded_base64(self):
        self.assertEqual(parse("ZXhhbXBsZQ"), "example")

    def test_parse_seconds_since_epoch(self):
        self.assertEqual(parse("1612625669"), "2021-02-06 16:34:29")

    def test_parse_milliseconds_since_epoch(self):
        self.assertEqual(parse("1612625669123"), "2021-02-06 16:34:29.123")

    def test_parse_jwt(self):
        self.assertEqual(
            parse("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwidGltZSI6MTUxNjI0OTAyMiwiaWF0IjoxNTE2MjM5MDIyfQ.rzDB7r2Ay8Eei88ZmTNX2jkUXScRm0pAhmuiv7zY1RI"),
            '{"alg":"HS256","typ":"JWT"}\n' +
            '{\n' +
            '  "sub": "1234567890",\n' +
            '  "name": "John Doe",\n' +
            '  "time": 1516249022, /* 2018-01-18 05:17:02 */\n' +
            '  "iat": 1516239022 /* 2018-01-18 02:30:22 */\n' +
            '}')

    def test_parse_json(self):
        self.assertEqual(parse('{"a":"b"}'),
            '{\n'
            '  "a": "b"\n'
            '}')

    def test_parse_json_non_ascii(self):
        self.assertEqual(parse('{"a":"å"}'),
            '{\n'
            '  "a": "å"\n'
            '}')

    def test_parse_json_non_ascii_escaped(self):
        self.assertEqual(parse('{"a":"å"}', '--escape'),
            '{\n'
            '  "a": "\\u00e5"\n'
            '}')

    def test_parse_json5(self):
        self.assertEqual(parse('{a:"b" /* comment */}'),
            '{\n'
            '  "a": "b"\n'
            '}')

    def test_parse_json_with_nested_json_string(self):
        self.assertEqual(parse('{"a":"{\\"a\\":\\"b\\"}"}'),
            '{\n'
            '  "a": "{\\"a\\":\\"b\\"}"\n'
            '}')

    def test_parse_json_recursive_string(self):
        self.assertEqual(parse('{"a":"{\\"a\\":\\"b\\"}"}', '--recursive'),
            '{\n'
            '  "a": {\n'
            '    "a": "b"\n'
            '  }\n'
            '}')

    def test_parse_json_recursive_string_with_error(self):
        self.assertEqual(parse('{"a": "{a\\": \\"b\\"}"}', '--recursive'),
            '{\n'
            '  "a": "{a\\": \\"b\\"}"\n'
            '}')

    def test_parse_json_query_string(self):
        self.assertEqual(parse('{"a":"b"}', '-q', 'a'), 'b')

    def test_parse_json_query_bool(self):
        self.assertEqual(parse('{"a":false}', '-q', 'a'), 'false')

    def test_parse_json_query_float(self):
        self.assertEqual(parse('{"a":1.0}', '-q', 'a'), '1.0')

    def test_parse_json_query_float(self):
        self.assertEqual(parse('{"a":1.0}', '-q', 'a'), '1.0')

    def test_parse_json_list_query(self):
        self.assertEqual(parse('[1,"a"]', '-q', '1'), 'a')

    def test_parse_json_queries(self):
        self.assertEqual(parse('{"a":[0, {}]}', '-q', 'a', '1'), '{}')

if __name__ == '__main__':
    unittest.main()
