import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    
    # def test_frenchToEnglishNullInput(self):
    #     self.assertEqual(french_to_english(NULL),NULL);
        
    # def test_englishToFrenchNullInput(self):
    #     self.assertEqual(english_to_french(NULL),NULL);
        
    def test_englishToFrenchHello(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour");
        
    def test_frenchToEnglishHello(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello");
        
    if __name__ == '__main__':
        unittest.main()
        
        