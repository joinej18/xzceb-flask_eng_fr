import unittest

from translator import english_to_french, french_to_english

class Test_englishtofrench(unittest.TestCase)
   def teste2f(self)
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Thank you'), 'Je vous remercie')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')

class Test_frenchToenglish(unittest.TestCase):
   def testf2e(self):
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english('Je vous remercie'), 'Thank you')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')

unittest.main()
