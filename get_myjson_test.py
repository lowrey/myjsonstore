import get_myjson as g
import unittest
import json

class GetFromMyjson(unittest.TestCase):
    def test_valid(self):
        c = g.get_content("2qyms")
        jsonc = json.loads(c)
        self.assertEquals(jsonc.algor, "You are hearing me talk.")
        
if __name__ == '__main__':
    unittest.main() 
