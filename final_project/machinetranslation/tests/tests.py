import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('What is the weather?'),
            "Quel est le temps?")
        self.assertNotEqual(english_to_french('How are you today?'),
            "Bonjour")
        with self.assertRaises(ValueError):
            english_to_french(None)
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Quel est le temps?"),
            "What is the weather?")
        self.assertNotEqual(french_to_english("Comment es-tu aujourd'hui?"),
            "Hello")
        with self.assertRaises(ValueError):
            french_to_english(None)
        self.assertEqual(french_to_english('Bonjour'),'Hello')

if __name__=="__main__":
    unittest.main()
