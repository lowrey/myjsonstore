import unittest
import myjson
from os import path


class MyJsonTests(unittest.TestCase):
    testdata = {"humungus": "I AM THE GREAT HUMUNGUS"}
    bin_id = None

    def setUp(self):
        self.bin_id = myjson.Post().content(self.testdata)
        # print(bin_id)

    def test_post_json(self):
        self.assertTrue(isinstance(self.bin_id, str))
        self.assertTrue("/" not in self.bin_id)

    def test_get_json(self):
        data = myjson.Get().content(self.bin_id)
        self.assertEquals(self.testdata["humungus"], data["humungus"])


class MyJsonFileTests(unittest.TestCase):
    testdir = path.join(path.dirname(path.realpath(__file__)), "testdata")
    bin_id = None

    def setUp(self):
        self.bin_id = myjson.Post().file(path.join(self.testdir, "humungus.jpg"))
        print(self.bin_id)

    def test_post_file(self):
        self.assertTrue(isinstance(self.bin_id, str))
        self.assertTrue("/" not in self.bin_id)

    def test_get_file(self):
        fpath = myjson.Get().file(self.bin_id, path.join(self.testdir, "output"))
        self.assertTrue(path.exists(fpath))

if __name__ == '__main__':
    unittest.main()
