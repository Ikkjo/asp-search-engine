class HTMLFile(object):

    def __init__(self, path):
        self._path = path
        self._word_set = set()
        self._text = []

    def add_word(self, word):
        self._word_set.add(word)
        self._text.append(word)

    def get_text(self):
        return self._text

    def set_text(self, text: list):
        for word in text:
            self._word_set.add(word)

        self._text = text

    def contains(self, word):
        return word in self._word_set

    @property
    def path(self):
        return self._path
