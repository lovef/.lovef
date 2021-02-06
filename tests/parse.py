import lovef.parse
import unittest


class Tests(unittest.TestCase):

    def test_parse_base64(self):
        self.assertEqual(lovef.parse.parse("ZXhhbXBsZQ=="), "example")
        self.assertEqual(lovef.parse.parse("w6XDpMO2"), "åäö")

    def test_parse_seconds_since_epoch(self):
        self.assertEqual(lovef.parse.parse(
            "1612625669"), "2021-02-06 16:34:29")

    def test_parse_milliseconds_since_epoch(self):
        self.assertEqual(lovef.parse.parse("1612625669123"),
                         "2021-02-06 16:34:29.123")


if __name__ == '__main__':
    unittest.main()
