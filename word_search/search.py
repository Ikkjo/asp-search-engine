from heapq import heappush, heappop

from igraph import Graph

from word_search.trie import WordNotFoundException

TXT_G = "\033[32m"
TXT_RESET = "\033[0m"


AND = "AND"
OR = "OR"
NOT = "NOT"
ALLOWED_OPERATORS = (AND, OR, NOT)

class SearchError(Exception):
    pass


class NoOccurrencesException(SearchError):
    pass


class ResultItem(object):

    def __init__(self, search_query, file_path, indices, rank=0):

        self._search_query = search_query
        self._file_path = file_path
        self._indices = indices
        self._rank = rank


    def add_to_rank(self, value: int):
        self._rank += value

    def sub_from_rank(self, value: int):
        self._rank -= value

    @property
    def search_query(self):
        return self._search_query

    @property
    def file_path(self):
        return self._file_path

    @property
    def rank(self):
        return self._rank

    @property
    def indices(self):
        return self._indices

    def __eq__(self, other):
        if isinstance(other, ResultItem):
            return self._file_path == other.file_path

        return self._file_path == other

    def __ne__(self, other):
        if isinstance(other, ResultItem):
            return self._file_path == other.file_path

        return self._file_path == other

def search(search_query, trie, file_graph, html_index, smallest_first=False, console_log=False):
    # if console_log:
    #     print(f"Word \"{search_query}\" was searched for")

    try:
        results = get_results(search_query, trie, file_graph)

    except WordNotFoundException:
        raise NoOccurrencesException

    formatted_results = []
    for result in results:
        f_r = format_for_sorting(result, file_graph, html_index)
        formatted_results.append(f_r)

    return heapsort_dict(formatted_results, smallest_first)


def format_for_sorting(result, graph, html_index):
    output = {}


    rank = result.rank
    output["word"] = result.search_query
    output["path"] = result.file_path

    # html = html_index[result.file_path]
    # text = html.get_text
    # for index in result.indices:
    #     color_word = TXT_G + text[index] + TXT_RESET
    #     start = index - 5 if index > 5 else index
    #     end = index + 5 if index < len(text) - 5 else index
    #
    #     while start != index and end != index:
    #         first =
    #
    #     output[str(index)] =


    return (rank, output)


def heapsort_dict(formatted_results, smallest_first):
    from dataclasses import dataclass, field
    from typing import Any

    @dataclass(order=True)
    class PrioritizedItem:
        priority: int
        item: Any = field(compare=False)

    heap = []
    for result in formatted_results:

        heappush(heap, PrioritizedItem(result[0], result))

    ret_list = [heappop(heap) for i in range(len(heap))]
    if not smallest_first:
        ret_list = list(reversed(ret_list))

    return ret_list

def get_results(search_query, trie, graph):
    results = []

    first_word = search_query[0]
    second_word = None
    operator = None
    if len(search_query) == 3:
        if search_query[1] in ALLOWED_OPERATORS:
            operator = search_query[1]
        second_word = search_query[2]

    results = rank_search_query(first_word, second_word, operator, graph, trie, results)

    return results

def rank_search_query(first_word, second_word, operator, graph, trie, results: list):
    file_scope = set()
    search_res = []

    first_locations, f_indices = trie.search(first_word)
    first_locations = set(first_locations)
    if operator is not None:
        second_locations, s_indices = trie.search(second_word)
        second_locations = set(second_locations)
        if operator == AND:
            file_scope = first_locations.intersection(second_locations)
            search_res = search_and(first_word, second_word, graph, file_scope)

        elif operator == OR:
            file_scope.add(first_locations)
            file_scope.add(second_locations)
            search_res = search_or(first_word, second_word, graph, file_scope)

        elif operator == NOT:
            file_scope = first_locations.difference(second_locations)
            search_res = search_not(first_word, graph, file_scope)

    else:
        search_res = search_not(first_word, graph, file_scope)

    results = search_res

    return results

def search_and(first_word, second_word, graph: Graph, scope):

    results = []


    for filename in list(scope):

        file = graph.vs.find(name=filename)

        first_rank = 0
        second_rank = 0

        f_loc, first_indices = file["trie"].search(first_word)
        s_loc, second_indices = file["trie"].search(second_word)

        first_rank += len(first_indices)

        second_rank += len(second_indices)

        edge_links = graph.incident(file)

        first_rank += len(edge_links)
        second_rank += len(edge_links)

        for link in graph.es.select(edge_links):
            link_vert = link.target_vertex
            try:

                floc, findi = link_vert["trie"].search(first_word)
                sloc, sindi = link_vert["trie"].search(second_word)
                first_rank += len(findi)
                second_rank += len(sindi)

            except WordNotFoundException:
                continue

        results.append(ResultItem(first_word, file["name"], first_indices, first_rank))
        results.append(ResultItem(second_word, file["name"], second_indices, second_rank))

    return results

def search_or(first_word, second_word, graph, scope):
    pass

def search_not(word, graph, scope):
    pass


