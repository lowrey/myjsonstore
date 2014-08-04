import unittest
import post_myjson


class PostStringToMyJson(unittest.TestCase):
    def test_post_string(self):
        testdata = {"humungus": "I AM THE GREAT HUMUNGUS"}
        bin_id = post_myjson.post_content(testdata)
        print(bin_id)
        self.assertTrue(isinstance(bin_id, str))
        self.assertTrue("/" not in bin_id)

if __name__ == '__main__':
    unittest.main() 
