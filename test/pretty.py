import lib.pretty
import unittest
import json

class TestStringMethods(unittest.TestCase):

    def test_pretty_json(self):
        self.assertEqual(lib.pretty.prettify('{"a":"b"}'),
            '{\n'
            '  "a": "b"\n'
            '}')
        self.assertEqual(lib.pretty.prettify('{"a":{"a":"b"}}'),
            '{\n'
            '  "a": {\n'
            '    "a": "b"\n'
            '  }\n'
            '}')
        json.loads('{"a": "{\\"a\\": \\"b\\"}"}')
        self.assertEqual(lib.pretty.prettify('{"a": "{\\"a\\": \\"b\\"}"}'),
            '{\n'
            '  "a": "{\\"a\\": \\"b\\"}"\n'
            '}')

    def test_pretty_json_recursive_string(self):
        self.assertEqual(lib.pretty.prettify('{"a": "{\\"a\\": \\"b\\"}"}', recursive = True),
            '{\n'
            '  "a": {\n'
            '    "a": "b"\n'
            '  }\n'
            '}')

    def test_pretty_json_recursive_string_with_error(self):
        self.assertEqual(lib.pretty.prettify('{"a": "{a\\": \\"b\\"}"}', recursive = True),
            '{\n'
            '  "a": "{a\\": \\"b\\"}"\n'
            '}')

    def test_pretty_xml(self):
        self.assertEqual(lib.pretty.prettify('<a><b/></a>'),
        '<a>\n'
        '  <b />\n'
        '</a>')

if __name__ == '__main__':
    unittest.main()
