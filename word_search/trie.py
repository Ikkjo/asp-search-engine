class WordLocation(object):

    def __init__(self, file_path: str, at_index: int):
        self._file_path = file_path
        self._at_index = at_index

    @property
    def file_path(self):
        return self._file_path

    @property
    def at_index(self):
        return self._at_index


class TrieNode(object):

    def __init__(self, char: str):
        self._char = char
        self.parent: TrieNode or None = None
        self.children = {}
        self.location = {}

    @property
    def char(self):
        return self._char

    @property
    def is_word(self):
        return len(self.location) > 0

class Trie(object):

    def __init__(self):
        root = TrieNode("*")
        self._root = root
        self._length = 1
        self._word_count = 0

    @property
    def root(self):
        return self._root

    def __len__(self):
        return self._length

    def add_word(self, word, location):
        node = self._root
        for character in word[:-1]:
            node = self._add_character(character, node)
        # Addition for last character
        last_character = word[-1]
        self._add_character(last_character, node, location, end=True)




    def _add_character(self, character, node, location=None , end=False):
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

            if file_path not in char_node.location:
                char_node.location[file_path] = []
            char_node.location[file_path].append(index)
            self._word_count += 1

        return char_node

if __name__ == '__main__':
    trie = Trie()
    trie.add_word("bubac", None)
    trie.add_word("bubanj", None)
    trie.add_word("bubrovnik", None)
    trie.add_word("sloj", None)
    trie.add_word("buba", None)
    trie.add_word("abuka", None)



