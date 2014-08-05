import unittest
import myjson

class MyJsonTests(unittest.TestCase):
    testdata = {"humungus": "I AM THE GREAT HUMUNGUS"}
    bin_id = None

    # Tests posts
    def setUp(self):
        self.bin_id = myjson.Post().content(self.testdata)
        # print(bin_id)

    def test_post_json(self):
        self.assertTrue(isinstance(self.bin_id, str))
        self.assertTrue("/" not in self.bin_id)

    def test_get_json(self):
        data = myjson.Get().content(self.bin_id)
        self.assertEquals(self.testdata["humungus"], data["humungus"])


if __name__ == '__main__':
    unittest.main()
