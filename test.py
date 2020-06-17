import cProfile
from word_search.html_parser import Parser
from word_search.trie import Trie, WordLocation
from word_search.trie_initialisation import initialise_trie

# Trie test ############################################################################################################
#
# def func():

#     import os
#     trie = Trie()
#     separator = os.sep
#     for (dirpath, dirnames, filenames) in os.walk("."):
#         for file in filenames:
#             if file.endswith(".html"):
#                 path = dirpath + separator + file
#                 html_file_contents = Parser().parse(path)
#                 word_list = html_file_contents[1]
#                 for word, index in zip(word_list, range(len(word_list))):
#                     file_path = path
#                     location = WordLocation(file_path, index)
#                     trie.add_word(word.lower(), location)
#     return trie
#
# print("Loading files...")
# cProfile.run("func()")
# print("Loading done.")
#
# title = "OVO JE TEST"

# Search test ##########################################################################################################
trie = initialise_trie()
word = "python"
cProfile("trie.search(word)")


# PQueue test ##########################################################################################################


