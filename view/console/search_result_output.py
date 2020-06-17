from os.path import abspath

def print_results(results: list, abs=True):
    for result in results:
        occurrences = result[0]
        file = abspath(result[1]) if abs else result[1]

        ocu_str = "occurrence" if occurrences == 1 else "occurrences"
        print(f"{occurrences} {ocu_str} found in file {file}")
