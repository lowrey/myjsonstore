import unittest
import myjson
import copy
from os import path


class MyJsonTests(unittest.TestCase):
    testdata = {"humungus": "I AM THE GREAT HUMUNGUS"}
    bin_id = None

    def setUp(self):
        self.bin_id = myjson.Post().content(self.testdata)

    def test_post_json(self):
        self.assertTrue(isinstance(self.bin_id, str))
        self.assertTrue("/" not in self.bin_id)

    def test_get_json(self):
        data = myjson.Get().content(self.bin_id)
        self.assertEquals(self.testdata["humungus"], data["humungus"])

    def test_put_json(self):
        self.testdata["humungus"] = "I AM NOT THE GREAT HUMUNGUS"
        myjson.Put().content(self.bin_id, self.testdata)
        data = myjson.Get().content(self.bin_id)
        self.assertEquals(self.testdata["humungus"], data["humungus"])


class MyJsonFileTests(unittest.TestCase):
    testdir = path.join(path.dirname(path.realpath(__file__)), "testdata")
    bin_id = None

    def setUp(self):
        self.bin_id = myjson.Post().file(path.join(self.testdir, "humungus.jpg"))

    def test_post_file(self):
        self.assertTrue(isinstance(self.bin_id, str))
        self.assertTrue("/" not in self.bin_id)

    def test_get_file(self):
        fpath = myjson.Get().file(self.bin_id, path.join(self.testdir, "output"))
        self.assertTrue(path.exists(fpath))

    def test_put_file(self):
        print(self.bin_id)
        myjson.Put().file(self.bin_id, path.join(self.testdir, "humungus.jpg"), "nothumungus.jpg")
        data = myjson.Get().content(self.bin_id)
        self.assertEquals("nothumungus.jpg", data["name"])

if __name__ == '__main__':
    unittest.main()
