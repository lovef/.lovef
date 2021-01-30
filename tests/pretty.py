from lovef import pretty
import unittest

class TestStringMethods(unittest.TestCase):

    def test_pretty_json(self):
        self.assertEqual(pretty.main(['{"a":"b"}']),
            '{\n'
            '  "a": "b"\n'
            '}')

    def test_pretty_json_non_ascii(self):
        self.assertEqual(pretty.main(['{"a":"å"}']),
            '{\n'
            '  "a": "å"\n'
            '}')

    def test_pretty_json_non_ascii_escaped(self):
        self.assertEqual(pretty.main(['{"a":"å"}', '--escape']),
            '{\n'
            '  "a": "\\u00e5"\n'
            '}')

    def test_pretty_json5(self):
        self.assertEqual(pretty.main(['{a:"b" /* comment */}']),
            '{\n'
            '  "a": "b"\n'
            '}')

    def test_pretty_xml(self):
        self.assertEqual(pretty.main(['<a><b/></a>']),
        '<a>\n'
        '  <b />\n'
        '</a>')

if __name__ == '__main__':
    unittest.main()
