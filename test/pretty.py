import lib.pretty
import unittest

class TestStringMethods(unittest.TestCase):

    def test_pretty_json(self):
        self.assertEqual(lib.pretty.prettify('{"a":"b"}'),
            '{\n'
            '  "a": "b"\n'
            '}')

    def test_pretty_json5(self):
        self.assertEqual(lib.pretty.prettify('{a:"b" /* comment */}'),
            '{\n'
            '  "a": "b"\n'
            '}')

    def test_pretty_xml(self):
        self.assertEqual(lib.pretty.prettify('<a><b/></a>'),
        '<a>\n'
        '  <b />\n'
        '</a>')

if __name__ == '__main__':
    unittest.main()
