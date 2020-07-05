from os.path import abspath

def print_results(results: list, abs=True):
    for result in results:
        res = result.item
        rank = res[0]
        out = res[1]
        word = out["word"]
        path = out["path"]

        print(f"Searched for {word}, found in file {path} (Rank: {rank})")
