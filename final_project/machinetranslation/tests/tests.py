import unittest

from translator import english_to_french, french_to_english

class Test_englishtofrench(unittest.TestCase):
   def teste2f(self):
        self.assertNotEqual(english_to_french('Null'), 'Nul')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')

class Test_frenchToenglish(unittest.TestCase):
   def testf2e(self):
        self.assertNotEqual(french_to_english('Null'), 'Nul')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')

unittest.main()
