import os
import pickle

from word_search.html_parser import Parser
from word_search.trie import Trie, WordLocation

separator = os.sep
DEFAULT_ROOT = os.curdir

def initialise_trie(root_dir=DEFAULT_ROOT, console_log=False):
    """Initialises trie from all .html files (recursively) starting from root_dir

    Tries to find an already made trie file in root_dir\data\trie.data. If file trie.data is not found, the funcion
    searches for all .hmtl files starting from the root dir, parses the text from them and adds them to a Trie structure
    and then saves that object in a binary file using the pickle library (file is saved in root_dir\data\ folder)

    :param root_dir: root_directory from which to search fro .html files
    :return: Trie of all words in found .html files
    """
    if console_log:
        print("Loading trie data from file...")

    trie_data_path = root_dir + separator+ "word_search"+ separator + "data" + separator + "trie.data"

    if os.path.exists(trie_data_path) and os.path.isfile(trie_data_path):
        trie = load_trie(trie_data_path)

    else:
        if console_log:
            print("No data file found. Making trie...")
        trie = make_trie()
        if console_log:
            print("Saving trie to file...")
        save_trie(trie_data_path, trie)

    if console_log:
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
    trie = initialise_trie(".")
    a = ""
