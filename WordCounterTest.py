# Testing each of the methods against the truth values given in the DreamBroker challenge

import unittest
import WordCounter as wc
import json


class WordCounterTest(unittest.TestCase):
    def test_text_length(self):
        c = wc.Count("hello 2 times  ")
        truth = json.dumps({"withSpaces":15,"withoutSpaces":11}, separators=(',', ':'))
        self.assertEqual(c.text_length(), truth)

    def test_word_count(self):
        c = wc.Count("hello 2 times  ")
        self.assertEqual(c.word_count(), 3)

    def test_character_count(self):
        c = wc.Count("hello 2 times  ")
        truth = json.dumps([{"e":2},{"h":1},{"i":1},{"l":2},{"m":1},{"o":1},{"s":1},{"t":1}], separators=(',', ':'))
        self.assertEqual(c.character_count(), truth)


if __name__ == '__main__':
    unittest.main()
