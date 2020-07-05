class TrieErrors(Exception):
    """Base class for Trie errors"""
    pass

class WordNotFoundException(TrieErrors):
    """Raised when word is not found during search"""
    pass

class WordLocations(object):

    def __init__(self, file_path: str, at_index: int, links: list):
        self._file_path = file_path
        self._at_index = at_index
        self._links = links

    @property
    def file_path(self):
        return self._file_path

    @property
    def at_index(self):
        return self._at_index

    @property
    def links(self):
        return self._links


class SearchResult(object):

    def __init__(self, locations: WordLocations, word):
        self._word = word
        self.file_locations = locations

class TrieNode(object):

    def __init__(self, char: str):
        self._char = char
        self.parent: TrieNode or None = None
        self.children = {}
        self.locations = []
        self.indices = []

    @property
    def char(self):
        return self._char

    @property
    def is_word(self):
        return len(self.locations) > 0

class Trie(object):

    def __init__(self):
        root = TrieNode("*")
        self._root = root
        self._length = 1
        self._word_count = 0
        self._words = set()

    @property
    def root(self):
        return self._root

    @property
    def words(self):
        return self._words

    def __len__(self):
        return self._length

    def add_word(self, word, location):
        self._words.add(word)
        node = self._root
        for character in word[:-1]:
            node = self._add_character(character, node)

        # Addition for last character
        last_character = word[-1]
        self._add_character(last_character, node, location, end=True)

    def _add_character(self, character, node, location=None, end=False):
        if character not in node.children:
            char_node = TrieNode(character)
            char_node.parent = node
            node.children[character] = char_node
            self._length += 1

        else:
            char_node = node.children[character]

        if end:
            file_path = location.file_path
            index = location.at_index

            char_node.locations.append(file_path)
            char_node.indices.append(index)
            self._word_count += 1

        return char_node

    def search(self, word):
        """Searches for a word in the trie

        :param word: word for which to search
        :return:
        """
        if word not in self._words:
            raise WordNotFoundException

        search_results = self._search(word, self._root)


        return search_results[0], search_results[1]

    def _search(self, word, node):
        char = word[0]

        # Base case if word is one character
        if word in node.children and node.children[word].is_word:
            return node.children[word].locations, node.children[word].indices

        if char in node.children:
            next_node = node.children[char]
            return self._search(word[1:], next_node)



if __name__ == '__main__':
    from word_search.data_structure_initialisation import initialise_structures
    trie = initialise_structures()

    trie.search("python")

    test = True



