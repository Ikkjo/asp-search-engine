import os
import pickle

from word_search.html_parser import Parser
from word_search.trie import Trie, WordLocations

separator = os.sep
DEFAULT_ROOT = os.curdir


def initialise_structures(root_dir=DEFAULT_ROOT, console_log=False):
    """Initialises trie from all .html files (recursively) starting from root_dir

    Tries to find an already made trie file in root_dir\data\trie.data. If file trie.data is not found, the funcion
    searches for all .html files starting from the root dir, parses the text from them and adds them to a Trie structure
    and then saves that object in a binary file using the pickle library (file is saved in root_dir\data\ folder)

    :param root_dir: root_directory from which to search fro .html files
    :return: Trie of all words in found .html files
    """
    if console_log:
        print("Loading trie data from file...")

    trie_data_path = root_dir + separator + "word_search" + separator + "data" + separator + "trie.data"
    file_graph_path = root_dir + separator + "word_search" + separator + "data" + separator + "file_graph.data"

    if (os.path.exists(trie_data_path) and os.path.isfile(trie_data_path)) and\
       (os.path.exists(file_graph_path) and os.path.isfile(file_graph_path)):  # Check to see if trie and graph data
                                                                               # files exist
        trie, graph = load_structures(trie_data_path, file_graph_path)

    else:
        if console_log:
            print("No data file found. Making trie...")
        trie, graph = make_structures()
        if console_log:
            print("Saving trie to file...")
        save_structures(trie_data_path, file_graph_path, trie, graph)

    if console_log:
        print("Trie loaded.")
    return trie, graph


def make_structures():
    separator = os.sep
    trie = Trie()
    file_graph = Graph()
    for (dirpath, dirnames, filenames) in os.walk("."):
        for file in filenames:

            if file.endswith(".html"):

                path = dirpath + separator + file
                html_file_contents = Parser().parse(path)
                word_list = html_file_contents[1]
                links = html_file_contents[0]

                for word, index in zip(word_list, range(len(word_list))):
                    file_path = path
                    location = WordLocations(file_path, index, links)
                    trie.add_word(word.lower(), location)
    return trie


def load_structures(trie_path, graph_path):
    trie = load_from_file(trie_path)
    graph = load_from_file(graph_path)
    return trie, graph


def save_structures(trie_path, graph_path, trie, graph):
    save_to_file(trie_path, trie)
    save_to_file(graph_path, graph)


def save_to_file(file_path, trie):
    with open(file=file_path, mode="wb") as trie_file:
        pickle.dump(trie, file=trie_file)


def load_from_file(file_path):
    with open(file=file_path, mode="rb") as trie_file:
        trie = pickle.load(trie_file)
    return trie


# if __name__ == '__main__':
#     trie = initialise_structures(".")
#     a = ""
