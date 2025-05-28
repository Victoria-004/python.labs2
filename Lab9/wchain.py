def read_input(filename):
    with open(filename, 'r') as f:
        N = int(f.readline())
        words = [f.readline().strip() for _ in range(N)]
    return N, words

def build_graph(words):
    graph = {}
    words_set = set(words)

    for word in words:
        graph[word] = []
        for i in range(len(word)):
            new_word = word[:i] + word[i + 1:]
            if new_word in words_set:
                graph[word].append(new_word)
    return graph

def find_longest_chain(graph):
    memo = {}

    def dp(word):
        if word in memo:
            return memo[word]

        best_path = [word]
        for next_word in graph[word]:
            candidate_path = dp(next_word)
            if len(candidate_path) + 1 > len(best_path):
                best_path = [word] + candidate_path

        memo[word] = best_path
        return best_path

    longest_chain = []
    for word in graph:
        path = dp(word)
        if len(path) > len(longest_chain):
            longest_chain = path

    return longest_chain

def solve(input_file, output_file):
    N, words = read_input(input_file)
    graph = build_graph(words)
    longest_chain = find_longest_chain(graph)

    with open(output_file, 'w') as f:
        f.write(str(len(longest_chain)) + '\n')

    print(len(longest_chain))

solve('wchain.in', 'wchain.out')
