from collections import Counter
import re
import json


def with_spaces(word):
    return len(word)


def without_spaces(word):
    return len(word) - word.count(' ')


class Count:
    def __init__(self, sentence):
        self.sentence = sentence

    def word_count(self):
        res = len(self.sentence.split())
        return res

    def character_count(self):
        res = Counter(self.sentence)
        for key in res.copy():
            if not re.search(r'[a-zA-Z]', key):
                res.pop(key)

        return json.dumps(sorted(res.items()), separators=(',', ':')) \
            .replace('[', '{').replace(']', '}').replace('{{', '[{').replace('}}', '}]').replace('",', '":')

    def text_length(self):
        return json.dumps({"withSpaces": with_spaces(self.sentence),
                           "withoutSpaces": without_spaces(self.sentence)}, separators=(',', ':'))


class Print:
    def __init__(self, sentence):
        self.c = Count(sentence)

    def print(self):
        return json.dumps({"textLength": self.c.text_length(),
                           "wordCount": self.c.word_count(),
                           "characterCount": self.c.character_count()}, separators=(',', ':')).replace('\\', '').replace('"{', '{')\
                                                                          .replace('}"', '}').replace('"[', '[').replace(']"', ']')

