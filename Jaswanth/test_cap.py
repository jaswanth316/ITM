
import unittest
import cap

class Testcap(unittest.TestCase):
    
    def test_one_word(self):
        text = "fcs"
        result = cap.cap_text(text)
        self.assertEqual(result,"Fcs")
    
    def test_multiple_words(self):
        text = "hi fcs"
        result = cap.cap_text(text)
        self.assertEqual(result,"Hi fcs")

if __name__ == '__main__':
    unittest.main()
    
