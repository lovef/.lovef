from lovef.parse import parse
import unittest


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


if __name__ == '__main__':
    unittest.main()
