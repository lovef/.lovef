import lovef.uuid
import uuid
import unittest

class TestStringMethods(unittest.TestCase):

    def test_uuid_format(self):
        uuid.UUID(lovef.uuid.main())

    def test_unique(self):
        self.assertNotEqual(lovef.uuid.main(), lovef.uuid.main())

if __name__ == '__main__':
    unittest.main()
