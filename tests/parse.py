import lovef.parse
import unittest

class Tests(unittest.TestCase):

    def test_parse_base64(self):
        self.assertEqual(lovef.parse.parse("ZXhhbXBsZQ=="), "example")
        self.assertEqual(lovef.parse.parse("w6XDpMO2"), "åäö")

if __name__ == '__main__':
    unittest.main()
