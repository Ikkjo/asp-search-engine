from view.console.word_input import search_word_input
from view.console.search_result_output import print_results
from word_search.search import search, NoOccurrencesException
from view.console.errors import no_occurrences
from word_search.trie_initialisation import initialise_trie

def run():
    trie = initialise_trie()
    words = search_word_input().split(" ")
    search_words = []
    words_to_search = set()
    for word in words:
        if word != "" and word not in words_to_search:
            search_words.append(word)
            words_to_search.add(word)

    try:
        for word in search_words:
            log = True if len(search_words) > 1 else False
            print_results(search(word, trie, console_log=log))

    except NoOccurrencesException:
        no_occurrences()

if __name__ == '__main__':
    run()