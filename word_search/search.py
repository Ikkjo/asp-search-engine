from heapq import heappush, heappop

from word_search.trie_initialisation import initialise_trie

class SearchError(Exception):
    pass

class NoOccurrencesException(SearchError):
    pass

def search(search_word, trie, smallest_first=False, console_log=False):


    if console_log:
        print(f"Word \"{search_word}\" was searched for")

    results = trie.search(search_word)

    if len(results) == 0:
        raise NoOccurrencesException("No occurrences found in all files!")

    return heapsort_dict(results, smallest_first)


def heapsort_dict(results, smallest_first):
    heap = []
    for location in results:
        occurrences = len(results[location])
        pair = (occurrences, location)
        heappush(heap, pair)

    if smallest_first:
        return [heappop(heap) for i in range(len(heap))]
    else:
        return reversed([heappop(heap) for i in range(len(heap))])
