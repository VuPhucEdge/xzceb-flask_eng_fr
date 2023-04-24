import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_case_2(self):
        self.assertNotEqual(english_to_french('None'), '')

class TestFrenchToEnglish(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_case_2(self):
        self.assertNotEqual(french_to_english('None'), '')

unittest.main()