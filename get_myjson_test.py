import get_myjson
import unittest

class GetFromMyjson(unittest.TestCase):
    def test_valid(self):
        data = get_myjson.get_content("2qyms")
        self.assertEquals("You are hearing me talk", data["algore"])
        
if __name__ == '__main__':
    unittest.main() 
