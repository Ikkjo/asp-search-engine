import os
import pickle

from word_search.html_parser import Parser
from word_search.trie import Trie, WordLocation


def initialise_trie():
    print("Loading trie data from file...")
    separator = os.sep
    trie_data_path = "." + separator + "data" + separator + "trie.data"

    if os.path.exists(trie_data_path) and os.path.isfile(trie_data_path):
        trie = load_trie(trie_data_path)

    else:
        print("No data file found. Making trie...")
        trie = make_trie()
        print("Saving trie to file...")
        save_trie(trie_data_path, trie)

    print("Trie loaded.")
    return trie


def make_trie():
    separator = os.sep
    trie = Trie()
    for (dirpath, dirnames, filenames) in os.walk("."):
        for file in filenames:

            if file.endswith(".html"):

                path = dirpath + separator + file
                html_file_contents = Parser().parse(path)
                word_list = html_file_contents[1]

                for word, index in zip(word_list, range(len(word_list))):
                    file_path = path
                    location = WordLocation(file_path, index)
                    trie.add_word(word.lower(), location)
    return trie


def save_trie(file_path, trie):
    with open(file=file_path, mode="wb") as trie_file:
        pickle.dump(trie, file=trie_file)

def load_trie(file_path):
    with open(file=file_path, mode="rb") as trie_file:
        trie = pickle.load(trie_file)
    return trie


if __name__ == '__main__':
    trie = initialise_trie()
    a = ""
