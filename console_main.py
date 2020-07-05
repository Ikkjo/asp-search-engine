from view.console.word_input import search_query_input
from view.console.search_result_output import print_results
from word_search.search import search, NoOccurrencesException
from view.console.errors import no_occurrences
from word_search.data_structure_initialisation import initialise_structures
from word_search.autocompleter import AutoCompleter
import readline

def run():
    trie, graph, html_index = initialise_structures()
    ac = AutoCompleter(trie.words)
    readline.set_completer(ac.complete)
    readline.parse_and_bind('tab: complete')
    words = search_query_input().split(" ")
    search_query = []
    words_to_search = set()
    for word in words:
        if word != "" and word not in words_to_search:
            search_query.append(word)
            words_to_search.add(word)

    try:
        print_results(search(search_query, trie, graph, html_index, console_log=True))

    except NoOccurrencesException:
        no_occurrences()

if __name__ == '__main__':
    run()