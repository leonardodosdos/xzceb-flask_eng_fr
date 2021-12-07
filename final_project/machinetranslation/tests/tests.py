import unittest

from machinetranslation import translator
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def testForNull(self): 
        self.assertIsNone(english_to_french(None))

    def testTranslation(self):
        translation = english_to_french('Hello')
        self.assertEqual(translation['translations'][0]['translation'], 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase): 
    def testForNull(self): 
        self.assertIsNone(french_to_english(None))
    
    def testTranslation(self):
        translation = french_to_english('Bonjour')
        self.assertEqual(translation['translations'][0]['translation'], 'Hello')


unittest.main()